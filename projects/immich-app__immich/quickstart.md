**安装**：项目推荐使用 Docker Compose 部署。详细步骤请参考官方文档：https://immich.app/docs/install/requirements 。

**最小依赖**：
- 安装 Docker 与 Docker Compose
- 下载官方提供的 `docker-compose.yml` 和 `.env` 示例文件
- 调整环境变量（特别是 `UPLOAD_LOCATION`）
- 执行 `docker compose up -d` 启动服务

**访问**：浏览器打开 `http://<server-ip>:2283` 即可使用；移动端 App 设置服务器地址后即可自动备份。

> 注意：README 未提供具体安装命令，以上为通用部署路径，确切配置请严格参照官网文档。