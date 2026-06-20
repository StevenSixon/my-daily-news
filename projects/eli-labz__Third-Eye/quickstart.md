## 安装与运行

**前提**：Node.js 18+、npm（或 Docker 可选）

1. 克隆仓库：
   ```bash
   git clone https://github.com/eli-labz/Third-Eye.git
   cd Third-Eye
   ```

2. 安装依赖并启动开发服务器：
   ```bash
   npm install
   npm run dev
   ```
   打开 http://localhost:3000 即可使用，无需 API 密钥。

**Docker 快速部署**：
```bash
cp .env.template .env
docker compose up -d
```

或使用预构建镜像：
```bash
docker run -d -p 3000:3000 --env-file .env ghcr.io/aiacos/third-eye:latest
```

**最小可用示例**：启动后默认显示全球地图，可点击侧边栏切换图层，如开启“Flights”查看实时航空数据，或点击新闻点观看直播。所有核心图层无需额外配置。

**可选配置**：若需高性能 API 调用或启用 RECON 扫描器，在 `.env` 中设置 `OPENSKY_CLIENT_ID`、`FIRMS_API_KEY` 等变量（详见 `.env.template`）。