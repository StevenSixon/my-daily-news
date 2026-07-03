## 安装
```bash
curl -fsSL https://skillspec.sh/install.sh | sh
# 或
cargo install skillspec
```

## 最小可用示例
```bash
# 本地技能风险分析
skillspec doctor ./my-skill

# 一键生成契约并安装到平台（需 Agent 插件支持）
# 在 Agent 对话中执行：/skillspec import ./my-skill, compile it, test it, install it, and prove it
```

## 依赖前提
- 操作系统：macOS / Linux / Windows
- 可选：Rust 环境（用于 Cargo 安装）
- Agent 集成需对应平台已安装 SkillSpec 插件（Claude Code / Codex）