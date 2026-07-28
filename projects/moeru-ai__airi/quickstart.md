## 安装与使用
### 桌面版
**Windows**  
- 下载 .exe 安装程序，或通过 `winget install MoeruAI.AIRI` / `scoop bucket add airi https://github.com/moeru-ai/airi && scoop install airi/airi` 安装。
**macOS**  
- 下载 .dmg 或运行 `brew install --cask airi`。
**Linux**  
- 从 GitHub Releases 下载对应编译包（具体格式未在截断部分显示，推测为 AppImage 或 deb）。

### Web 版
直接访问 [https://airi.moeru.ai](https://airi.moeru.ai)，无需安装，支持移动端浏览器。

### 最小可用示例
1. 启动应用后，需配置 AI 后端（可能需 OpenAI API 密钥或本地模型服务，README 未明确）。
2. 通过界面导入或创建角色卡片（支持 Live2D 模型）。
3. 在对话框输入文字或启用麦克风直接语音聊天。
4. 如需游戏功能，启动 Minecraft/Factorio 并按照文档（在 project site 的 `/games` 路径）进行连接。

### 依赖前提
- 桌面版：无需额外环境，Electron 已内置。
- 自托管开发环境：需要 Node.js 及 pnpm（仓库使用 pnpm workspace）。
- AI 模型：需用户自行提供兼容的 API 端点（例如 OpenAI 格式）或本地推理服务，具体支持清单未在 README 详述。