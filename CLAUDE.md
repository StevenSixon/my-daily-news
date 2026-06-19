# CLAUDE.md — 给 AI 编码代理的项目须知

## 🔴 安全红线（公开仓库，最高优先级）

**本仓库是公开的 GitHub 开源项目。绝不允许把任何密钥 / 凭据 / token 写入代码、提交或推送到远程。**

- **永不提交**：`.env`、`*.pem`、`*.key`、`*secret*.json`、`data/.feishu_token.json` 及任何含真实密钥值的文件。这些已被 `.gitignore` 忽略，不要用 `git add -f` 强加。
- **永不硬编码**密钥。代码里一律用 `env("KEY")` / `require_env("KEY")` 从 `.env` 读取；新增密钥时只在 `.env.example` 补**空值占位键名**。
- **提交前自查**：`git status` / `git diff --cached`，确认没有密钥、token、私钥、绝对家目录路径、内网地址等敏感信息。
- **不要在 commit message、PR 描述、日志、注释、文档里粘贴**真实密钥值或带 token 的 URL。
- 已启用 pre-commit 钩子（`scripts/git-hooks/pre-commit`）做兜底拦截，但**它是最后防线，不是借口**——你仍需主动避免暂存敏感内容。绝不要用 `--no-verify` 绕过，除非 100% 确认是误报。
- 完整规则与“万一泄露”处置见 **SECURITY.md**。

## 项目结构

AI 项目日报流水线：每天抓 GitHub trending 的 AI 项目 → LLM 分类/分析 → 生成日报 → 推送飞书 + 看板。

- `src/` — Python 流水线（`pipeline.py` 主流程，`collect/analyze/classify/push`，`github_client.py`、`feishu_client.py`）。
- `daily/<date>.json|.md` — 每日日报输出。
- `projects/<owner__name>/` — 每个项目的 `metadata.json` + `analysis.md`。
- `dashboard/` — React + Tailwind 看板，打包成单文件 `bundle.html`。数据由 `scripts/gen-data.mjs` 从上述文件生成；`refresh.sh` 负责“生成→打包→提交→推送”。详见 `dashboard/README.md`。
- `deploy/` — launchd 定时任务与入口脚本。
- `.github/workflows/deploy-dashboard.yml` — 把 `bundle.html` 发布到 GitHub Pages。

## 约定

- npm/pnpm 安装若 404：本机 `~/.npmrc` 指向内网源，命令前加 `npm_config_registry=https://registry.npmjs.org/`。
- 看板数据变更后重新生成：`cd dashboard && pnpm gen`，再用 artifacts-builder 的 `bundle-artifact.sh` 重打包。
