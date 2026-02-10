import torch
from config import DEVICE, MAX_LENGTH, NUM_BEAMS, TGT_LANG_CODE
from model import model, tokenizer

def execute_translation(text: str) -> str:
    """
    Hàm thực hiện dịch từ tiếng Việt sang tiếng Anh
    """
    # Lấy token ID bắt buộc cho ngôn ngữ đích
    forced_bos_token_id = tokenizer.lang_code_to_id[TGT_LANG_CODE]

    # Tokenize input
    inputs = tokenizer(
        text, 
        return_tensors="pt", 
        padding=True, 
        truncation=True, 
        max_length=MAX_LENGTH
    ).to(DEVICE)

    # Generate (Inference)
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs,
            decoder_start_token_id=forced_bos_token_id,
            num_beams=NUM_BEAMS,
            max_new_tokens=MAX_LENGTH,
            early_stopping=True
        )

    # Decode kết quả
    translation = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translation