**安装**
```bash
npx eve@latest init my-agent
```
或添加到现有项目：`cd myapp && npx eve@latest init .`

**修改指令**
编辑 `agent/instructions.md`：
```markdown
You are a helpful assistant.
```

**添加工具**
创建 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "Return mock weather data.",
  inputSchema: z.object({ city: z.string() }),
  async execute({ city }) {
    return { city, condition: "Sunny", temperatureF: 72 };
  },
});
```

**配置模型**
编辑 `agent/agent.ts`：
```ts
import { defineAgent } from "eve";
export default defineAgent({ model: "anthropic/claude-sonnet-5" });
```

**运行**
```bash
npm run dev
```

**依赖前提**
- Node.js (≥18)
- 对应模型 API 密钥（需在环境变量中配置）