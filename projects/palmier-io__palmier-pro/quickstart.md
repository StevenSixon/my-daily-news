### 前提条件
- macOS 26 (Tahoe) 及以上
- Apple Silicon (M系列芯片)
- 可选：Claude Code / Cursor / Codex 用于AI协作

### 安装
从 [Release 页面](https://github.com/palmier-io/palmier-pro/releases) 下载 `PalmierPro.dmg`，拖入应用文件夹打开。

### 快速接入Agent
1. 打开 Palmier Pro
2. 在终端执行：
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```
3. 在Claude Code中尝试：“在当前时间线第0秒插入一个纯色背景，延长到8秒，并添加标题字幕”
4. 观察编辑器中时间线实时变化

Cursor 用户可在应用内 `Help` → `MCP Instructions` → `Install in Cursor` 完成配置。