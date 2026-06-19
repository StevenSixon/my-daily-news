### 安装
**桌面版（推荐）**  
从 [Releases](https://github.com/alchaincyf/fanbox/releases/latest) 下载最新 `FanBox-2.3.1-arm64.dmg`，拖入 `应用程序` 文件夹。  
- 平台：macOS (Apple Silicon)  
- 首次打开若提示“未验证的开发者”：右键点击 → 打开 → 确认。

**网页版**（仅文件浏览/搜索/预览，无终端与编辑器）  
```bash
git clone https://github.com/alchaincyf/fanbox
cd fanbox
node server.js
```
浏览器访问 `http://localhost:4567`。

**开发模式**  
```bash
npm install
npm run app   # 启动完整桌面应用
```

### 最小可用示例
1. 启动 FanBox 后，左侧为文件浏览器，点击文件夹即可预览内容。  
2. 使用 `⌘K` 搜索项目，输入项目名片段，回车打开；或在结果上按 `⌘↵` 用外部编辑器打开整个项目。  
3. 在右侧或下方终端中启动 Claude Code：输入 `claude`，然后在文件列表中拖一个文件到终端提供上下文。  
4. 观察 Agent 写文件时卡片高亮，点击“跟随模式”图标，可实时看到代码或 HTML 变化。  
5. 点击项目文件夹，在下方可看到历史会话，点击“▶ 续上”自动在终端执行 `claude --resume`。

### 依赖前提
- 桌面版：macOS 12+ (Apple Silicon)，无需 Node.js 或其他运行时（内置 Electron）。  
- 网页版：Node.js 18+。  
- 内嵌终端使用系统默认 Shell（zsh/bash），需预先安装 Claude Code 或 Codex CLI。