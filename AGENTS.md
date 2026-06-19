# AGENTS.md

> 适用于所有 AI 编码代理（Claude Code、Cursor、Codex、Copilot 等）。

## 🔴 安全红线（公开仓库）

本仓库是**公开**的 GitHub 项目。**绝不**把密钥 / 凭据 / token 写入代码或提交到远程：

- 不提交 `.env`、`*.pem`、`*.key`、`*secret*.json`、`data/.feishu_token.json`（均已被 `.gitignore` 忽略，勿强加）。
- 不硬编码密钥；用 `env("KEY")` / `require_env("KEY")` 读取，新增项只在 `.env.example` 加空值占位。
- 提交前 `git diff --cached` 自查；不要在 commit/PR/日志/文档粘贴真实密钥或带 token 的 URL。
- 已启用 pre-commit 拦截钩子（`scripts/git-hooks/pre-commit`），勿用 `--no-verify` 绕过。

详细项目说明见 **[CLAUDE.md](./CLAUDE.md)**，安全细则与泄露处置见 **[SECURITY.md](./SECURITY.md)**。
