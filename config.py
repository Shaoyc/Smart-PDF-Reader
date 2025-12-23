import os
from pathlib import Path

# === 全局配置 ===
PDF_PATH = "test.pdf"
OUTPUT_IMAGE_DIR = "pdf_images"
DPI = 200
GLM_MODEL = "glm-4v-flash"
API_KEY = os.getenv("ZHIPUAI_API_KEY", "your-default-key-here")
# 创建输出目录
Path(OUTPUT_IMAGE_DIR).mkdir(exist_ok=True)