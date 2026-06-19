## 安装
### 方式一：本地 pip/uv 安装
```bash
# 1. 克隆仓库
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# 2. 创建并激活虚拟环境
uv venv .venv && source .venv/bin/activate
# 或：python3 -m venv .venv && source .venv/bin/activate

# 3. 安装（生产模式）
make install
```

### 方式二：Docker（无需本地 Python）
```bash
make docker-build
# 或 docker build -t skillspector .
```

## 最小可用示例
1. **静态扫描（无 LLM）**
```bash
# 扫描本地技能目录
skillspector scan ./my-skill/ --no-llm

# 扫描单一 SKILL.md
skillspector scan ./SKILL.md

# 扫描 Git 仓库
skillspector scan https://github.com/user/my-skill
```

2. **使用 LLM 深度分析**
```bash
# OpenAI
export SKILLSPECTOR_PROVIDER=openai
export OPENAI_API_KEY=sk-...
skillspector scan ./my-skill/

# 本地 Ollama
export SKILLSPECTOR_PROVIDER=openai
export OPENAI_API_KEY=ollama
export OPENAI_BASE_URL=http://localhost:11434/v1
export SKILLSPECTOR_MODEL=llama3.1:8b
skillspector scan ./my-skill/
```

3. **输出 JSON 报告**
```bash
skillspector scan ./my-skill/ --format json --output report.json
```

## 依赖前提
- Python 3.12+（本地安装时）或 Docker 环境
- 若启用 LLM 分析，需对应提供商的 API key（OpenAI、Anthropic、NVIDIA）或本地兼容端点（Ollama/vLLM）
- 扫描 Git 仓库或 URL 时需网络连接