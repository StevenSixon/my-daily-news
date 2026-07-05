## 安装与运行
```bash
git clone <repo>
cd T3MP3ST
npm install
npm run server   # 启动 War Room，访问 http://127.0.0.1:3333/ui/
```
在 War Room 的 Settings 中连接本地 AI 代理（Claude Code / Codex / Hermes），无需密钥。或者设置环境变量 `OPENROUTER_API_KEY` 等使用密钥。

验证声明：
```bash
npm run verify-claims
```

**依赖**：Node.js (TypeScript 项目)，需本机已安装并配置 AI 编码代理（如 Claude Code）以提供智能决策。