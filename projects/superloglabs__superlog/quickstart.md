## 安装与最小示例

**前提条件**
- Node.js 20+
- pnpm 9+
- Docker

**本地启动**
```bash
pnpm install
docker compose up -d
pnpm --filter @superlog/db db:migrate
pnpm dev
```
启动后访问：
- Web UI：`http://localhost:5173`
- API：`http://localhost:4100`
- OTLP 接入：`http://localhost:4101`

**通过 AI 编程代理安装（推荐）**
在项目根目录执行：
```
npx skills add superloglabs/skills --all
```
然后按照代理提示完成配置。