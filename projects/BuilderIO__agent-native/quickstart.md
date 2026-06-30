```bash
# 创建新项目
npx @agent-native/core@latest create my-app
cd my-app
pnpm install
pnpm dev
```
创建时可选择：完整模板（如邮件+日历）、仅聊天UI、无头模式（先Action后加UI）。

**前提**：Node.js >= 18，pnpm，数据库（默认使用内置Drizzle适配，正式使用需提供数据库连接）。

**最小示例**——定义一个Action：
```ts
export default defineAction({
  schema: z.object({
    emailId: z.string(),
    body: z.string(),
  }),
  run: async ({ emailId, body }) => {
    await db.insert(replies).values({ emailId, body });
  },
});
```
该Action自动可用于UI按钮触发、Agent工具调用和API端点。更多见https://agent-native.com 。