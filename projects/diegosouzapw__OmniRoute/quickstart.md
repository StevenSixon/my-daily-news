## 安装
```bash
# Docker 方式
docker pull diegosouzapw/omniroute
docker run -d -p 20128:20128 diegosouzapw/omniroute

# npm 方式 (需要 Node.js)
npm install -g omniroute
omniroute start
```

## 使用
1. 启动后服务运行在 `http://localhost:20128`
2. 将你的编码工具（如 Claude Code, Cursor, Cline）的 API Base URL 设置为 `http://localhost:20128/v1`
3. 无需额外 API Key（免费供应商自动处理）

> 精确的 CLI 命令和配置细节请查阅 [getting-started](docs/getting-started) 文档。