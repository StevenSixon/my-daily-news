## 环境依赖
- Python 3.11+ (推荐 3.11.13)
- Ollama (如需本地运行) 或 Google Gemini API Key
- 可选：GitHub Token (提高API调用限额)

## 安装
```bash
git clone https://github.com/interviewstreet/hiring-agent
cd hiring-agent
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## 配置
```bash
cp .env.example .env
# 编辑 .env:
#   LLM_PROVIDER=ollama (或 gemini)
#   DEFAULT_MODEL=gemma3:4b (或 gemini-2.0-flash)
#   若用Gemini需填入 GEMINI_API_KEY
```
若本地已有 Ollama 服务，需先拉取模型：
```bash
ollama pull gemma3:4b
```

## 最小可用示例
```bash
python score.py /path/to/resume.pdf
```
执行后会：
1. 解析PDF为Markdown并缓存 (cache/)
2. 如果简历含GitHub链接，抓取项目信息
3. 在终端打印包含分项评分、证据、总分的评估报告
4. 当 config.py 中 DEVELOPMENT_MODE=True 时，将结果追加到 resume_evaluations.csv