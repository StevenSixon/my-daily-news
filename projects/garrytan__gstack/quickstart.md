## 准备工作
- 安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- 安装 [Git](https://git-scm.com/)
- 安装 [Bun](https://bun.sh/) v1.0+
- 若在 Windows 上，还需 [Node.js](https://nodejs.org/)

## 安装
在 Claude Code 对话中粘贴以下命令，让 Claude 执行：
```
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```
然后根据提示将技能列表加入 CLAUDE.md。

## 最小上手
1. 运行 `/office-hours`：描述你的产品想法，Claude 会进行问诊并输出设计文档。
2. 对任意功能想法运行 `/plan-ceo-review` 进行策略审查。
3. 在有代码变更的分支运行 `/review` 获取审查和自动修复。
4. 运行 `/qa https://你的测试环境` 进行浏览器端自动化测试。
5. 运行 `/ship` 生成测试和 PR。

## 团队共享（推荐）
在仓库内执行：
```bash
(cd ~/.claude/skills/gstack && ./setup --team) && ~/.claude/skills/gstack/bin/gstack-team-init required && git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```
这将让团队成员在工作时自动获取 gstack 并保持版本一致。