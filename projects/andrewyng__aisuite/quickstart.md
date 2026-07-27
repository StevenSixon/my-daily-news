## 安装
```bash
pip install 'aisuite[all]'   # 安装所有供应商 SDK
```
或只装需要的：
```bash
pip install 'aisuite[openai,anthropic]'
```

## 最小示例
```python
import aisuite as ai
client = ai.Client()

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## 依赖前提
- Python 3.10+
- 对应供应商的 API Key（设为环境变量，如 `OPENAI_API_KEY`）
- 如需本地模型，安装 Ollama 并启动服务