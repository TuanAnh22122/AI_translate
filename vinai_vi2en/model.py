from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from config import MODEL_NAME, DEVICE, SRC_LANG

print(f"Loading model: {MODEL_NAME} on {DEVICE}...")

# Load Tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, src_lang=SRC_LANG)

# Load Model
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(DEVICE)
model.eval()  # Chuyển sang chế độ eval ngay khi load

print("Model loaded successfully!")