# 1. 使用官方 Python 基础镜像
FROM python:3.11

# 2. 设置工作目录
WORKDIR /app

# 3. 将 requirements.txt 复制到工作目录中
COPY requirements.txt .

# 4. 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 5. 将当前目录下的所有文件复制到工作目录中
COPY . .

# 6. 暴露应用程序的端口（假设你的服务运行在 8000 端口）
EXPOSE 8000

# 7. 使用 Uvicorn 启动应用程序
#    这里假设你的 FastAPI 或者类似的应用位于 smtpService/app.py 中，并且定义了 app 对象
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
