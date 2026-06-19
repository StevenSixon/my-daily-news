## 安装与运行
### 前提
- 无需任何运行时依赖，仅需下载二进制。
- macOS/Linux: 使用curl安装脚本；Windows: PowerShell下载安装脚本。

### 安装
```bash
# 标准版
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash

# 带图可视化UI版
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --ui
```

### 使用
1. 重启你的AI编码代理（如Claude Code、Cursor等）。
2. 对代理说 **“Index this project”**。二进制将自动分析当前项目并构建知识图谱。
3. 后续通过代理对话直接发起结构化查询（如“find all functions that call init()”）。

### 启用UI
若安装了UI版本，在代理连接时，浏览器打开 `http://localhost:9749` 即可查看3D知识图谱。

### 更新
```bash
codebase-memory-mcp update
```

### 卸载
```bash
codebase-memory-mcp uninstall
```
（仅移除代理配置，不删除二进制和数据库。）