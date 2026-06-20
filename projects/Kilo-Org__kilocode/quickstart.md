## 安装
**VS Code**：在扩展市场搜索 "Kilo Code" 安装。
**CLI**：`npm install -g @kilocode/cli` 或 `curl -fsSL https://kilo.ai/cli/install | bash`。
**JetBrains**：在插件市场安装 "Kilo Code"。

## 最小可用示例
```bash
# CLI 模式：在项目目录下启动会话
kilo
# 进入交互后直接用自然语言提需求

# 自主模式（CI/CD）
kilo run --auto "修复所有失败的测试并确保通过"
```

## 依赖前提
- CLI 需要 Node.js 环境（未指定最低版本，建议 LTS）。
- VS Code 或 JetBrains IDE 已安装对应扩展/插件。
- 无需直接提供 API 密钥即可开始（通过 Kilo 账户接入模型）。