import os
import time
from pathlib import Path
from config import PDF_PATH, OUTPUT_IMAGE_DIR
from pdf_utils import pdf_to_images_pymupdf
from glm_client import analyze_image_with_glm

def main():
    if not os.getenv("ZHIPUAI_API_KEY") and not PDF_PATH:
        raise EnvironmentError("请确保设置了 ZHIPUAI_API_KEY 或 config 中有默认 key")
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"PDF 文件不存在: {PDF_PATH}")

    # 1. PDF 转图像
    image_paths = pdf_to_images_pymupdf(PDF_PATH)

    # 2. 逐页分析
    results = {}
    for img_path in image_paths:
        page_num = int(Path(img_path).stem.split('_')[-1])
        result = analyze_image_with_glm(img_path)
        results[page_num] = result
        time.sleep(0.3)  # 避免 API 限流

    # 3. 输出结果
    print("\n" + "=" * 60)
    print("📄 PDF 多模态解析结果汇总")
    print("=" * 60)
    for page in sorted(results.keys()):
        print(f"\n--- 第 {page} 页 ---")
        print(results[page])

    # 4. 保存到文件
    with open("pdf_glm_analysis.txt", "w", encoding="utf-8") as f:
        for page in sorted(results.keys()):
            f.write(f"--- 第 {page} 页 ---\n")
            f.write(results[page] + "\n\n")
    print("\n✅ 结果已保存至: pdf_glm_analysis.txt")


if __name__ == "__main__":
    main()