## 安装
```bash
npx eve@latest init my-agent
```
这会在 `my-agent/` 创建项目，安装依赖，初始化 Git 并启动交互终端。

## 最小可用示例
1. 编辑 `agent/instructions.md`，写入：
```md
你是一个简洁的天气演示助手，告诉用户天气数据是模拟的。
```
2. 添加工具 `agent/tools/get_weather.ts`：
```ts
import { defineTool } from "eve/tools";
import { z } from "zod";

export default defineTool({
  description: "返回模拟天气数据",
  inputSchema: z.object({ city: z.string().min(1) }),
  async execute({ city }) {
    return { city, condition: "晴", temperatureF: 72 };
  },
});
```
3. 选择模型 `agent/agent.ts`：
```ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-4.6",
});
```
4. 启动代理：
```bash
npm run dev
```

## 依赖前提
- Node.js 环境
- 项目中需安装 Zod（用于工具 schema）
- 所选模型提供商的有效 API Key（需按对应服务配置）
- 如需频道或沙箱，可能需要额外环境变量或容器