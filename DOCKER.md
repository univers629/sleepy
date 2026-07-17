安装 Docker：

```bash
curl -fsSL https://get.docker.com | sh
```

验证 Docker 安装：

```bash
docker -v
```

验证 docker-compose 安装：

```bash
docker compose version
```

进入 root 目录：

```bash
cd /root
```

克隆你的 sleepy 项目：

```bash
git clone --depth 1 https://github.com/univers629/sleepy.git
```

进入项目目录：

```bash
cd sleepy
```
安装依赖

```shell
pip install flask pytz --break-system-packages
```

先启动一遍程序:
```shell
python3 server.py
```

如果不出意外，会提示类似于下方内容，同时目录下出现`config.json` 文件
```python
[Warning] [2025-01-25 21:39:00] config.json not exist, creating
[Error] [2025-01-25 21:39:00] Create config.json failed: Generated new config file (config.json), please edit it and re-run this program.
[Warning] [2025-01-25 21:39:00] ==========
Generated new config file (config.json), please edit it and re-run this program. 
```
打开`config.json` 文件
```shell
nano config.json
```
会出现按照下面的说明编辑`config.json`文件，编辑完成后按`Ctrl+X`后按`Y`确认修改，最后按`回车键`退出(记得可以修改/static/favicon.ico)
```python
{
"version": "2025.1.18.1",
"debug": false,
"host": "0.0.0.0",
"port": 9010,
"timezone": "Asia/Shanghai",
"metrics": true,
"secret": "", # 这里填写你要设置的密码
"status_list": [
    {
        "id": 0,
        "name": "活着", # 可以更改成自己想要的状态
        "desc": "目前在线，可以通过任何可用的联系方式联系本人。", # 可以更改成自己想要的描述
        "color": "awake"
    },
    {
        "id": 1,
        "name": "似了", # 可以更改成自己想要的状态
        "desc": "睡似了或其他原因不在线，紧急情况请使用电话联系。", # 可以更改成自己想要的描述
        "color": "sleeping"
    }
],
"refresh": 20000, # 填写你要的网页自动刷新时间间隔，20000ms=20秒
"data_check_interval": 30,
"other": {
            "user": "User", # 填写你想在网页上显示的昵称
            "background": "https://imgapi.siiway.top/image",
            "alpha": 0.85,
            "learn_more": "搭建教程",
            "repo": "https://github.com/univers629/sleepy",
            "more_text": "＞﹏＜<br/>已被视奸 <span id='finicount_views'>(未知)</span> 次<script async src='https://finicounter.eu.org/finicounter.js'></script>", #这里还可以填你的联系方式
            "device_status_slice": 50 # 设备状态从开头截取多少文字显示 (防止窗口标题过长, 设置为 0 禁用)
}
}
```

构建并启动容器：

```bash
docker compose up --build -d
```

查看容器运行状态：

```bash
docker ps | grep sleepy
```