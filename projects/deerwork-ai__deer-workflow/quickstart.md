## 安装
```bash
# 1. 安装 Bun 运行时
# 2. 登录 Codex CLI (默认 Agent，或安装 Claude Code)
# 3. 全局安装 deer-workflow
bun install --global @deerwork-ai/deer-workflow
```

## 最小可用示例
从自然语言生成工作流并运行：
```bash
# 生成工作流文件
deer-workflow create \
  "创建一个输入 topics 字符串数组，并行研究每个主题，并合成报告的工作流" \
  > workflow.ts

# 运行工作流
deer-workflow run ./workflow.ts \
  --input '{"topics":["Agent Skills","Dynamic Workflows"]}'
```

交互模式会展示分阶段的 TUI；若须打印 JSON 事件流，加 `--print`。