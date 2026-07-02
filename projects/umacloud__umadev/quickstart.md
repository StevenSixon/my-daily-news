```bash
# 1. 确保已安装一个 AI 编码 CLI 并登录，例如
npm i -g @anthropic-ai/claude-code
claude auth login

# 2. 安装 umadev
npm install -g umadev

# 3. 启动交互式 chat UI（首次运行会提示选择 base）
umadev

# 4. 在提示符下输入需求，例如
# > add CSV export to the reports page

# 或者直接无交互式运行
umadev run "add CSV export to the reports page" --backend claude-code
```

**依赖前提**：
- Node.js 环境（用于 npm 安装）
- 至少一个受支持的 AI 编码 CLI（Claude Code / Codex / OpenCode）并已登录
- 如需本地向量检索，确保网络可下载 ~224 MB 的嵌入模型（会自动处理），或手动下载至 `~/.umadev/embed-model/`
- 从源码构建需 Rust 1.87+ 并手动下载模型