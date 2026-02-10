import torch

# Tên model trên HuggingFace
MODEL_NAME = "vinai/vinai-translate-en2vi-v2"

# Thiết lập thiết bị (GPU/CPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Các tham số sinh văn bản (Generation configs)
MAX_LENGTH = 128
NUM_BEAMS = 5
SRC_LANG = "en_XX"
TGT_LANG_CODE = "vi_VN"