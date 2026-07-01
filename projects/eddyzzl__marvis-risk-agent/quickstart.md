### 安装与运行
```bash
git clone https://github.com/eddyzzl/marvis-risk-agent.git
cd marvis-risk-agent
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
marvis serve --host 127.0.0.1 --port 8000 --workspace ./workspace
```
打开 http://127.0.0.1:8000/。

### 最小可用示例
1. 按 docs/notebook_contract.md 准备一个符合规范的验证 Jupyter Notebook。
2. 将 Notebook 和相关数据放入 workspace 下的材料目录。
3. 在 Web UI 创建任务，选择该 Notebook，Agent 将执行并生成报告初稿。

### 依赖前提
- Python 3.11+ (推荐 3.12)
- macOS 或 Linux (当前验证环境)
- Java 运行时（仅当需用 pypmml 评分）
- Node.js（可选，仅用于前端语法检查）