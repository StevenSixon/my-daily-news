## 安装
```bash
# macOS / Linux
curl -fsSL https://herdr.dev/install.sh | sh

# 或 Homebrew
brew install herdr

# 或 mise
mise use -g herdr

# Windows (beta)
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

## 最小可用示例
```bash
# 启动 herdr
herdr

# 在 herdr 内启动你的AI Agent，例如 Claude Code
claude

# 拆分窗格，运行另一个Agent
# 快捷键：Ctrl+B % (垂直分割), Ctrl+B " (水平分割), 或用鼠标拖拽
# 然后在新窗格里启动另一个Agent

# 分离会话（Agent继续后台运行）
Ctrl+B q

# 重新连接
herdr
```

**前提依赖**：需要支持UTF-8的现代终端（如 iTerm2、Windows Terminal、Alacritty 等），无额外运行时依赖（单Rust二进制）。