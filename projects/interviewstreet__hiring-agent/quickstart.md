**前提**
- Python 3.11+
- Ollama（如需本地模型）或 Gemini API Key
- （可选）GitHub Token 以提高 API 频率限制

**安装步骤**
```bash
git clone https://github.com/interviewstreet/hiring-agent
cd hiring-agent
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

**配置 LLM 后端**
编辑 `.env`：
```bash
# 使用本地 Ollama
LLM_PROVIDER=ollama
DEFAULT_MODEL=gemma3:4b

# 或使用 Gemini
# LLM_PROVIDER=gemini
# DEFAULT_MODEL=gemini-2.0-flash
# GEMINI_API_KEY=你的密钥
```

**拉取 Ollama 模型（如果使用本地）**
```bash
ollama pull gemma3:4b
```

**最小示例**
```bash
python score.py /path/to/resume.pdf
```
输出为终端报告；若 `config.py` 中 `DEVELOPMENT_MODE=True`，还会生成缓存 JSON 和 `resume_evaluations.csv`。