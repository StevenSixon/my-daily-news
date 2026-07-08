## 安装
```bash
npx skills add https://github.com/isjiamu/gzh-design-skill
```
或由 Agent 自动识别安装，也可手动克隆：
```bash
git clone https://github.com/isjiamu/gzh-design-skill.git ~/.claude/skills/gzh-design
```
## 使用
对任意集成了该 skill 的 Agent（Claude Code、Cursor 等）直接说：
```
用摸鱼绿把这篇文章排成公众号 HTML：article.md
```
Agent 会按 `SKILL.md` 工作流读取主题组件库、解析 Markdown、装配 HTML，并运行校验脚本，最后输出可预览和复制的 HTML 文件。

## 依赖前提
- Node.js 环境（用于 `npx skills`）
- Python 3（需运行校验脚本，项目内已提供脚本，无需额外安装库）
- 支持的 AI Agent 客户端（Claude Code CLI 等，用于驱动排版流程）
> ⚠️ 本项目本身**不提供独立命令行生成工具**，排版过程必须由 AI Agent 根据 `SKILL.md` 动态组装，而校验脚本可独立运行：
> ```bash
> python3 scripts/validate_gzh_html.py out.html
> ```