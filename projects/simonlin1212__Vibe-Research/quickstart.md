## 安装
```bash
# 后端 (FastAPI :8900)
cd backend
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8900

# 前端 (Vite + React :5899)
cd frontend
npm install
npm run dev
# 打开 http://localhost:5899
```
## 最小可用示例
启动后，在「接入AI」页选择“订阅接入”并勾选已安装的CLI(如Claude Code)，即可在个股页或复盘页点击“问AI”获得分析。无需填写API key。
## 依赖前提
- Python 3.10+
- Node.js 18+
- (可选) 用于CLI接入的Claude Code/Codex等需提前安装并登录