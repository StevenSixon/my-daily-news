### 前置依赖
- Node.js ≥20
- 注册 Duel Agents 并获取 API Key（格式 `duel_xxx_xxx`）

### 安装 CLI 工具
```bash
export DUEL_API_KEY=duel_yourprefix_yoursecret
npx @duel-agents/install all      # 一次性配置所有支持的 IDE
npx @duel-agents/install doctor   # 检查连接和密钥状态
```

### 在代码中调用
```bash
npm install @duel-agents/sdk
```
```ts
import { DuelClient } from "@duel-agents/sdk";

const duel = new DuelClient({
  apiKey: process.env.DUEL_API_KEY!
});

// OpenAI 兼容风格
const chat = await duel.chat.completions.create({
  model: "duel-auto",
  messages: [{ role: "user", content: "Hello" }],
});

// Anthropic 兼容风格
const msg = await duel.messages.create({
  model: "duel-auto",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }],
});
```
> **注意**：截至 README 撰写，npm 包未实际发布，可能需要克隆仓库并执行 `npm run build` 才能使用。