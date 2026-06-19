# 安全说明 / Security

> ⚠️ **本仓库是公开的 GitHub 开源项目。任何密钥、凭据、token 都绝不能进入提交或推送到远程。**

## 密钥放在哪里

所有密钥只存在于本地、**不入库**的文件中：

| 文件 | 内容 | 状态 |
|------|------|------|
| `.env` | GitHub / 飞书 / Anthropic / OpenAI / Gemini / DeepSeek 等密钥 | `.gitignore` 已忽略 |
| `data/.feishu_token.json` | 飞书 tenant_access_token 运行时缓存 | `.gitignore` 已忽略 |

需要的环境变量见 `.env.example`（仅含**键名**，无真实值）。新增密钥时：
1. 加到本地 `.env`；
2. 在 `.env.example` 里补一个**空值**的占位键名；
3. 代码里用 `env("KEY")` / `require_env("KEY")` 读取，**不要**硬编码。

## 三层防护

1. **`.gitignore`** —— 忽略 `.env*`（保留 `.env.example`）、`*.pem`、`*.key`、`*secret*.json`、token 缓存等。
2. **pre-commit 钩子**（`scripts/git-hooks/pre-commit`）—— 提交前自动扫描，发现密钥文件名或密钥值（`ghp_…`、`sk-…`、`AKIA…`、私钥块等）即拒绝提交。
3. **自动化脚本** —— `dashboard/refresh.sh` 只暂存生成产物（`dashboard/src/daily.json`、`dashboard/bundle.html`，均由公开 GitHub 数据生成），不会 `git add -A`。

### 启用 pre-commit 钩子（克隆后执行一次）

```bash
git config core.hooksPath scripts/git-hooks
```

> 误报时可用 `git commit --no-verify` 跳过，但**务必先确认确实不含密钥**。

## 万一密钥已经被提交了怎么办

提交进 git 历史的密钥即使后续删除，仍能从历史中找回，必须按泄露处理：

1. **立刻吊销/轮换**该密钥（GitHub token、飞书 App Secret、各家 API Key 都到对应控制台重置）。
2. 用 `git filter-repo` 或 BFG 清理历史，再强推：
   ```bash
   git filter-repo --path .env --invert-paths   # 示例：从全部历史移除 .env
   ```
3. 确认远程（含 PR、fork、缓存）已清理。

## 上报

发现疑似泄露或安全问题，请私下联系仓库所有者，不要公开开 issue 贴出敏感内容。
