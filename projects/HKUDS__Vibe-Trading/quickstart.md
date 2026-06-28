```bash
# 安装
pip install -U vibe-trading-ai

# 启动（默认使用本地数据缓存和示例配置）
vibe-trading run

# 或通过API服务器模式启动
vibe-trading serve --port 8000

# 访问Web UI
http://localhost:8000
```
更多配置：设置环境变量 `OPENAI_API_KEY` 或 `DEEPSEEK_API_KEY` 等启用LLM。查看 [文档](https://vibetrading.wiki/docs/) 获取详细指南。