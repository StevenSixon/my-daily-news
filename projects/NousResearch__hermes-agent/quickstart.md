### 安装
Linux/macOS/WSL2/Termux：
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
Windows PowerShell（原生）：
```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```
安装后重启 shell：
```bash
source ~/.bashrc  # 或 source ~/.zshrc
```

### 最小可用
```bash
hermes              # 进入交互式 CLI，开始对话
hermes model        # 选择您的模型（OpenAI、Nous Portal 等）
hermes gateway setup # 配置 Telegram、Discord 等平台
hermes gateway start # 启动网关，从聊天软件与代理对话
```
通过 `/new` 重置对话，`/compress` 管理上下文，`/skills` 浏览技能。

### 依赖前提
安装脚本自动处理所有依赖（uv、Python 3.11、Node.js、ripgrep、ffmpeg 等），无需手动准备。Windows 下会附带便携 Git Bash 用于执行 shell 命令。