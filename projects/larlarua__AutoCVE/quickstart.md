## 前提
- 安装 Docker 和 Docker Compose
- 准备一个兼容的 LLM API 地址与密钥（OpenAI 格式或兼容接口）

## 一行命令部署
```bash
# Linux/macOS/Git Bash
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml \
  | docker compose -f - up -d
```
```bash
# Windows PowerShell / CMD
curl.exe -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml | docker compose -f - up -d
```

## 访问服务
- 前端界面：http://localhost:3000
- 后端 API：http://localhost:8000
- Swagger 文档：http://localhost:8000/docs
- 数据库管理：http://localhost:8080

## 最小可用流程
1. 在前端配置模型（API 地址、密钥等）
2. 导入一个 GitHub 仓库
3. 创建审计任务（选择“一键 CVE”或手动选择模式）
4. 观察实时审计过程与阶段输出
5. 在漏洞管理中查看/导出 CVE 报告