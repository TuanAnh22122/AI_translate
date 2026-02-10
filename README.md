# AI_translate

## 📌 Giới thiệu
**AI_translate** là một dự án xây dựng hệ thống dịch máy **Anh ↔ Việt** dựa trên các mô hình NLP, được đóng gói và triển khai dưới dạng **microservices** bằng Docker. Dự án hướng tới việc cung cấp một API dịch thuật đơn giản, dễ mở rộng và có thể triển khai nhanh trong môi trường local hoặc server.

Kiến trúc dự án được tách thành các thành phần riêng biệt:
- Dịch **English → Vietnamese**
- Dịch **Vietnamese → English**
- **Gateway API** làm trung gian xử lý request

---

## 🏗️ Kiến trúc tổng quan

```
AI_translate/
├── vinai_en2vi/        # Service dịch English → Vietnamese
├── vinai_vi2en/        # Service dịch Vietnamese → English
├── vinai_gateway/      # API Gateway
├── docker-compose.yml  # Orchestration các service
└── README.md           # Tài liệu dự án
```

---

## 🧠 Các thành phần chính

### 1️⃣ vinai_en2vi
- Chịu trách nhiệm dịch **tiếng Anh sang tiếng Việt**
- Sử dụng mô hình vinai/vinai-translate-en2vi-v2
- Được đóng gói như một service độc lập

### 2️⃣ vinai_vi2en
- Chịu trách nhiệm dịch **tiếng Việt sang tiếng Anh**
- Kiến trúc tương tự `vinai/vinai-translate-vi2en-v2`
- Được đóng gói như một service độc lập

### 3️⃣ vinai_gateway
- Đóng vai trò **API Gateway**
- Nhận request từ client
- Tự động định tuyến request đến service dịch phù hợp
- Có thể mở rộng để:
  - Logging
  - Rate limiting
  - Authentication

---

## 🚀 Cách chạy dự án

### 🔧 Yêu cầu hệ thống
- Docker >= 20.x
- Docker Compose >= v2
- Linux / macOS / Windows (WSL khuyến nghị)

---

### ▶️ Chạy bằng Docker Compose

```bash
git clone https://github.com/TuanAnh22122/AI_translate.git
cd AI_translate
docker compose up --build
```

Sau khi chạy thành công, các service sẽ được khởi động đồng thời.

---

## 🔌 API Usage (Ví dụ)

### 📥 Request dịch Anh → Việt
```json
curl -X 'POST' \
  'http://127.0.0.1:8080/translate?vi2en=true&text=xin%20ch%C3%A0o' \
  -H 'accept: application/json' \
  -d ''
```

### 📤 Response
```json
{
  "input_vi": "xin chào",
  "output_en": "hello there.",
  "device": "cuda"
}
```

---

## ⚙️ Cấu hình

- Các cấu hình model, port, device (CPU/GPU) có thể được chỉnh trong:
  - `Dockerfile`
  - `docker-compose.yml`
- Có thể mở rộng để chạy GPU bằng cách thêm:
  ```yaml
  deploy:
    resources:
      reservations:
        devices:
          - driver: nvidia
            capabilities: [gpu]
  ```

---

## 📈 Hướng phát triển
- [ ] Thêm README chi tiết cho từng service
- [ ] Hỗ trợ batch translation
- [ ] Thêm logging & monitoring (Prometheus, Grafana)
- [ ] Benchmark tốc độ & độ chính xác
- [ ] Thêm giao diện Web UI

---

## 👤 Tác giả
- **Tuấn Anh Trần**
- GitHub: https://github.com/TuanAnh22122

---

## 📜 License
Dự án được phát hành cho mục đích **học tập và nghiên cứu**. Vui lòng kiểm tra license của các mô hình AI được sử dụng trước khi triển khai thương mại.

---

✨ Nếu bạn muốn mình viết thêm README cho từng service, sơ đồ kiến trúc, hoặc API spec (OpenAPI/Swagger) — cứ nói nhé!

