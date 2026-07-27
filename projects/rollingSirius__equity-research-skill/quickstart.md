## 安装
- **最简单**：将仓库链接 https://github.com/rollingSirius/equity-research-skill 直接发送给Claude或其他支持Skill的AI，告诉它“请安装并使用”。
- **Claude Code**：`git clone` 到 `~/.claude/skills/equity-research` 或项目 `.claude/skills/` 目录。
- **Claude Desktop/Cowork**：下载仓库zip，在 Settings → Capabilities → Skills 中上传。
- **Codex/其他Agent**：将仓库放入项目目录，配置Agent读取 `SKILL.md` 并遵循流程。

## 最小可用示例
在对话中直接输入：
- “帮我研究一下 NVDA”
- “深度分析一下 AAPL 最新财报”
- “按半导体行业附录分析台积电的周期位置和估值”
AI会自动加载Skill并生成报告（默认PDF）。也可显式调用：Claude Code 输入 `/equity-research 分析 TSLA`。

## 依赖前提
- **联网搜索/网页抓取**：建议，用于获取实时数据；离线使用时需用户提供申报材料。
- **Python环境**：非必须安装在本机；脚本可用Agent自带代码环境、在线notebook或AI托管环境执行，仅使用标准库。
- **PDF生成**：需要md→PDF工具链（如pandoc/wkhtmltopdf），若不可用则降级输出.md并说明。
- 不需要IBKR、Morningstar等专业连接器，有则更好，无则用公开源降级。