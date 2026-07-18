# coding: utf-8
"""Windows 前台窗口状态上报脚本

依赖：pywin32、requests
    pip install pywin32 requests
"""

from __future__ import annotations

import atexit
import ctypes
import signal
import threading
from datetime import datetime
from time import monotonic

import requests
from win32gui import GetClassName, GetForegroundWindow, GetWindowText  # type: ignore

# --- config start -----------------------------------------------------------
# 可填服务根地址，或完整的 /device/set 地址。
SERVER = "https://你的域名"
SECRET = "你的服务端密码"
DEVICE_ID = "device-1"
DEVICE_SHOW_NAME = "电脑"

# 轮询间隔；网络失败时下一个轮询会自动重试。
CHECK_INTERVAL = 3
# 即使窗口没有变化，也每隔此秒数发送一次心跳，避免服务端状态因某次丢包过期。
HEARTBEAT_INTERVAL = 60
# 服务端偶尔响应较慢；单个整数同时作为连接和读取超时，避免元组配置歧义。
REQUEST_TIMEOUT = 15
# 点击控制台窗口的关闭按钮时，Windows 只给进程很短的清理时间。
SHUTDOWN_TIMEOUT = (1, 3)

BYPASS_SAME_REQUEST = True
SKIPPED_NAMES = {
    "", "系统托盘溢出窗口。", "新通知", "任务切换", "快速设置", "通知中心", "搜索", "Flow.Launcher",
}
NOT_USING_NAMES = {"我们喜欢这张图片，因此我们将它与你共享。"}
REVERSE_APP_NAME = True
# 没有前台窗口（通常是关闭当前应用后回到桌面）时，是否上报离线。
REPORT_OFFLINE_ON_EMPTY_TITLE = True
# 这些是 Windows 桌面和任务栏的窗口类；获得焦点时不代表用户正在使用某个应用。
NOT_USING_WINDOW_CLASSES = {"Progman", "WorkerW", "Shell_TrayWnd", "Shell_SecondaryTrayWnd"}
# --- config end -------------------------------------------------------------

URL = SERVER.rstrip("/")
if not URL.endswith("/device/set"):
    URL += "/device/set"

SESSION = requests.Session()
STOP_EVENT = threading.Event()
LAST_SUCCESSFUL_PAYLOAD: tuple[bool, str] | None = None
LAST_SUCCESSFUL_AT = 0.0
OFFLINE_REPORTED = False


def log(message: str) -> None:
    try:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}", flush=True)
    except Exception:
        pass


def display_name(title: str) -> str:
    if not REVERSE_APP_NAME:
        return title
    # 例如："文件 - VS Code" -> "VS Code - 文件"。
    return " - ".join(reversed(title.split(" - ")))


def foreground_window() -> tuple[int, str, str] | None:
    """返回（句柄，标题，窗口类）；None 表示本轮读取 Windows API 失败。"""
    try:
        hwnd = GetForegroundWindow()
        return (hwnd, GetWindowText(hwnd), GetClassName(hwnd)) if hwnd else (0, "", "")
    except Exception as error:
        log(f"读取前台窗口失败，将重试：{error}")
        return None


def post(
    using: bool,
    app_name: str,
    timeout: tuple[int, int] = REQUEST_TIMEOUT,
) -> bool:
    """仅在服务端确认 2xx 后才返回成功。"""
    payload = {
        "secret": SECRET,
        "id": DEVICE_ID,
        "show_name": DEVICE_SHOW_NAME,
        "using": using,
        "app_name": app_name if using else "",
    }
    try:
        response = SESSION.post(URL, json=payload, timeout=timeout)
        response.raise_for_status()
        try:
            result = response.json()
        except ValueError:
            result = response.text[:200] or "<empty response>"
        log(f"POST {response.status_code}: {result}")
        return True
    except requests.RequestException as error:
        # 不更新 LAST_SUCCESSFUL_*，因此下一轮会继续尝试，不会“卡在未上报”。
        log(f"上报失败，将在下次轮询重试：{error}")
        return False


def update() -> None:
    global LAST_SUCCESSFUL_PAYLOAD, LAST_SUCCESSFUL_AT

    window = foreground_window()
    if window is None:
        return
    _hwnd, title, window_class = window
    no_application = (
        (not title and REPORT_OFFLINE_ON_EMPTY_TITLE)
        or window_class in NOT_USING_WINDOW_CLASSES
    )
    if no_application:
        state = (False, "")
        now = monotonic()
        if state != LAST_SUCCESSFUL_PAYLOAD or now - LAST_SUCCESSFUL_AT >= HEARTBEAT_INTERVAL:
            log(f"前台为桌面/任务栏（类：{window_class or '无'}），正在上报离线状态")
            if post(False, ""):
                LAST_SUCCESSFUL_PAYLOAD = state
                LAST_SUCCESSFUL_AT = now
        return
    if title in SKIPPED_NAMES:
        return

    using = title not in NOT_USING_NAMES
    app_name = display_name(title) if using else ""
    state = (using, app_name)
    now = monotonic()
    unchanged = state == LAST_SUCCESSFUL_PAYLOAD
    heartbeat_due = now - LAST_SUCCESSFUL_AT >= HEARTBEAT_INTERVAL
    if BYPASS_SAME_REQUEST and unchanged and not heartbeat_due:
        return

    log(f"窗口：{title!r}；上报：using={using}, app_name={app_name!r}")
    if post(using, app_name):
        LAST_SUCCESSFUL_PAYLOAD = state
        LAST_SUCCESSFUL_AT = now


def report_offline() -> None:
    """正常退出时尽力发送离线状态；最多阻塞 REQUEST_TIMEOUT 的读取时间。"""
    global OFFLINE_REPORTED
    if OFFLINE_REPORTED:
        return
    OFFLINE_REPORTED = True
    log("正在上报离线状态")
    post(False, "", timeout=SHUTDOWN_TIMEOUT)


def request_stop(*_args: object) -> None:
    STOP_EVENT.set()


# Ctrl+C 会触发 signal；但直接点击 cmd/PowerShell 窗口的 × 会发送
# CTRL_CLOSE_EVENT，Python 不会将它转换为 SIGTERM。必须使用 Windows API 接住它。
CTRL_CLOSE_EVENT = 2
CTRL_LOGOFF_EVENT = 5
CTRL_SHUTDOWN_EVENT = 6
CONSOLE_HANDLER = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_uint)


@CONSOLE_HANDLER
def console_close_handler(event: int) -> bool:
    if event in {CTRL_CLOSE_EVENT, CTRL_LOGOFF_EVENT, CTRL_SHUTDOWN_EVENT}:
        try:
            report_offline()  # 同步请求，必须在返回给 Windows 前完成。
        except Exception:
            pass
    # 返回 False：让 Windows 在清理完毕后继续默认的退出流程。
    return False


def install_console_close_handler() -> None:
    try:
        ctypes.windll.kernel32.SetConsoleCtrlHandler(console_close_handler, True)
    except Exception as error:
        log(f"无法注册窗口关闭处理器：{error}")


def main() -> None:
    log(f"启动，目标：{URL}")
    while not STOP_EVENT.is_set():
        try:
            update()
        except Exception as error:
            # 防止任何未预料的单次异常结束整个常驻脚本。
            log(f"本轮发生未预料异常，将继续运行：{error}")
        STOP_EVENT.wait(CHECK_INTERVAL)


if __name__ == "__main__":
    atexit.register(report_offline)
    install_console_close_handler()
    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)
    try:
        main()
    finally:
        report_offline()
