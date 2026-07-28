## 安装
### 桌面应用
从[Releases](https://github.com/xuzhougeng/wisp-science/releases)下载对应平台的安装包。macOS选Apple Silicon或Intel；Windows选MSI/NSIS（未签名，需选择“仍要运行”）。首次启动需要WebView2 Runtime（Win10/11通常已预装）。

### 从源码构建
```bash
# 前提：Rust 1.88+, wasm32-unknown-unknown target, uv, Trunk, Tauri CLI v2
git clone https://github.com/xuzhougeng/wisp-science.git
cd wisp-science
cargo tauri dev    # 热加载开发模式
cargo tauri build  # 生成安装包
```

### Headless CLI
直接运行CLI：
```bash
export WISP_API_KEY="<your-key>"
export WISP_PROVIDER="openai"   # 或 anthropic
export WISP_MODEL="deepseek-v4-pro"
cargo run -p wisp-cli
```
CLI自动加载内置Skills和Python/R REPL。首次运行会在`.wisp/`下创建venv。

## 最小可用示例
1. 启动桌面应用，进入Settings配置模型（API密钥保存至OS密钥环）。
2. 创建新项目，选择本地运行环境。
3. 在会话中提问“用Python画一个火山图”，代理将自动调用Python REPL执行并返回图表。
4. 查询NCBI：“查找人类BRCA1基因的序列”，代理通过MCP工具获取数据。