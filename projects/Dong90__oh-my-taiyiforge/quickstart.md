## 安装与快速开始
**前提**：Node.js ≥ 20，Git，AI 终端（Claude/Cursor/OpenCode/Codex 至少一种）。

```bash
# 1. 克隆仓库并构建
git clone https://github.com/Dong90/oh-my-taiyiforge.git
cd oh-my-taiyiforge
npm install && npm run build

# 2. 将 Skill 安装到你的 AI 终端（以全部安装为例）
node scripts/taiyi-forge.sh install --all

# 3. 在 AI 终端聊天中开始第一个 change
/taiyi:new "优化登录流程"
/taiyi:status
```
之后引擎会逐步提示下一步命令，你只需按阶段产出规定写 Markdown 和代码，审批点需人工确认。

也可单独安装到某个终端，如 `node scripts/taiyi-forge.sh install --cursor`。