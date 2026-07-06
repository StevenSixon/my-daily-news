## 安装（推荐 Homebrew）
```bash
brew install gastown
```
或通过 npm：`npm install -g @gastown/gt`，或源码构建（Go 1.25+）。

## 前置依赖
- Git 2.25+、Dolt 2.0.7+、beads（bd）0.55.4+（Homebrew 自动安装）
- sqlite3（通常系统已有）
- tmux 3.0+（完整体验所需）
- 至少一种 AI 代理 CLI：Claude Code、Codex CLI 或 GitHub Copilot CLI

## 最小可用示例
1. 创建工作区并进入
```bash
gt install ~/gt --git && cd ~/gt
```
2. 添加一个代码仓库作为 Rig
```bash
gt rig add myproject https://github.com/you/repo.git
```
3. 创建你自己的 Crew 工作副本
```bash
gt crew add yourname --rig myproject
cd myproject/crew/yourname
```
4. 启动市长会话（协调界面）
```bash
gt mayor attach
```
在市长会话中，你可以直接告诉它要做什么，它会自动创建 Convoy、指派代理。

5. 无 tmux 最小模式（手动运行代理）
```bash
gt convoy create "Fix bugs" gt-abc12   # 创建任务
cd myproject/crew/yourname
gt sling gt-abc12 myproject           # 指派代理
claude --resume                        # 启动 Claude Code 执行
```
状态会保存在 Git Hook 中，随时可恢复。