```bash
# 初始化新项目
npx eve@latest init my-agent
cd my-agent
```
修改 `agent/instructions.md` 为自定义系统提示。

添加工具 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "返回模拟天气数据",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "Sunny", temperatureF: 72 };
  },
});
```
在 `agent/agent.ts` 中设置模型：
```ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-4.6",
});
```
启动开发：
```bash
npm run dev
```
依赖：Node.js 18+，对应模型的 API key（需通过环境变量提供，如 `ANTHROPIC_API_KEY`）。