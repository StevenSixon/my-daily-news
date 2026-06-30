### 依赖
- Docker 及 Docker Compose
- 可访问的 LLM 服务（OpenAI 兼容 API）

### 一行部署
```bash
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml | docker compose -f - up -d
```

### 访问
- 前端：http://localhost:3000
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

### 最小可用流程
1. 登录前端，进入“模型配置”添加 LLM（API 地址、密钥、模型名）。
2. 在“项目”中导入一个 GitHub 仓库。
3. 创建审计任务，选择审计模式（推荐“智能审计”）。
4. 实时观察审计过程，完成后在“漏洞管理”查看并导出 CVE 报告。