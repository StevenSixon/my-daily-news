```bash
# 确保 Node.js 环境（推荐 18+）及 pnpm
npx @agent-native/core@latest create my-app
cd my-app
pnpm install
pnpm dev
```
- 创建时可选择：完整模板、仅聊天UI、无头模式（先定义 actions）。
- 无头模式会引导你通过 CLI 调用第一个 action 和 Agent。
- 需提供兼容 Drizzle 的 SQL 数据库（如 Neon、PostgreSQL）并配置连接。
- 使用 `npx @agent-native/core@latest skills add visual-plan` 可快速为现有 Agent 添加视觉规划技能。