from fastapi import FastAPI, HTTPException
from render import TranslationRequest, TranslationResponse
from embedding import execute_translation
from config import DEVICE

app = FastAPI(title="VinAI Translate EN-VI Service")

@app.post("/translate-en2vi", response_model=TranslationResponse)
async def translate_endpoint(request: TranslationRequest):
    try:
        result_text = execute_translation(request.text)
        
        # --- SỬA ĐOẠN NÀY ---
        return TranslationResponse(
            input_en=request.text,  # Khớp với render.py
            output_vi=result_text,  # Khớp với render.py
            device=DEVICE
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "running", "model": "en2vi", "device": DEVICE}