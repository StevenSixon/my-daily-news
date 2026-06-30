**前置依赖**
- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Node.js](https://nodejs.org/en/download)

**安装**
```bash
uvx google-agents-cli setup
```
或仅安装编码助手技能（不装完整 CLI）：
```bash
npx skills add google/agents-cli
```

**最小可用示例**
1. 打开任意编码助手（如 Claude Code）。
2. 对助手说：
> Use agents-cli to build a caveman-style agent that compresses verbose text into terse, technical grunts

助手将使用 agents-cli 的脚手架、代码生成、部署命令完成一个可用 Agent。

**独立使用 CLI**
```bash
agents-cli scaffold my-agent
cd my-agent
agents-cli run "Hello"
agents-cli eval generate
agents-cli deploy
```