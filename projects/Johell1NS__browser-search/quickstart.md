## 安装与上手

### 环境要求
- Node.js >= 18（可使用 npx）
- Docker（用于 SearXNG 和 Camofox）
- Git

### 快速安装技能定义
```bash
npx skills add Johell1NS/browser-search
```
该命令将 SKILL.md 安装到支持 Skills 规范的 AI 代理中（如 OpenCode）。

### 完整基础设施搭建
```bash
git clone https://github.com/Johell1NS/browser-search
cd browser-search
npm install
```
然后向 AI 代理展示本 README，让其根据你的平台完成 SearXNG、Camofox 服务的 Docker 启动与配置。主要服务：
- SearXNG：`docker run ... -p 8080:8080` 参见 searxng-docker
- Camofox：`docker run ... -p 9377:9377` 参见 jo-inc/camofox-browser
- CloakBrowser：已包含在 `scripts/cloak/cloak-fetch.mjs` 中，无需额外安装。

### 最小可用示例
假设服务已启动，向 AI 代理提问“搜索最近的大模型基准”时，代理会：
1. 用 SearXNG 搜索：`curl http://localhost:8080/search?format=json&q=...`
2. 用 Camofox 打开结果链接：`curl -X POST http://localhost:9377/tabs ...`
3. 若遇 Cloudflare，切换到 CloakBrowser：`node scripts/cloak/cloak-fetch.mjs <URL>`

### 验证安装
运行预检脚本：
```bash
bash scripts/check-browser-search.sh
```