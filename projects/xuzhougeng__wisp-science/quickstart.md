### 前提
- Rust 1.88+ 并添加wasm32-unknown-unknown目标：`rustup target add wasm32-unknown-unknown`
- `uv`（Python环境管理器）
- 可选：R（需`Rscript`在PATH并安装`jsonlite`包）
- Trunk：`cargo install --locked trunk`
- Tauri CLI v2：`cargo install tauri-cli --version "^2"`
- Windows需WebView2运行时（通常已自带），macOS需Xcode命令行工具

### 构建运行
**桌面应用开发模式**  
```bash
cargo tauri dev      # 热重载，前端在1421端口
cargo tauri build    # 生成安装包（MSI/NSIS于target/release/bundle）
```

**无头CLI**  
```powershell
$env:WISP_API_KEY = "<your provider key>"
$env:WISP_PROVIDER = "openai"   # 可选: openai_responses, anthropic
$env:WISP_MODEL = "deepseek-v4-pro"
cargo run -p wisp-cli
```
CLI将加载内置技能目录，自动配置Python venv（`.wisp/python/.venv`）和R REPL。

### 最小可用示例
1. 启动桌面应用，在设置中添加模型提供商和API密钥
2. 新建项目，使用对话输入提示，如“查询UniProt中CRISPR相关蛋白并分析”
3. 查看右侧研究图谱和Artifact面板，追溯执行结果
4. （可选）配置SSH远程服务器，将计算任务发送至GPU节点