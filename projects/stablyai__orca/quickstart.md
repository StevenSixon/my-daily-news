## 安装

1. 从 [onorca.dev/download](https://onorca.dev/download) 下载对应平台安装包（支持 macOS、Windows、Linux）。
2. 移动端可通过 iOS App Store、TestFlight 或直接下载 Android APK。

## 前提

- 本地已安装 [Git](https://git-scm.com/)。
- 至少安装一个受支持的 CLI 代理并配置好密钥（如 `claude`、`codex` 等）。

## 最小可用示例

```bash
# 1. 启动 Orca 桌面应用
# 2. 打开一个仓库目录
# 3. 按 Cmd+Shift+P 打开命令面板，选择 "Create Worktree"
# 4. 在代理选择框中勾选 Claude Code 和 Codex，填入同一指令
# 5. 提交后即可在右侧看到两个并行执行的终端，各自在独立分支工作
# 6. 完成后在 "Tree View" 中对比 diff，选择满意分支合并
```

如需脚本化：
```bash
orca worktree create --agent claude --agent codex --prompt "Refactor this module"
```

更多细节参阅 [文档站点](https://www.onorca.dev/docs)。