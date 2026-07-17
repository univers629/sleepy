FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口（v4.0 默认是 9010，看 config.json 里的 port）
EXPOSE 9010

# 启动
CMD ["python3", "server.py"]