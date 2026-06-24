## 安装
```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash
```
Windows 下使用 PowerShell 运行 `install.ps1`。可选 `--ui` 参数安装可视化版本。

**依赖前提**：无（单静态二进制）。安装脚本会自动配置检测到的 AI 代理（Claude Code、Aider 等 11 种）。

## 最小可用示例
1. 重启你的 AI 编码代理
2. 在代理中说 “Index this project”
3. 查询示例：
   - “Find dead functions”
   - “Show architecture overview”
   - “What HTTP routes exist in this project?”

## 自动索引
```bash
codebase-memory-mcp config set auto_index true
```
之后首次连接时自动索引项目。