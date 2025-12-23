# 📄 PDF 多模态智能解析工具

> 本项目可将任意 PDF 文档（包括扫描件、图文混合页）自动转换为图像，并通过 **智谱 AI 的 GLM-4V-Flash 多模态大模型** 进行内容理解与结构化描述，适用于合同分析、报告摘要、教育资料处理等场景。

---

## ✨ 核心功能

- ✅ 使用 **PyMuPDF (fitz)** 高效渲染 PDF 为高清 PNG 图像  
- ✅ 通过 **Base64 内嵌图像** 调用 **GLM-4V-Flash**，无需公网 URL  
- ✅ 完全本地运行，**不依赖 Poppler / ImageMagick**  
- ✅ 自动分页解析并生成结构化文本结果  
- ✅ 模块化设计，易于扩展与集成

---

## 📁 项目结构

```bash
llm_pdf/
├── config.py                 # 全局配置（路径、DPI、API Key 等）
├── pdf_utils.py              # PDF → 图像转换逻辑
├── glm_client.py             # GLM-4V-Flash API 调用封装
├── main.py                   # 主程序入口
├── test.pdf                  # 示例 PDF（替换为你自己的文件）
├── pdf_images/               # 自动生成的图像缓存目录
└── pdf_glm_analysis.txt      # 输出的解析结果文件
```

## ⚙️ 快速开始

### 1. 安装依赖

```python
pip install pymupdf zhipuai
```

💡 pymupdf 是 PyMuPDF 的 PyPI 包名，导入时使用 import fitz

### 2. 准备 PDF 文件

将你的 PDF 文件命名为 test.pdf 并放在项目根目录，或修改 config.py 中的 PDF_PATH。

### 3. 配置 API Key（二选一）

方式 A：硬编码（仅用于测试）
已在 config.py 中预置示例 Key（请勿用于生产）：

```python
API_KEY = os.getenv("ZHIPUAI_API_KEY", "your-default-key-here")
```

方式 B：环境变量（推荐）

```bash
# Linux / macOS
export ZHIPUAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

# Windows (PowerShell)
$env:ZHIPUAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

### 4. 运行程序

```bash
python main.py
```

### 5. 查看结果

控制台实时输出每页分析内容
最终结果保存至：pdf_glm_analysis.txt

### 🛠️ 自定义配置（`config.py`）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `PDF_PATH` | `"test.pdf"` | 待解析的 PDF 文件路径 |
| `OUTPUT_IMAGE_DIR` | `"pdf_images"` | 图像缓存目录 |
| `DPI` | `200` | 渲染分辨率（150~300 推荐） |
| `GLM_MODEL` | `"glm-4v-flash"` | 使用的多模态模型 |
| `API_KEY` | 从环境变量读取 | 智谱 AI API Key |

---

## 📦 依赖说明

| 包 | 用途 |
|----|------|
| `pymupdf` | PDF 渲染为图像（轻量、跨平台） |
| `zhipuai` | 调用智谱 AI 大模型 API |
| `base64` | 内置模块，用于图像编码 |

---

## 📜 许可证

MIT License — 免费用于个人及商业项目。

---

## 🙌 致谢

- [PyMuPDF 官网](https://pymupdf.readthedocs.io/)
- [智谱 AI 开放平台](https https://open.bigmodel.cn/)
- GLM-4V-Flash：高效、低成本的多模态推理模型

---

## 💖 关于作者
如果你觉得它对你有帮助：

✅ 点个 Star 是最大的鼓励！
💬 欢迎提 Issue 或 PR，一起让它变得更好
📧 联系邮箱：shaoycamore@gmail.com
（可用于合作或反馈建议）
