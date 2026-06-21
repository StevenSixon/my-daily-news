## 准备
- Python 3.12+、Node.js 22+、Docker（推荐）
- 一个 LLM API key（如 OpenAI、DeepSeek）

## 安装运行
```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup   # 交互式配置向导，生成 config.yaml 和 .env
make docker-init   # 拉取沙箱镜像
export OPENAI_API_KEY=your-key  # 或写入 .env
make docker-start  # 开发模式启动
```
访问控制台，开始创建长程任务。更多配置见 `config.example.yaml`。