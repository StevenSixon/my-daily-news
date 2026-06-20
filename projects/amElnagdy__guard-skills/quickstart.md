**安装整个包**
```bash
npx skills add amElnagdy/guard-skills
```

**或安装单个守卫**
```bash
npx skills add amElnagdy/guard-skills --skill clean-code-guard
# 可选 --agent 指定目标代理（如 codex、claude-code）
```

**使用示例**
在 AI 生成 diff 后直接调用：
```text
Use $clean-code-guard on the diff you just produced.
Use $test-guard on the tests you just wrote.
Use $wp-guard on this WordPress plugin change.
```

**依赖前提**
- Node.js 环境（支持 npx）
- 已配置的编码代理（如 Codex、Claude Code 等）
- 无需额外网络或 MCP 服务