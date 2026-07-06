## 安装
```bash
# 使用安装脚本 (macOS/Linux)
curl -fsSL https://skillspec.sh/install.sh | sh
# 或通过 Cargo
cargo install skillspec
```

## 快速使用
```bash
# 1. 对任意技能目录进行风险分析
skillspec doctor ./my-skill

# 2. (在支持的 Agent 中) 导入技能并编译合同
# 在 Claude Code 等中运行：
# /skillspec import ./my-skill, compile it, install it, and prove it

# 3. 查看路由模式帮助
skillspec install router
```

## 依赖前提
- 需要有 `SKILL.md` 文件；Doctor 命令可独立运行。
- 若要使用插件系统导入和证明，需安装支持的 Agent 平台（Claude Code、Codex、Agents 等）。
- 如果通过 Cargo 安装，需要 Rust 工具链（stable 即可）。
- 在线 Doctor 页面无需本地安装。