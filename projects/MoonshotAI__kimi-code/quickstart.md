## 安装
**macOS/Linux**
```bash
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```
**Windows**
```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```
> 前提：Windows 需安装 Git Bash，若非默认路径则设置 `KIMI_SHELL_PATH` 环境变量。

## 启动
```bash
cd your-project
kimi
```
首次运行输入 `/login`，选择 OAuth 或 API Key 登录。之后即可输入任务，例如：
```
Analyze the project structure and suggest improvements.
```

## 编辑器集成
登录后，在 Zed 的 `~/.config/zed/settings.json` 中添加：
```json
"agent_servers": {
  "Kimi Code CLI": {
    "type": "custom",
    "command": "kimi",
    "args": ["acp"],
    "env": {}
  }
}
```

## 开发环境
```bash
git clone https://github.com/MoonshotAI/kimi-code.git
cd kimi-code
pnpm install
pnpm dev:cli   # 开发模式运行
```
要求 Node.js ≥24.15.0、pnpm 10.33.0。