```bash
# 前提：Node.js 18+ 及 npm
npx eve@latest init my-agent
cd my-agent
# 编辑 agent/instructions.md 设定行为
# 在 agent/tools/ 下添加工具，如 get_weather.ts
# 选择模型：修改 agent/agent.ts 中的 model 字段
npm run dev
```

最小示例工具：
```ts
// agent/tools/get_weather.ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "Return weather data",
  inputSchema: z.object({ city: z.string() }),
  async execute({ city }) {
    return { city, condition: "Sunny", temperatureF: 72 };
  },
});
```

然后运行 `npm run dev` 即可在终端中交互。