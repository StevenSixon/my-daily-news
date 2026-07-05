### 安装
```bash
# 使用 npm 全局安装
npm install -g omniroute

# 或直接用 npx 免安装运行
npx omniroute
```
### 启动并获取端点
```bash
# 启动网关（默认端口 20128）
omniroute start
```
打开浏览器访问 `http://localhost:20128` 进入仪表盘，无需配置即可使用 90+ 免费提供商。端点地址为 `http://localhost:20128/v1`。

### 配置编码工具
以 Cursor 为例，在设置中将 API Base URL 改为 `http://localhost:20128/v1`，API Key 留空或填任意值，即可开始使用。支持 Claude Code、Cline、Codex、Copilot 等 24+ 工具，具体配置见文档。

### 前提
- Node.js >= 18
- （可选）自有 API 密钥可添加到仪表盘以提升可用性，但不是必需。