## 安装与运行

**前提**：Node.js ≥22（推荐最新 LTS）

### 方式一：npm 全局安装
```bash
npm install -g omniroute
```
启动网关：
```bash
omniroute start
```
默认监听 `http://localhost:20128`。

### 方式二：直接使用 Docker
```bash
docker run -d --name omniroute -p 20128:20128 diegosouzapw/omniroute
```

### 配置 IDE/CLI 示例（以 Claude Code 和 Cline 为例）

**Claude Code** 中设置环境变量：
```bash
export ANTHROPIC_BASE_URL=http://localhost:20128/v1
export ANTHROPIC_API_KEY=any-value-you-want
```

**Cline（VS Code 扩展）**：
1. 打开设置，找到 `Cline: Api Provider`，选择 `OpenAI Compatible`。
2. `Base URL` 填入 `http://localhost:20128/v1`。
3. `API Key` 可任意填写。

其他工具（Cursor、Codex、Copilot 等）同理，只需将 API 基础地址指向本机网关即可。

**打开仪表板**：浏览器访问 `http://localhost:20128` 查看实时路由、压缩统计和免费额度消耗。