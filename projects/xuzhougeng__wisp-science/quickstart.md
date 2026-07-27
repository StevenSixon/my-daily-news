## 安装
### 前提
- **Rust 1.88+** 及 `wasm32-unknown-unknown` 目标
- **uv** (Python 环境管理器)
- **Trunk**: `cargo install --locked trunk`
- **Tauri CLI v2**: `cargo install tauri-cli --version "^2"`
- Windows 需 WebView2 运行时（系统自带或从微软下载）；macOS 需 Xcode 命令行工具
- 可选 R 环境（需 `Rscript` 及 `jsonlite` 包）

### 构建
```powershell
git clone https://github.com/xuzhougeng/wisp-science
cd wisp-science
cargo tauri dev    # 开发模式，热重载
cargo tauri build  # 生成安装包（MSI/NSIS for Windows, .dmg/.app for macOS）
```
Windows 构建生成的安装包未签名，可能触发 SmartScreen，选择“仍要运行”。

### 最小可用示例
1. 启动应用，按引导输入 DeepSeek API key（其他 provider 后续在 Settings → Models 配置）。
2. 新建项目，在对话框输入：
   - “从 NCBI 下载一个基因序列并统计 GC 含量”，agent 将调用内置 MCP 工具获取数据，并通过 Python REPL 计算。
3. 或加载种子演示项目（seed/ 目录）查看对话记录。

### 无桌面的 Headless CLI 模式
```powershell
$env:WISP_API_KEY = "<your key>"
$env:WISP_PROVIDER = "openai"
$env:WISP_MODEL = "deepseek-v4-pro"
cargo run -p wisp-cli
```
CLI 自动加载技能目录并启动 Python/R REPL。