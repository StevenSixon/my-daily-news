## 快速上手
### 前提
- Python 3.10~3.14
- 有效的 LLM API Key（默认 OpenAI，也可配置其他）

### 安装
```bash
uv pip install cognee
```

### 最小示例
```python
import os
os.environ["LLM_API_KEY"] = "your-openai-key"

import cognee
import asyncio

async def main():
    # 存储记忆
    await cognee.remember("Cognee turns documents into AI memory.")
    # 查询记忆
    results = await cognee.recall("What does Cognee do?")
    for r in results:
        print(r)
    # 删除数据集
    await cognee.forget(dataset="main_dataset")

asyncio.run(main())
```

### CLI 方式
```bash
cognee-cli remember "Some important info"
cognee-cli recall "info?"
cognee-cli -ui   # 启动 Web 界面（需 Docker）
```