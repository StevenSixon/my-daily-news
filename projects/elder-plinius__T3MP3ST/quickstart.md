## 安装与启动
```bash
# 克隆仓库并安装
npm install

# 启动 War Room UI
npm run server    # 浏览器打开 http://127.0.0.1:3333/ui/
```

## 连接 AI 代理（零密钥）
在 War Room 设置中连接本地已有代理（如 Claude Code、Codex），输入自然语言目标即可启动任务。

## 使用 API 密钥（可选）
```bash
export OPENROUTER_API_KEY=sk-...
# 或其它支持的密钥：ANTHROPIC_API_KEY, OPENAI_API_KEY, VENICE_API_KEY, XAI_API_KEY
```

## 完全离线运行
```bash
ollama serve && ollama pull llama3
export TEMPEST_LOCAL_BASE_URL=http://localhost:11434/api
export TEMPEST_LOCAL_MODEL=llama3
npx tempest config   # 选择 local 提供商
```

## 验证所有基准数字
```bash
npm run verify-claims   # 自动重新计算 README 里的每一个指标
```

**依赖前提**：Node.js 16+，npm，浏览器 UI 模式无需额外依赖。离线模式需本地运行兼容 OpenAI API 的模型服务（Ollama/LM Studio/vLLM）。