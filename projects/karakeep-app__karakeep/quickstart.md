**环境要求**：Docker、Meilisearch（用于搜索）、关系数据库（推荐PostgreSQL）。

**快速部署**：
参考官方文档 [https://docs.karakeep.app/Installation/docker](https://docs.karakeep.app/Installation/docker)
典型流程：
```bash
git clone https://github.com/karakeep-app/karakeep.git
cd karakeep
# 复制并编辑环境变量，配置Meilisearch地址、数据库连接、AI密钥等
cp .env.example .env
# 启动服务栈
docker compose up -d
```
访问 `http://localhost:3000` 开始使用。
更多配置选项（Ollama本地模型、SSO等）见文档。