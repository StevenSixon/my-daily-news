## 在线使用
访问 [https://muapi.ai/open-generative-ai](https://muapi.ai/open-generative-ai?utm_source=github&utm_medium=readme&utm_campaign=open-generative-ai)，注册免费账号即可从浏览器使用所有工作室。

## 桌面应用安装
1. 从 [Releases](https://github.com/Anil-matcha/Open-Generative-AI/releases) 下载对应平台安装包：
   - macOS（Apple Silicon）：`Open.Generative.AI-2.0.0-arm64.dmg`
   - macOS（Intel）：`Open.Generative.AI-2.0.0.dmg`
   - Windows：`Open.Generative.AI.Setup.2.0.0.exe`
   - Linux：`.AppImage` 或 `.deb`
2. 安装后首次运行需绕过 Gatekeeper（macOS）或 SmartScreen（Windows）。
3. 启动应用，进入 **Settings → Local Models** 安装本地推理引擎和模型（可选）。
4. 如需使用云端模型，在设置中输入 MuAPI 密钥。

## 本地模型示例（Z-Image Turbo）
1. 在桌面版设置中安装 sd.cpp 引擎，下载 Z-Image Turbo 模型及辅助文件（Qwen3-4B 文本编码器 + FLUX VAE）。
2. 进入 Image Studio，打开 ⚡ Local 开关，选择 Z-Image Turbo。
3. 输入提示词，点击生成，无需网络和 API 密钥。

## 前提条件
- 桌面应用无需额外依赖；源码构建需 Node.js 环境（README 未提供构建指南）。