### 安装方式

**macOS 桌面应用**
- 从 [Latest Release](https://github.com/inkeep/open-knowledge/releases/latest) 下载 `OpenKnowledge-arm64.dmg`
- 打开 DMG，将 **OpenKnowledge** 拖入 `Applications`，启动

**跨平台 Web 应用（Linux/Windows/Intel Mac）**
1. 确保已安装 Node.js 24+
2. 全局安装 CLI：
   ```bash
   npm install -g @inkeep/open-knowledge
   ```
3. 进入项目目录并初始化：
   ```bash
   cd your-project
   ok init          # 脚手架项目，自动配置 Claude Code、Cursor、Codex
   ok start --open  # 启动本地 Web 编辑器并在浏览器中打开
   ```

### 最小可用示例
- 安装后打开项目，即进入 WYSIWYG 编辑界面
- 点击「Ask AI」或右下角代理图标，选择已连接的桌面 AI 工具，直接对话并生成/编辑内容
- 所有笔记以标准 Markdown 文件保存在项目目录，可用 Git 版本控制