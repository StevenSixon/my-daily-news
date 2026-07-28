### 桌面安装包
从 [GitHub Releases](https://github.com/0xsline/OpenChatCut/releases/latest) 下载对应平台的 DMG/安装器/AppImage。macOS 版本首次打开需手动允许运行。

### 从源码运行
**依赖**：Node.js 24.x、npm（推荐使用 nvm，项目内置 `.nvmrc`）
```bash
git clone https://github.com/0xsline/OpenChatCut.git
cd OpenChatCut
npm install
cp .env.example .env.local   # 按需填写模型或媒体服务的 API 密钥
npm run dev
```
浏览器访问 `http://localhost:5199`。

### 桌面开发
```bash
npm run desktop:dev
```
桌面环境与 Web 版共享同一套嵌入式服务。

### 媒体编码配置
默认优先使用硬件加速（macOS VideoToolbox，Windows NVENC），可通过 `.env.local` 中的环境变量调整渲染并发、禁用硬件编码或覆盖编码器。详见 `.env.example`。