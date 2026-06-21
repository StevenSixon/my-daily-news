**零成本部署（推荐方式）**

1. **Fork 仓库**：点击 GitHub 页面右上角 Fork 按钮，克隆到自己的仓库。
2. **配置 Secrets**：在仓库的 `Settings → Secrets and variables → Actions` 添加以下必要环境变量：
   - AI 模型（至少选一个，推荐 Anspire）：`ANSPIRE_API_KEYS` 或 `GEMINI_API_KEY` 等。
   - 通知渠道（至少选一个）：`WECHAT_WEBHOOK_URL`、`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` 等。
   - 自选股票列表（必填）：`STOCK_LIST`，例如 `600519,hk00700,AAPL,7203.T,005930.KS`。
   - 新闻搜索（推荐）：`ANSPIRE_API_KEYS` 可复用，或添加 `SERPAPI_API_KEYS`。
3. **启用 Actions**：进入 `Actions` 标签页，点击 `I understand my workflows, go ahead and enable them`。
4. **手动测试**：在 `Actions` 中选择 `每日股票分析` workflow，点击 `Run workflow` 触发一次运行。
5. 成功后，系统将在每个工作日北京时间 18:00 自动执行分析并推送至所选通知渠道。

**本地/Docker 运行**

```bash
# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis
# 安装依赖
pip install -r requirements.txt
# 配置环境变量
cp .env.example .env && vim .env   （填入 AI key、通知配置和股票列表）
# 执行一次分析
python main.py
# 启动 Web 界面
python main.py --webui
```

Docker 部署与更多命令请参阅 [完整指南](docs/full-guide.md)。

**前置要求**

- Python 3.10+（本地运行）
- 至少一个 LLM API key（Anspire、AIHubMix、Gemini 等）
- 一个通知渠道的 Webhook/Bot token
- 一份自选股票代码清单