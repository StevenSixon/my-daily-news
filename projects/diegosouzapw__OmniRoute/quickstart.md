**推测的快速上手指南**（未在原 README 截段中给出，以下基于 npm 和 Docker 包名推断）：

1. 使用 npm 一键启动：
   ```bash
   npx omniroute@latest
   ```
   或通过 Docker 运行：
   ```bash
   docker run -d -p 20128:20128 diegosouzapw/omniroute
   ```
2. 服务默认运行在 `http://localhost:20128`，将 AI 工具（如 Claude Code、Cursor）的 API 地址设为 `http://localhost:20128/v1`。
3. 无需 API 密钥即可免费使用 90+ 免费提供商池，高级功能可按需配置环境变量。

**注意**：具体命令需参阅官方文档或仓库 `docs/getting-started`。