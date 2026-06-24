## 安装与依赖
- Python 3.9+
- Microsoft或Google账号
- 浏览器（Playwright将自动安装Chromium）

```bash
# 克隆项目（仓库URL按实际填写）
git clone <repo-url>
cd Windows-Copilot-API

# 创建虚拟环境
python3 -m venv venv && source venv/bin/activate   # macOS/Linux
python -m venv venv && venv\Scripts\activate      # Windows

# 安装依赖
pip install -r requirements.txt
playwright install chromium

# 登录（弹出浏览器，用Microsoft或Google账号登录）
python -m copilot login
```

## 最小可用示例
### Python库方式
```python
from copilot import CopilotClient

client = CopilotClient()
reply = client.chat("用一句话打招呼")
print(reply.text)
```

### OpenAI服务器方式
```bash
python app.py
# 服务运行在 http://localhost:8000
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")
resp = client.chat.completions.create(model="copilot", messages=[{"role":"user","content":"Hello!"}])
print(resp.choices[0].message.content)
```

或使用curl：
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello!"}]}'
```