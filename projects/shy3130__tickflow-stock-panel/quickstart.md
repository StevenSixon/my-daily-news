## 安装与最小可用示例

### 前置依赖
- Python >= 3.11
- Node >= 20
- Docker (最简单方式) 或 pnpm + uv

### Docker 部署 (推荐)
```bash
cp .env.example .env   # 留空 TickFlow Key 使用 Free 模式
docker compose up --build
# 访问 http://localhost:3018
```

### 桌面客户端
从 [GitHub Releases](https://github.com/shy3130/tickflow-stock-panel/releases/latest) 下载对应平台安装包，双击安装即可启动。

### 第一次使用
1. 打开面板，进入 设置 → 凭据与能力 → 重新检测
2. 点“立即跑盘后管道”拉取K线（Free模式仅10只示例股）
3. 自选页添加股票，查看K线
4. 选股页执行内置策略或自定义信号
5. 监控中心配置告警规则

### Dev 模式 (二次开发)
```bash
cp .env.example .env
./dev.sh   # macOS/Linux
.\dev.ps1 # Windows
```
后端启动在 :3018, 前端在 :3011