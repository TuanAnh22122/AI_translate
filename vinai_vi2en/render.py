from pydantic import BaseModel

# Input schema
class TranslationRequest(BaseModel):
    text: str

# Output schema
class TranslationResponse(BaseModel):
    input_vi: str
    output_en: str
    device: str