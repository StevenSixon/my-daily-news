## 安装
**桌面版**：从 [GitHub Releases](https://github.com/0xsline/OpenChatCut/releases/latest) 下载对应平台安装包。注意 macOS 包未签名，首次启动需系统“安全性”中批准。

**从源码运行**：
```bash
git clone https://github.com/0xsline/OpenChatCut.git
cd OpenChatCut
npm install          # 需要 Node.js 24.x
cp .env.example .env.local
npm run dev
```
浏览器访问 `http://localhost:5199`。仅配置你实际使用的模型/媒体服务密钥到 `.env.local`。

## 最小可用示例
1. 创建项目，导入一段视频或图片。
2. 在聊天框输入“为这段视频添加淡入淡出转场和自动字幕”。
3. 代理会读取工程上下文，生成编辑提案，预览后应用。
4. 如需手动调整，可在时间线上微调，然后导出 MP4。

## 依赖前提
- Node.js 24.x（`.nvmrc` 提供版本管理）
- npm（安装依赖）
- 可选：本地 H.264 导出在 macOS 自动使用 VideoToolbox，Windows 使用 NVENC，或回退软件编码，可通过环境变量调优（见 `.env.example`）。