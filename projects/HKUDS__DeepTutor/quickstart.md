```bash
# 安装
pip install deeptutor
# 启动本地服务
deeptutor start
# 添加模型提供商（例如OpenAI）
export OPENAI_API_KEY=sk-...
# 或交互登录
deeptutor provider login openai-codex
```
配置完成后浏览器访问本地Web界面，即可创建知识库、设置导师伙伴并开始对话。支持Docker部署，详见官方文档。