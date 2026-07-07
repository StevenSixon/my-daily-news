## 安装
1. 将技能注入你的 AI 代理（支持 OpenCode/Claude Code/Claude 等 70+ 种代理）：
   ```bash
   npx skills add Johell1NS/browser-search
   ```
2. 克隆仓库并安装 Node 依赖（CloakBrowser 内置于此）：
   ```bash
   git clone https://github.com/Johell1NS/browser-search
   cd browser-search
   npm install
   ```
3. 启动 SearXNG 和 Camofox 的 Docker 容器，具体配置可向你的 AI 代理提问——“帮我按 docs.searxng.org 和 camofox-browser README 在本机部署”。确保 SearXNG 监听 `:8080`，Camofox 监听 `:9377`。
4. 验证：
   - 搜索测试：`curl -s "http://localhost:8080/search?format=json&q=test"`
   - 浏览测试：CloakBrowser 提取示例：`node scripts/cloak/cloak-fetch.mjs "https://example.com"`

## 依赖前提
- Node.js ≥ 18
- Docker 引擎（用于 SearXNG 和 Camofox）
- npm（随 Node 附带）
- 防火墙/网络允许本地 8080、9377 端口