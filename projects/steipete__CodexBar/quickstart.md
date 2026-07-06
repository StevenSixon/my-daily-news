## 安装
```bash
# 通过 Homebrew 快速安装（推荐）
brew install --cask codexbar

# 或下载 GitHub Releases 中的 dmg：https://github.com/steipete/CodexBar/releases
```

- 要求：macOS 14+（Sonoma）
- **首次运行**后，点击菜单栏图标 → Settings → Providers，启用你使用的 AI 服务。
- 根据提供商不同，系统会提示授权或自动读取已有本地会话（CLI 登录、浏览器 Cookie 等）。
  - 示例：若已登录 Claude Desktop，可以直接读取 token；否则可手动粘贴 OAuth 凭证。
  - 若使用 Safari Cookies，需授予 Full Disk Access。
- 授权完成后，菜单栏即显示用量条和重置时间。

## 最小可用示例（CLI 成本）
```bash
# 查看 Codex 本地日志的成本估算
codexbar cost --provider codex

# 设置 API Key（不打开设置面板）
printf '%s' "$ELEVENLABS_API_KEY" | codexbar config set-api-key --provider elevenlabs --stdin
```

依赖前提：
- macOS 14+（GUI）；Linux 仅支持 CLI。
- 目标提供商的用户会话：至少一种已登录的方式（如 GitHub Copilot 需设备流授权，Cursor 需浏览器登录等）。