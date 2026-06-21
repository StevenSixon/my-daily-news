## 安装
```bash
pip install cognee
```
或 `uv pip install cognee`。
要求 Python 3.10～3.14。

## 配置
设置 OpenAI API Key（或其它 LLM）：
```python
import os
os.environ["LLM_API_KEY"] = "your-openai-api-key"
```
也可使用 `.env` 文件，参考 [模板](https://github.com/topoteretes/cognee/blob/main/.env.template)。

## 最小示例
```python
import cognee
import asyncio

async def main():
    # 存储到永久知识图谱
    await cognee.remember("Cognee 将文档转化为 AI 记忆。")

    # 存储到会话级记忆
    await cognee.remember("用户偏好详细解释。", session_id="chat_1")

    # 查询记忆（自动选择最佳搜索策略）
    results = await cognee.recall("Cognee 能做什么？")
    for r in results:
        print(r)

    # 查询会话记忆
    results = await cognee.recall("用户偏好什么？", session_id="chat_1")
    for r in results:
        print(r)

    # 删除数据集
    await cognee.forget(dataset="main_dataset")

if __name__ == "__main__":
    asyncio.run(main())
```

## CLI 快速体验
```bash
cognee-cli remember "Cognee 将文档转化为 AI 记忆。"
cognee-cli recall "Cognee 能做什么？"
cognee-cli forget --all
```
启动本地 UI（需 Docker）：
```bash
cognee-cli -ui
```