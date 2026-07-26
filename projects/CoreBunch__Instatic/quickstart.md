## 部署 Instatic

### 1. 一键部署（推荐）
- **Railway + SQLite**：[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/instatic-cms-sqlite)
- **Railway + Postgres**：[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/instatic-cms-postgres)

### 2. 通过 Docker 自托管
从项目仓库获取 compose 文件（假设已 git clone）：
```bash
# 使用 SQLite（单机推荐）
INSTATIC_IMAGE=ghcr.io/corebunch/instatic:latest \
  docker compose -f compose.prod.yml -f compose.sqlite.yml up -d
```
详细 VPS、Postgres、HTTPS 配置见 [deployment 文档](docs/deployment/README.md)。

### 最低要求
- Docker 环境（容器内已包含 Bun 及所有依赖）
- 持久化存储卷（用于数据库和上传文件）

项目本身不需要本地安装 Node、Bun 或数据库，镜像开箱即用。