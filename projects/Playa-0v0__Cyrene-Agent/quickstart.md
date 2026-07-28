## 安装与运行

### 前提
- Windows 10/11 64位
- Node.js 24 LTS, npm 10+
- Rust stable + Visual Studio 2022 Build Tools（仅源码构建需要）
- （可选）网易云音乐客户端 + uv

### 步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/Playa-0v0/Cyrene-Agent.git
   cd Cyrene-Agent
   ```
2. 安装依赖
   ```bash
   npm ci
   ```
3. 构建 Rust 截图助手（首次必须）
   ```bash
   npm run build:screenshot-helper
   npm run build
   ```
4. 启动应用
   ```bash
   npm start
   ```
   （开发模式：`npm run dev`）
5. 安装推荐模型 BGE-M3（从 Releases 下载 zip 解压到项目根目录），重启后在设置→本地 AI 模型确认已安装。
6. 配置 API Key
   - 托盘图标 → 打开设置 → 模型设置：填入 LLM 厂商、API Key、模型名。
   - 按需配置 TTS/ASR/外部渠道。

### 最小可用示例
- 启动后桌面会出现昔涟 Live2D 形象，点击对话框即可聊天（Chat 模式）。
- 在聊天窗口切换到 Work 模式可进行任务操作，如“帮我查今天天气”或“写一个会议纪要”。
- 右下角托盘图标可管理窗口和设置。