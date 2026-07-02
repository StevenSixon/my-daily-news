## 安装
**一键安装（推荐）**
- macOS / Linux：
  ```bash
  curl -fsSL https://agents.craft.do/install-app.sh | bash
  ```
- Windows（PowerShell）：
  ```powershell
  irm https://agents.craft.do/install-app.ps1 | iex
  ```
**从源码构建**
```bash
git clone https://github.com/lukilabs/craft-agents-oss.git
cd craft-agents-oss
bun install
bun run electron:start
```

## 最小可用示例
1. 启动桌面应用。
2. 选择一个 LLM 连接：输入 Anthropic API 密钥，或通过 OAuth 连接 ChatGPT Plus / GitHub Copilot。
3. 创建第一个工作区（Workspace），例如 `我的日常`。
4. 在对话框中输入：`add Linear as a source`，代理将自动查找并配置 Linear MCP 服务器。
5. 开始对话：`列出我本周待办任务`，代理会调用已连接的 Linear 工具并返回结果。

## 依赖前提
- **运行桌面应用**：macOS、Linux 或 Windows，无需额外依赖（安装脚本自动处理）。
- **编译源码**：需安装 [Bun](https://bun.sh)（≥ 1.x）。
- **远程服务器**：Docker（推荐）或 Node.js ≥ 18。