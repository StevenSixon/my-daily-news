### 1. 环境准备
确保本地安装 **Node >=22** 和 **Bun**：
```bash
node --version
bun --version
# 若无 Bun: winget install Oven-sh.Bun 或访问 https://bun.sh
```

### 2. 构建并全局安装
```bash
git clone https://github.com/0xwilliamortiz/openclaude-improved.git
cd openclaude-improved
bun install
bun run build
npm install -g .
```

### 3. 最小可用示例（OpenAI 后端）
```bash
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="gpt-4o"
openclaude
```
或使用 Ollama 本地模型：
```bash
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_MODEL="qwen2.5-coder:7b"
openclaude
```
首次启动后也可用 `/provider` 命令进行交互式配置。