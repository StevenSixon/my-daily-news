### 安装
```bash
pip install vulnclaw
```

### 配置 API
```bash
# 选择提供商（自动填充 base URL）
vulnclaw config provider minimax   # 或 openai/deepseek 等
# 设置 API Key
vulnclaw config set llm.api_key sk-your-key
```

### 启动
```bash
# 进入 REPL 模式，可直接输入自然语言任务
vulnclaw
# 或直接一键执行全流程
vulnclaw run http://testphp.vulnweb.com
# 启动 Web UI
vulnclaw web
```

### 环境检查
```bash
vulnclaw doctor
```
输出会检查 Python、Node.js、npx、nmap 等依赖。手动安装时建议提前安装 nmap 和 Node.js (≥14)。

### Docker 快速体验
```bash
docker compose up --build
```
镜像已包含所有 MCP 运行时，访问 http://127.0.0.1:7788。