### 前提
- Node.js 22.x、pnpm 10.x、Git LFS 已安装
- 克隆仓库并拉取子模块：
```bash
git clone https://github.com/makecindy/cindy.git
cd cindy
git submodule update --init --recursive cindy-protocol
git lfs pull
pnpm install
```
- 运行桌面开发环境（中国大陆账户用 `--region=cn`，其他用 `global`）：
```bash
pnpm restart:desktop:remote --region=global
```
### 最小示例
1. 启动后看到登录界面，使用你的 Cindy 云账号登录（或选择“Local mode”跳过登录）。
2. 在主界面选择一个 harness（如 Claude Code）和模型，输入一个简单任务，例如“用 TypeScript 写一个 Hello World 函数并保存为 hello.ts”。
3. Agent 将自动生成文件并保存到工作目录，同时输出执行结果。

> 注意：本地模式不支持服务器相关功能；正式使用前可在官网下载预构建包。