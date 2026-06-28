## 安装与快速体验
### 前提
- Python 3.10～3.14
- LLM API Key（例如 OpenAI）

### 安装
```bash
uv pip install cognee
```

### 配置
```python
import os
os.environ["LLM_API_KEY"] = "YOUR_OPENAI_API_KEY"
```

### 最小运行示例
```python
import cognee
import asyncio

async def main():
    # 永久存储知识图谱
    await cognee.remember("Cognee turns documents into AI memory.")

    # 带会话 ID 的临时记忆
    await cognee.remember("User prefers detailed explanations.", session_id="chat_1")

    # 跨会话回忆
    results = await cognee.recall("What does Cognee do?")
    for r in results:
        print(r)

    # 删除数据集
    await cognee.forget(dataset="main_dataset")

asyncio.run(main())
```

### Docker 快速启动
```bash
cp .env.template .env   # 编辑设置 LLM_API_KEY
docker compose up        # 默认启动 API + 必要服务
```
或直接拉取镜像：
```bash
echo 'LLM_API_KEY="YOUR_KEY"' > .env
docker run --env-file ./.env -p 8000:8000 --rm -it cognee/cognee:main
```

### CLI 体验
```bash
cognee-cli remember "Cognee turns documents into AI memory."
cognee-cli recall "What does Cognee do?"
cognee-cli forget --all
# 启动本地 UI
cognee-cli -ui
```