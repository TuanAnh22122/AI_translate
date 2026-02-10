# Dùng python bản nhẹ (Slim) để tiết kiệm dung lượng
FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime

WORKDIR /app

# Cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Mở cổng 8080 (Cổng cho Gateway)
EXPOSE 8080

# Chạy app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]