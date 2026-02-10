from fastapi import FastAPI, HTTPException
from render import TranslationRequest, TranslationResponse
from embedding import execute_translation
from config import DEVICE

app = FastAPI(title="VinAI Translate VI-EN Service")

@app.post("/translate-vi2en", response_model=TranslationResponse)
async def translate_endpoint(request: TranslationRequest):
    try:
        # Gọi hàm xử lý logic từ file embedding.py
        result_text = execute_translation(request.text)
        
        return TranslationResponse(
            input_vi=request.text,
            output_en=result_text,
            device=DEVICE
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "running", "device": DEVICE}