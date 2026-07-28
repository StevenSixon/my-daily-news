## 安装
从 [onorca.dev/download](https://onorca.dev/download) 获取 macOS/Windows/Linux 桌面版，或通过 iOS App Store/TestFlight/Android APK 安装移动端。

## 最小可用示例
1. 确保安装好 git 和至少一个支持的代理 CLI（如 `claude`）。
2. 启动 Orca，打开终端，执行：
   ```
   orca worktree create --agent claude --prompt "实现一个简单的任务管理器"
   orca worktree create --agent codex --prompt "实现一个简单的任务管理器"
   ```
3. 在侧边栏观察两个代理的进度，通过 `Annotate AI Diff` 对比生成结果，选择更优的实现分支合并到主分支。

## 依赖前提
- Git
- 相应代理的运行时（Claude Code、Codex 等）及有效的 API 密钥/订阅
- (远程场景) SSH 访问远程主机