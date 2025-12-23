import base64
from zhipuai import ZhipuAI
from config import API_KEY, GLM_MODEL

# 初始化客户端
client = ZhipuAI(api_key=API_KEY)

def analyze_image_with_glm(image_path, prompt="请详细描述该页面的内容，包括文字、表格、图表等信息。"):
    """使用 Base64 方式调用 GLM-4V-Flash"""
    print(f"🧠 正在分析: {image_path}")
    try:
        with open(image_path, "rb") as image_file:
            encoded_str = base64.b64encode(image_file.read()).decode("utf-8")

        response = client.chat.completions.create(
            model=GLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded_str}"}},
                        {"type": "text", "text": prompt}
                    ]
                }
            ],
            temperature=0.3,
            max_tokens=1024
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = f"❌ 分析失败 ({image_path}): {str(e)}"
        print(error_msg)
        return error_msg