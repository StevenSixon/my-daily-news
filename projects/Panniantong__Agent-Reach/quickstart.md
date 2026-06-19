## 安装
### 前提
- Python 3.10+（需 pip）
- Node.js（自动检测安装，若无）
- 对于 OpenClaw 用户：需先开启 exec 权限（`openclaw config set tools.profile "coding"`）
- 桌面端使用 OpenCLI 需 Chrome 浏览器

### 最小可用示例
在你的 AI Agent 对话框输入：
```
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```
Agent 会自动完成：pip 安装、基建检测、MCP 搜索引擎配置、技能文件注入。

**安装后直接使用**（零配置）：
- “帮我看看这个 YouTube 视频讲什么” → 自动调 yt-dlp 提取字幕
- “B站搜一下 AI 教程” → 自动用 bili-cli 搜索
- “全网搜 LLM 框架对比” → Exa 语义搜索
- “这个网页写了啥” → Jina Reader 阅读

**解锁需要登录的平台**，告诉 Agent “帮我配 Twitter” 或 “帮我配 Reddit”，桌面环境优先使用 OpenCLI（浏览器登录态零配置），服务器会引导扫码或导出 Cookie。

**体检**：`agent-reach doctor` 查看所有渠道状态与当前活跃后端。

**更新**：
```
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

**安全模式/预览**：加 `--safe` 仅显示需求不自动修改系统；加 `--dry-run` 仅预览操作。