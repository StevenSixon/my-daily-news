```bash
# 前提：Docker & Docker Compose，Claude Pro/Max 订阅或 API key，Telegram Bot Token
git clone https://github.com/duckbugio/flock
cd flock/adapters/telegram
cp .env.example .env
# 编辑 .env，至少填写：TELEGRAM_BOT_TOKEN，TELEGRAM_BOT_USERNAME，ALLOWED_USERS，CLAUDE_CODE_OAUTH_TOKEN
docker compose up -d
# 向你的机器人发送一条功能描述，即可开始
```