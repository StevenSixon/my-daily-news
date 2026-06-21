## 安装
- 系统要求：macOS 26 (Tahoe) ，Apple Silicon (M 系列芯片)
- 下载：从 [GitHub Releases](https://github.com/palmier-io/palmier-pro/releases) 获取 `PalmierPro.dmg` 安装
- 无需登录即可使用免费编辑器功能

## 连接 AI 代理（MCP）
启动应用后，MCP 服务自动运行于 `http://127.0.0.1:19789/mcp`。

**Claude Code**：
```bash
claude mcp add --transport http palmier-pro http://127.0.0.1:19789/mcp
```

**Codex**：
```bash
codex mcp add palmier-pro --url http://127.0.0.1:19789/mcp
```

**Cursor**：应用内 `Help` → `MCP Instructions` → `Install in Cursor`，或手动配置 `~/.cursor/mcp.json`。

## 最小可用示例
1. 打开 Palmier Pro，新建或打开项目
2. 在 Claude Code 中执行自然语言指令，例如：“在时间线 0 秒位置添加视频 example.mp4，裁剪开头 1 秒”
3. AI 会通过 MCP 调用工具操作编辑器，结果即时反映在界面上

## 依赖前提
- 仅 macOS，无 Windows/Linux 支持
- 需 Apple Silicon
- AI 生成功能需订阅（其余功能免费）