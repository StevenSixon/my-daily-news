1. Fork仓库并启用Actions。
2. 设置Secrets：至少一个LLM API Key（推荐ANSPIRE_API_KEYS）、通知Webhook（如企业微信）、自选股列表（STOCK_LIST）。
3. 手动触发“每日股票分析”工作流测试。
4. 默认工作日18:00自动运行，也可通过GitHub Actions手动执行或本地 `python main.py` 启动。