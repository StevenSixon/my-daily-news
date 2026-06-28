## 前提

- Node.js 18+
- 推荐使用 pnpm
- 一个支持 Drizzle 的 SQL 数据库（项目会引导配置）

## 脚手架创建

```bash
npx @agent-native/core@latest create my-app
cd my-app
pnpm install
pnpm dev
```

创建时可通过交互选择模式：
- **Full template(s)**：克隆一个或多个完整应用（如 Mail + Calendar）。
- **Chat**：带轻量聊天 UI 和浏览器壳的单应用。
- **Headless**：无 UI，通过 CLI 和 API 交互。

也可直接指定：
```bash
npx @agent-native/core@latest create my-app --template mail
```

## 最小动作示例

```ts
import { defineAction } from '@agent-native/core';
import { z } from 'zod';

export default defineAction({
  schema: z.object({
    emailId: z.string(),
    body: z.string(),
  }),
  run: async ({ emailId, body }) => {
    // 在此编写业务逻辑，例如操作数据库
    console.log(`回复邮件 ${emailId}：${body}`);
  },
});
```

该动作自动可用作 UI 按钮点击、Agent 工具调用、HTTP 端点等。

## 为已有 Agent 添加可视化规划技能

在任意 Node 项目中运行：
```bash
npx @agent-native/core@latest skills add visual-plan
```

之后在 Claude Code、Cursor、GitHub Copilot 等环境中可使用 `/visual-plan` 和 `/visual-recap` 命令。