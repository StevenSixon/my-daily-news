## 安装与最小示例

### 1. 一键连接代理
```bash
npx -y nubase_cli@latest install-skills
```
（在项目目录执行，自动安装 Claude Code / Codex 技能并配置 MCP，浏览器授权后即可使用）

### 2. 自托管服务（可选）
```bash
docker run -d --name nubase \
  -p 9999:9999 -p 5432:5432 \
  -v nubase_data:/data \
  ottermind/nubase:latest
```
访问 `http://localhost:9999/studio` 创建账户和项目，点击 Provision 初始化数据库。

### 3. 使用代理构建应用
代理连接后可执行：
- 查看/创建/修改数据库表
- 运行 SQL 和设置 RLS
- 部署边缘函数（`/functions/v1`）
- 上传静态资源到 CDN（`/assets/v1`）
- 写入/搜索记忆（`/mem/v1`）
- 创建定时任务

### 依赖前提
- 连接代理：需 Node.js 环境，已安装 Claude Code 或 Codex
- 自托管：Docker，无外部依赖（镜像内含 PostgreSQL、Redis）
- 记忆功能需要 OpenAI 或 Anthropic API 密钥（可选）