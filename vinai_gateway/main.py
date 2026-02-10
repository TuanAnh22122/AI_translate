from fastapi import FastAPI, HTTPException
import httpx
import os  # <--- BẮT BUỘC PHẢI IMPORT THƯ VIỆN NÀY

app = FastAPI(title="VinAI Unified Gateway")

# --- SỬA LẠI PHẦN CẤU HÌNH ---
# Dùng os.getenv để lấy địa chỉ từ Docker Compose truyền vào.
# Nếu không tìm thấy biến môi trường, nó mới dùng giá trị mặc định (để test lẻ).

# Lưu ý: Tên biến môi trường (trong ngoặc kép) phải khớp với file docker-compose.yml
URL_VI2EN = os.getenv("VI2EN_URL", "http://vi2en-service:8000/translate-vi2en")
URL_EN2VI = os.getenv("EN2VI_URL", "http://en2vi-service:8000/translate-en2vi")

print(f"DEBUG CONFIG: VI2EN={URL_VI2EN}")
print(f"DEBUG CONFIG: EN2VI={URL_EN2VI}")

@app.post("/translate")
async def translate_gateway(vi2en: bool, text: str):
    """
    API Tổng hợp:
    - vi2en=True:  Gọi model Việt -> Anh
    - vi2en=False: Gọi model Anh -> Việt
    """
    
    # 1. Chọn đường dẫn
    if vi2en:
        target_url = URL_VI2EN
    else:
        target_url = URL_EN2VI

    # 2. Đóng gói dữ liệu
    payload = {"text": text}

    # 3. Gửi request
    async with httpx.AsyncClient() as client:
        try:
            # Timeout 60s vì model AI load lần đầu rất lâu
            response = await client.post(target_url, json=payload, timeout=60.0)
            
            # Nếu Model trả về lỗi (ví dụ 500 hoặc 404)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Lỗi từ Model Service ({target_url}): {response.text}"
                )
            
            return response.json()

        except httpx.RequestError as e:
            # In lỗi chi tiết ra để debug
            print(f"Lỗi kết nối tới {target_url}: {e}")
            raise HTTPException(
                status_code=503, 
                detail=f"Không thể kết nối tới Model Service tại {target_url}. Kiểm tra xem container model đã chạy xong chưa?"
            )

@app.get("/health")
def health_check():
    return {"status": "Gateway is active"}