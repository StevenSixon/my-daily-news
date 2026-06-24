### 依赖
- Docker 与 Docker Compose
- 可访问容器镜像的网络（或提前拉取 `ghcr.io/larlarua/autocve-frontend:v1.0.0` 与 `ghcr.io/larlarua/autocve-backend:v1.0.0`）

### 一行命令部署
```bash
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.0/docker-compose.prod.yml | docker compose -f - up -d
```
Windows 使用 `curl.exe` 替换。

### 访问服务
- 前端：http://localhost:3000
- API 文档：http://localhost:8000/docs
- 数据库管理：http://localhost:8080（Adminer）

### 最小可用示例
1. 在前端界面配置 LLM 模型（API 密钥等，按界面引导操作）。
2. 导入一个开源仓库（支持 URL 或本地）。
3. 创建审计任务，选择审计模式（如“智能审计”快速体验 Finding Agent）。
4. 跟踪实时审计过程，结束后在漏洞管理模块查看结果，可导出英文或中文报告。

### 源码构建（可选）
```bash
git clone https://github.com/larlarua/AutoCVE.git
cd AutoCVE
docker compose up -d --build
```