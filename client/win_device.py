# coding: utf-8
"""Windows 前台窗口状态上报脚本（稳健版）。

依赖：pywin32、requests
    pip install pywin32 requests
"""

from __future__ import annotations

import atexit
import signal
import sys
import threading
from datetime import datetime
from time import monotonic

import requests
from win32gui import GetForegroundWindow, GetWindowText  # type: ignore

# --- config start -----------------------------------------------------------
# 可填服务根地址，或完整的 /device/set 地址。
SERVER = "https://你的域名地址"
SECRET = "填写服务端设置的密码"
DEVICE_ID = "device-1"
DEVICE_SHOW_NAME = "电脑"

# 轮询间隔；网络失败时下一个轮询会自动重试。
CHECK_INTERVAL = 3
# 即使窗口没有变化，也每隔此秒数发送一次心跳，避免服务端状态因某次丢包过期。
HEARTBEAT_INTERVAL = 60
# (连接超时, 读取超时)。过长会让脚本看似“卡住”。
REQUEST_TIMEOUT = (3, 8)

BYPASS_SAME_REQUEST = True
SKIPPED_NAMES = {
    "", "系统托盘溢出窗口。", "新通知", "任务切换", "快速设置", "通知中心", "搜索", "Flow.Launcher",
}
NOT_USING_NAMES = {"我们喜欢这张图片，因此我们将它与你共享。"}
REVERSE_APP_NAME = True
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


def foreground_title() -> str | None:
    """返回标题；返回 None 表示本轮读取 Windows API 失败，应在下轮重试。"""
    try:
        hwnd = GetForegroundWindow()
        return GetWindowText(hwnd) if hwnd else ""
    except Exception as error:
        log(f"读取前台窗口失败，将重试：{error}")
        return None


def post(using: bool, app_name: str) -> bool:
    """仅在服务端确认 2xx 后才返回成功。"""
    payload = {
        "secret": SECRET,
        "id": DEVICE_ID,
        "show_name": DEVICE_SHOW_NAME,
        "using": using,
        "app_name": app_name if using else "",
    }
    try:
        response = SESSION.post(URL, json=payload, timeout=REQUEST_TIMEOUT)
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

    title = foreground_title()
    if title is None:
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
    post(False, "")


def request_stop(*_args: object) -> None:
    STOP_EVENT.set()


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
    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)
    try:
        main()
    finally:
        report_offline()
