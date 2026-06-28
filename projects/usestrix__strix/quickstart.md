### 安装
```bash
curl -sSL https://strix.ai/install | bash
```
### 配置环境变量
```bash
export STRIX_LLM="openai/gpt-5.4"   # 模型ID，如openai/gpt-5.4或anthropic/claude-sonnet-4-6
export LLM_API_KEY="your-api-key"
# 可选：本地模型base_url、Perplexity搜索键、推理强度等
```
### 第一次扫描
```bash
strix --target ./app-directory   # 本地代码或Git仓库URL或线上URL
```
首次运行自动拉取Docker沙盒镜像，结果保存在`strix_runs/<run-name>`。
### 前提
- Docker 已安装并运行
- 至少一个LLM提供商的API key（OpenAI/Anthropic/Google等）