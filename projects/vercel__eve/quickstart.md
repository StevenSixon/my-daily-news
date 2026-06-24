## 安装与初始化

```bash
npx eve@latest init my-agent
cd my-agent
```

这会创建项目、安装依赖、初始化 Git 并启动交互式终端。

## 最小可用示例

1. **编辑系统提示** `agent/instructions.md`：

```md
You are a concise weather demo assistant. Tell users that the weather data is mocked.
```

2. **添加工具** `agent/tools/get_weather.ts`：

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

3. **选择模型** `agent/agent.ts`：

```ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-4.6",
});
```

4. **启动**：

```bash
npm run dev
```

## 依赖前提

- Node.js 18 或更高版本
- 对应模型提供商的 API 密钥（如 Anthropic API Key），需通过环境变量或配置文件注入（具体方式参考 `agent-config.md`）。