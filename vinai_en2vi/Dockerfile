# 1. Dùng Base Image Pytorch (Giữ nguyên như bạn muốn)
FROM pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime

WORKDIR /app

# 2. Cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy code (app.py, render.py, model.py...)
COPY . .

# 4. QUAN TRỌNG: Model Service chạy cổng 8000 (Không phải 8080)
EXPOSE 8000

# 5. QUAN TRỌNG: Chạy app:app (Không phải main:app) và Host 0.0.0.0
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]