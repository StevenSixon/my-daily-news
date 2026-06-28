## 方式一：GitHub Actions（推荐）
1. Fork 本仓库，并给 Star。
2. 在仓库 Settings → Secrets 中配置：
   - AI 模型：推荐 `ANSPIRE_API_KEYS` 或 `AIHUBMIX_KEY`
   - 通知渠道：如 `WECHAT_WEBHOOK_URL`
   - 自选股：`STOCK_LIST`（如 `600519,hk00700,AAPL`）
   - 新闻源：可选 `ANSPIRE_API_KEYS`、`SERPAPI_API_KEYS` 等
3. 启用 Actions，手动触发 `每日股票分析` 测试。
4. 默认工作日 18:00（北京时间）自动执行。

## 方式二：本地 / Docker 运行
```bash
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git
cd daily_stock_analysis
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 填入 API 密钥和股票列表
python main.py
```
Docker 部署：
```bash
docker compose up -d
```

## 最小示例
```bash
# 分析指定股票，输出报告
python main.py --stocks 600519,AAPL
# 启动 Web 界面
python main.py --webui
```

前提：Python 3.10+，已配置至少一个 LLM API Key。