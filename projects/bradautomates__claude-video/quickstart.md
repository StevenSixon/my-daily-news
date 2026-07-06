## 安装与上手
**前置依赖**：首次运行时脚本会自动通过 `brew`（macOS）安装 `ffmpeg` 和 `yt-dlp`，或提示 Linux/Windows 相应命令。确保有相应包管理器权限。

**安装方式（任选其一）**：

1. **Claude Code（推荐，自动更新）**
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

2. **Codex / Cursor / Copilot / Gemini CLI 等 50+ 宿主**
```bash
npx skills add bradautomates/claude-video -g
```
（-g 全局安装，也可省略以项目级安装）

3. **claude.ai（Web 版）**
- 从 [Release 页](https://github.com/bradautomates/claude-video/releases/latest) 下载 `watch.skill` 文件
- 设置 → 能力 → 技能 → 点击 + 导入文件

**最小可用示例**：
```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
```
首次运行会自动完成环境检查（setup.py --check）并安装缺少的工具。之后即可直接对任何视频提问。