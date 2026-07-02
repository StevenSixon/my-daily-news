**1. 一键初始化**
```bash
npx @santifer/career-ops init
```
（需要 Node.js 环境，若已安装 Claude Code 等 AI CLI，则已满足）

**2. 进入目录并启动 AI CLI**
```bash
cd career-ops
claude   # 或 codex / gemini / opencode / agy / grok
```
首次启动会通过对话引导配置 CV、个人资料与目标角色，无需手动编辑。

**3. 使用**
- 粘贴职位 URL 或描述文本触发全自动管道
- 使用 `/career-ops` 命令（及其 CLI 别名）调用各种模式，如 `/career-ops scan` 扫描门户、`/career-ops pdf` 生成简历

**手动安装（可选）**
```bash
git clone https://github.com/santifer/career-ops.git
cd career-ops && npm install
npx playwright install chromium   # PDF 生成所需
npm run doctor                    # 检查环境
# 编辑 config/profile.example.yml 和 portals.yml
# 添加 cv.md
claude
```
前置依赖：Node.js、Chromium（Playwright 自动管理）、一个兼容的 AI CLI。