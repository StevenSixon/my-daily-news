### 前提条件
- Rust（stable）与 Tauri 2 系统依赖（见 https://v2.tauri.app/start/prerequisites/）
- Node.js 20+ 和 npm
- 可选：Docker Compose（用于 Context Engine）

### 安装与运行
```bash
cd apps/desktop
npm install

# 开发模式
npm run tauri:dev

# 生产构建
npm run tauri:build
```
Windows 用户可直接双击仓库根目录的 `launch-godcoder.bat`，脚本会自动设置 Cargo 路径并启动应用。

首次启动后，进入 Settings 添加 LLM 提供商（base_url + api_key + model），创建新会话，选择文件夹和模式即可开始使用。

### 可选：启动 Context Engine
```bash
cd services/context-engine
cp .env.example .env   # 设置 SUPERCODER_OPENAI_API_KEY

docker compose up -d --build
```
然后在应用设置中启用“Context engine”。