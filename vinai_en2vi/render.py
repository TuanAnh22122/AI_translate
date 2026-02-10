from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    input_en: str  # Đổi thành input_en
    output_vi: str # Đổi thành output_vi
    device: str