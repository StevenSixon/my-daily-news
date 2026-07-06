## 安装
- 从 [官网](https://onorca.dev/download) 或 [GitHub Releases](https://github.com/stablyai/orca/releases) 下载对应平台的桌面应用（macOS/Windows/Linux）。
- 移动端：iOS 用户可从 App Store 或 [TestFlight](https://testflight.apple.com/join/YjeGMQBA) 获取；Android 用户直接下载 [APK](https://github.com/stablyai/orca/releases/download/mobile-android-v0.0.22/app-release.apk)。

## 最小可用示例
1. 启动 Orca 桌面应用，添加你的 AI 服务 API 密钥（如 Anthropic、OpenAI 等）。
2. 打开项目，创建一个或多个工作树（Worktree）。
3. 在终端中运行你的 CLI 代理（例如 `claude` 或 `codex`），Orca 会自动在隔离环境中启动它。
4. 使用界面内的提示输入框向代理下达指令，或点击“设计模式”从浏览器发送 UI 元素信息。
5. 查看各工作树的实时输出，对比结果后通过 Git 面板合并最佳修改。
6. 出门在外时，打开手机伴侣，接收完成通知并远程指导代理继续工作。

## 依赖前提
- 已安装 Node.js（代理可能需要），但应用本身为独立二进制，无需额外环境。
- 需要使用外部 API 的服务订阅（如 Claude、Codex 等），请自行提前申请对应密钥。
- 对于 SSH 工作树功能，需要可访问的远程服务器和 SSH 密钥配置。

> 若需从源码构建，项目基于 TypeScript 和 Electron，请确保 Node >=18 并执行 `npm install && npm start`，但 README 未提供详细构建说明，建议直接使用预构建包。