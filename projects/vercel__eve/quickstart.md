```bash
npx eve@latest init my-agent
cd my-agent
```

用你喜欢的编辑器修改 `agent/instructions.md` 来定义系统角色。

添加工具：在 `agent/tools/` 下创建 TypeScript 文件，使用 `defineTool` 和 Zod schema。

配置模型：编辑 `agent/agent.ts`，设置 `model` 字段（如 `"anthropic/claude-sonnet-4.6"`）。

启动开发：

```bash
npm run dev
```

更多功能参考 [官方文档](https://eve.dev/docs)。