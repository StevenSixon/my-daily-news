### 安装
```bash
npm install -g umadev
```
确保已安装并登录至少一个支持的 CLI（如 Claude Code：`npm i -g @anthropic-ai/claude-code && claude auth login`）。

### 最小示例
```bash
# 交互式对话
umadev
# 输入任务，如：build me a todo app with a Postgres backend

# 非交互式运行
umadev run "add CSV export to the reports page" --backend claude-code
```
首次运行时选择基座，后续构建将在隔离分支进行，完成后输出代码、文档和交付证明。