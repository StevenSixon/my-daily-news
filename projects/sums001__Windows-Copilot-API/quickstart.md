**前提**：Python 3.9+，微软账号。

```bash
# 1. 克隆并进入目录
git clone <repo-url> && cd Windows-Copilot-API

# 2. 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt
playwright install chromium

# 4. 登录微软账号（会打开浏览器）
python -m copilot login

# 5. Python 快速示例
from copilot import CopilotClient
client = CopilotClient()
reply = client.chat("你好，请用一句话自我介绍")
print(reply.text)

# 6. 启动 OpenAI 兼容服务器（另一终端）
python app.py
# 然后使用 openai SDK：
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")
resp = client.chat.completions.create(
    model="copilot",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(resp.choices[0].message.content)
```