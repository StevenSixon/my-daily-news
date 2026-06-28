### 前置依赖
- Python≥3.11, Node≥20, uv, pnpm
- 克隆仓库：`git clone https://github.com/shy3130/tickflow-stock-panel`

### 快速启动
#### 开发模式
```bash
cp .env.example .env
./dev.sh        # 同时启动前后端
```
访问 http://localhost:3011 （前端）

#### Docker部署
```bash
cp .env.example .env
docker compose up --build
```
访问 http://localhost:3018

### 最小可用示例
1. 进入Web面板，设置页点击“立即跑盘后管道”加载历史日K。
2. 在选股页选择内置策略（如“均线多头”）点击扫描，查看结果。
3. 在回测页选择策略和日期区间运行回测，观察净值曲线。
无需填写任何API Key即可体验（None模式）。