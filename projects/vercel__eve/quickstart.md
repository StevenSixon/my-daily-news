**安装与初始化**
```bash
npx eve@latest init my-agent
cd my-agent
```

**最小可用示例**
1. 编辑 `agent/instructions.md`：
```markdown
你是一个返回模拟天气的助手，告知数据为模拟。
```
2. 创建 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "返回指定城市的模拟天气",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "晴", temperatureC: 22 };
  },
});
```
3. 配置模型 `agent/agent.ts`：
```ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-5",
});
```
4. 启动：
```bash
npm run dev
```

**依赖前提**：Node.js 环境、npm，连接相应模型服务（如 Anthropic API）的凭证。