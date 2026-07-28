## 安装与快速启动
1. **前提条件**：macOS/Linux/Windows，无需预装 Python（安装脚本通过 uv 自动部署 Python 3.12 到 `~/.octop/venv`）。
2. **安装**：
   - macOS/Linux 推荐一行命令：`curl -fsSL https://.../install.sh | bash`
   - Windows：`irm https://.../install.ps1 | iex`
   - 或使用 pip：`pip install octop`（需自行管理 Python 3.11+ 环境）
   - Docker（生产环境）：`docker compose -f docker/docker-compose.yml up -d`
3. **初始化**：`octop init`，交互式创建数据库、JWT 密钥和管理员账号。
4. **运行**：`octop run`，然后访问 `http://127.0.0.1:8088`，默认凭据 admin/octop（务必修改）。
5. **配置**：通过 `octop models`、`octop provider` 等命令配置 LLM 供应商和模型。
6. **可选组件**：安装浏览器自动化插件 `--extras browser` 或飞书通道 `--extras channels-feishu`。

详细文档参见 [docs/](./docs/) 目录。