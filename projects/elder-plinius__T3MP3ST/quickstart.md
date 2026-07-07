### 前提
- Node.js >=18、npm
- 本机已安装一个 AI 编码代理（如 Claude Code、Codex、Hermes），或 Ollama 等本地模型，或可选的云 API 密钥（OpenRouter/Anthropic/OpenAI）

### 安装与启动
```bash
git clone https://github.com/elder-plinius/T3MP3ST
cd T3MP3ST
npm install
npm run server          # War Room → http://127.0.0.1:3333/ui/
```

在 War Room 的 Settings 中连接已登录的本地代理，或设置环境变量（如 `export OPENROUTER_API_KEY=...`）。

### 完全离线示例
```bash
ollama serve && ollama pull llama3
export TEMPEST_LOCAL_BASE_URL=http://localhost:11434/api
export TEMPEST_LOCAL_MODEL=llama3
npx tempest config        # 选择 local 作为默认 provider
```

然后在 War Room 中向 Op Admiral 描述授权目标，启动自主攻击。

### 验证所有基准声明
```bash
npm run verify-claims
```
该命令会从 `bench/` 目录中的提交数据重新计算代码中出现的每个数字，确保一切可重现。