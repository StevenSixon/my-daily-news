## 安装

确保 Node.js 环境，运行：

```bash
npx eve@latest init my-agent
```

会在 `my-agent` 目录下生成标准项目结构，安装依赖并启动终端交互。

## 最小可用示例

1. 编辑 `agent/instructions.md`：
```md
你是一个简洁的天气演示助手，告知用户天气数据为模拟。
```

2. 添加工具 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "返回指定城市的模拟天气。",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "晴", temperatureF: 72 };
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

4. 启动开发：
```bash
npm run dev
```

即可在交互终端测试你的第一个 Agent。

## 依赖前提

- Node.js (>=18)
- 可选的模型提供商 API Key（如 Anthropic）