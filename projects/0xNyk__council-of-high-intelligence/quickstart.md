## 安装
```bash
git clone https://github.com/0xNyk/council-of-high-intelligence.git
cd council-of-high-intelligence
# 为 Claude Code 安装
./install.sh
# 或为 Codex 安装
./install.sh --codex
```

## 最小可用示例
在 Claude Code 或 Codex 会话中直接调用：
```
/council Should we open-source our agent framework?
/council --quick Should we add caching here?
/council --duo Should we use microservices or monolith?
/council --triad strategy What's our competitive moat?
```

## 依赖前提
- 至少安装一个 LLM 提供商 CLI（Claude、Codex、Gemini、Ollama、Cursor 或 NVIDIA NIM 环境变量）
- 对于 NVIDIA NIM，需导出 `NVIDIA_API_KEY`；对于 Cursor，需安装 `cursor-agent` 并配置 API key
- Shell 环境（Bash/Zsh）