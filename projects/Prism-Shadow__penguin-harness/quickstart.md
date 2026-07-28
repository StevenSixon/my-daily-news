## 安装
```bash
# Linux / macOS
curl -fsSL https://penguin.ooo/install.sh | sh

# Windows PowerShell
irm https://penguin.ooo/install.ps1 | iex

# 或通过 npm（需 Node >=24）
npm install -g @prismshadow/penguin-cli
```

## 启动 Web 界面
```bash
penguin web
# 自动打开 http://127.0.0.1:7364 ，默认账号 admin / penguin-2026
```

## 最小 CLI 示例
```bash
# 配置模型（需要API密钥）
penguin config model add --provider deepseek --model-id deepseek-v4-pro --api-key sk-... --set-default

# 一句话任务
penguin run -m "创建一个包含'Hello, Penguin'的hello.txt文件"

# 交互式对话
penguin chat
```

## SDK 快速入门
```typescript
import { createAgent, isCompleteModelMessage, userText } from "@prismshadow/penguin-core";

const agent = await createAgent({ agentId: "default_agent" });
const session = await agent.createSession({ workspaceDir: process.cwd() });

for await (const output of session.run([userText("创建hello.txt并写入hi")], {
  approve: async () => "allow",
})) {
  if (isCompleteModelMessage(output) && output.payload.type === "text") {
    console.log(output.payload.text);
  }
}
```

**依赖前提**：至少一个模型提供商的API密钥；安装脚本会自动携带Node运行时，若使用npm方式需Node ≥24。