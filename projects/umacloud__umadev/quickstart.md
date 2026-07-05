## 安装
```bash
npm install -g umadev
```
首次运行时会自动下载 ~224MB 的本地嵌入模型至 `~/.umadev/embed-model`（可选，失败则回退 BM25）。

**依赖前提**：必须安装并登录至少一个 AI 编码 CLI：
- Claude Code: `npm i -g @anthropic-ai/claude-code && claude auth login`
- Codex: `npm i -g @openai/codex && codex login`
- OpenCode: 从 opencode.ai 获取并配置

## 最小可用示例
```bash
umadev                       # 启动交互式聊天，首次会提示选择基础 CLI
# 输入需求，例如：
> build me a todo app with a Postgres backend

# 或者非交互方式运行：
umadev run "add CSV export to the reports page" --backend claude-code
```
构建会在独立的 `umadev/<slug>` 分支进行，不触碰当前工作分支。完成后输出规划文档、源代码、质量报告和交付证明包。