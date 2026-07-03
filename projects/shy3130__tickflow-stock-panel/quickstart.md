## 环境准备

- Python ≥ 3.11
- Node.js ≥ 20
- [uv](https://docs.astral.sh/uv/) 包管理器
- pnpm (`npm i -g pnpm`)

## 最小部署

### 方式一：Docker（推荐）

```bash
git clone https://github.com/shy3130/tickflow-stock-panel.git
cd tickflow-stock-panel
cp .env.example .env
# 编辑.env，可选择填写TICKFLOW_API_KEY（留空为None免费模式）
docker compose up --build
```

访问 `http://localhost:3018`

### 方式二：开发模式

```bash
cp .env.example .env
./dev.sh           # Windows: .\dev.ps1
```

自动启动后端（3018端口）和前端（3011端口）。

## 初始化使用

1. 打开面板，进入“设置→凭据与能力”，点击“重新检测”确认数据档位
2. “设置→立即跑盘后管道”拉取日K并计算指标（当日数据盘后1-2小时可用）
3. 在“自选”页添加股票，进入“选股”运行策略
4. 在“回测”页选择策略+区间查看绩效
5. 配置“监控中心”实现盘中实时提醒