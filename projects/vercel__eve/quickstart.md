### 安装
```bash
npx eve@latest init my-agent
```
或添加到现有项目：
```bash
cd myapp && npx eve@latest init .
```
前置要求：Node.js 环境。

### 最小示例
1. 编辑 `agent/instructions.md`：
```markdown
You are a concise weather demo assistant. Tell users that the weather data is mocked.
```
2. 添加工具 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "Return mock weather data for a city.",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "Sunny", temperatureF: 72 };
  },
});
```
3. 配置模型 `agent/agent.ts`：
```ts
import { defineAgent } from "eve";
export default defineAgent({ model: "anthropic/claude-sonnet-4.6" });
```
4. 启动：
```bash
npm run dev
```
终端 UI 等待交互，按提示操作即可。