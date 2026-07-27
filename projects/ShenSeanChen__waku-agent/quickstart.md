```bash
git clone https://github.com/ShenSeanChen/waku-agent && cd waku-agent
uv venv && uv pip install -e .     # 创建虚拟环境并安装 waku 命令
cp .env.example .env               # 选择一个 LLM 提供商，粘贴一个 API 密钥
uv run waku                        # 终端对话
uv run waku dashboard              # 启动本地仪表盘 -> http://localhost:7777
```
最小可用示例：在聊天中输入“Remember Alex prefers morning meetings.”，再输入“Book a catch-up with Alex on Friday.”，Waku 会记住偏好并合理安排时间。依赖前提：需安装 [uv](https://docs.astral.sh/uv/)；任意支持的 LLM 提供商 API 密钥。