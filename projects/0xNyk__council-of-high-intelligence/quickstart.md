## 安装与使用

### 前提
- 已安装 Claude Code 或 Codex CLI。
- 若需使用非 Anthropic 模型，需额外安装对应 CLI（如 `gemini`、`ollama`）并导出相应的 API 密钥。

### 安装
```bash
git clone https://github.com/0xNyk/council-of-high-intelligence.git
cd council-of-high-intelligence
./install.sh          # 为 Claude Code 安装
# 或
./install.sh --codex   # 为 Codex 安装
```

### 最小可用示例
在 Claude Code 或 Codex 会话中：
```
/council 我们应该开源我们的智能体框架吗？
/council --quick 这里应该加缓存吗？
/council --duo 使用微服务还是单体？
```

### 高级用法
- 指定三人组：`/council --triad architecture 什么是我们的竞争护城河？`
- 仅用双人并指名：`/council --duo --members torvalds,ada 这个抽象值得吗？`
- 使用预定义配置文件：`/council --profile execution-lean 今天发布吗？`

安装后即通过自动探测分配服务提供者，无需额外配置。