## 安装
### 前提
- 操作系统：macOS、Linux 或 Windows
- Claude Code 或其他兼容宿主（Codex、Cursor、Copilot、Gemini CLI 等）已安装
- 首次运行会自动检测并提示安装 `ffmpeg` 和 `yt-dlp`（macOS 使用 brew，Linux/Windows 给出安装命令）
- 若视频无字幕且需使用回退功能，需要 Groq 或 OpenAI 的 Whisper API 密钥（**可选**）

### Claude Code
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

### 其他 Agent 宿主（Codex、Cursor、Copilot、Gemini CLI 等 50+）
```bash
npx skills add bradautomates/claude-video -g
```
`-g` 全局安装（用户级），去掉则为当前项目安装。

### claude.ai（网页版）
1. 从 [Releases](https://github.com/bradautomates/claude-video/releases/latest) 下载 `watch.skill`
2. 进入 Settings → Capabilities → Skills，点击 `+` 并导入文件

## 最小可用示例
### 分析 YouTube 视频的特定时刻
```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
```

### 诊断录屏 Bug
```
/watch bug-repro.mov what's going wrong?
```

### 长视频总结（仅依赖字幕，零帧提取）
```
/watch https://youtu.be/<long-talk> summarize this --detail transcript
```

### 高精度分析（无帧预算上限）
```
/watch https://youtu.be/<launch-video> what's actually new --detail token-burner
```

### 指定时间段密集分析
```
/watch https://youtu.be/<video> what happens between 1:20 and 2:00 --start 1:20 --end 2:00
```