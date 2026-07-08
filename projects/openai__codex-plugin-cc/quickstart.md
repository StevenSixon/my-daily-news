## 安装
```bash
# 在 Claude Code 中添加 marketplace
/plugin marketplace add openai/codex-plugin-cc

# 安装插件
/plugin install codex@openai-codex

# 重载插件
/reload-plugins

# 运行设置
/codex:setup
```
若未安装 Codex CLI，按提示安装或手动执行 `npm install -g @openai/codex`，然后 `!codex login` 登录。

## 最小可用示例
```bash
# 后台普通审查
/codex:review --background

# 查看状态
/codex:status

# 获取结果
/codex:result
```

## 前提
- Node.js 18.18+
- ChatGPT 订阅（含 Free）或 OpenAI API 密钥，具有 Codex 使用额度
- 已登录 Codex CLI