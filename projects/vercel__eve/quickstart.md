### 安装与创建项目

```bash
npx eve@latest init my-agent
cd my-agent
```

这会在 `my-agent` 目录创建标准代理结构，安装依赖，初始化 Git，并启动交互式终端 UI。

### 最小可用示例

1. 编辑 `agent/instructions.md`：

```markdown
你是一个天气演示助手。告诉用户天气数据是模拟的。
```

2. 添加工具 `agent/tools/get_weather.ts`：

```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "返回模拟天气数据。",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "晴天", temperatureF: 72 };
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

4. 运行代理：

```bash
npm run dev
```

### 依赖前提

- Node.js（版本要求未在 README 列出，建议使用 LTS）
- 有效的 API 密钥对应的模型提供商（如 Anthropic）
- （可选）Slack/Discord Bot Token 以启用通道功能