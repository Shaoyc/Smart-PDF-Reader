import fitz  # PyMuPDF
import os
from pathlib import Path
from config import OUTPUT_IMAGE_DIR, DPI

def pdf_to_images_pymupdf(pdf_path, output_dir=OUTPUT_IMAGE_DIR, dpi=DPI):
    """使用 PyMuPDF 将 PDF 每一页转为 PNG 图像"""
    print(f"📄 正在将 {pdf_path} 转换为图像（DPI={dpi}）...")
    doc = fitz.open(pdf_path)
    image_paths = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        image_path = os.path.join(output_dir, f"page_{page_num + 1:03d}.png")
        pix.save(image_path)
        image_paths.append(image_path)
        print(f"  ✅ 已保存: {image_path}")

    doc.close()
    return image_paths