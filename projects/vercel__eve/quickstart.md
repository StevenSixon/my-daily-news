## 安装与初始化

```bash
npx eve@latest init my-agent
```
自动创建目录、安装依赖、初始化 Git 并启动交互终端。
若已存在项目，可在项目根执行：
```bash
cd myapp
npx eve@latest init .
```

## 最小示例

1. 编写系统提示 `agent/instructions.md`：
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

export default defineAgent({
  model: "anthropic/claude-sonnet-4.6",
});
```
4. 启动：
```bash
npm run dev
```

**前提**：Node.js 环境，需要模型提供商 API 密钥（如 Anthropic API key）配置在环境变量或 .env 文件中。