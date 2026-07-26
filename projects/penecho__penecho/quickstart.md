## 安装
- 桌面版：从 GitHub Releases 下载
- npm 版（需 Node.js 20.3+）：
  ```bash
  npm install -g penecho
  ```

## 配置与启动
1. 交互式配置（至少配置一个 AI 后端）：
   ```bash
   penecho configure
   ```
   选择 Claude CLI / Codex CLI / API，并设置模型、effort 等。
2. 启动服务：
   ```bash
   penecho
   ```
   默认监听 http://localhost:3888，终端会打印本机局域网地址。
3. 也可直接指定后端启动：
   ```bash
   penecho --codex --model gpt-5.6-sol --effort xhigh
   penecho --claude --model opus --effort max
   ```

## 必备前提
- Codex 后端需先安装并认证 `@openai/codex` CLI，执行 `codex login status` 确认
- Claude 后端需安装 Claude Code CLI 并完成认证
- API 后端需提供 OpenAI 或 Anthropic 兼容密钥（明文保存于 `~/.penecho/config.env`，仅本地）