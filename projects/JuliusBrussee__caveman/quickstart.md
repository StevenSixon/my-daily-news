## 安装
```bash
# macOS/Linux/WSL
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```
**要求**: Node.js ≥18。安装器会自动检测本机代理并安装对应插件/扩展/规则文件。

## 最小可用示例
1. 在支持的代理（如Claude Code）中对话，代理已默认启用穴居人模式，或手动输入 `/caveman` 或说 "talk like caveman"。
2. 测试效果：输入“解释React组件为什么重新渲染？”，代理会回答精简版，如“New object ref each render. Wrap in useMemo.”
3. 切换级别：`/caveman ultra` 获得更短回复；`/caveman wenyan` 尝试文言风。关闭：说 "normal mode"。

## 依赖前提
- Node.js ≥18
- 至少安装了一个支持的AI代理（Claude Code CLI, Gemini CLI, Cursor等）