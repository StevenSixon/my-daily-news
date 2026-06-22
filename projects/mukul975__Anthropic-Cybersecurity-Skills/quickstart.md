### 安装

推荐使用 npx（依赖 Node.js 和 agentskills CLI）：

```bash
npm install -g @agentskills/cli   # 若尚未安装
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

或直接克隆仓库：

```bash
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

### 使用

技能文件位于仓库 `skills/` 目录下。任何支持 [agentskills.io](https://agentskills.io) 标准的 AI 代理平台（如 Claude Code、GitHub Copilot、Cursor）均可直接读取并利用。

**最小示例**：在 Claude Code 中激活后，代理可自动根据任务需求匹配相应技能。无需额外配置，直接开始安全交互。

> 详细平台配置请参考 [agentskills.io 文档](https://agentskills.io/docs)。