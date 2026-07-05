## 快速上手
### 依赖前提
- Docker 和 Docker Compose 已安装
- 可访问的 LLM 服务（如 OpenAI API 密钥或兼容 API 端点）

### 一行命令部署
```bash
# Linux / macOS / Git Bash
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.4/docker-compose.prod.yml \
  | docker compose -f - up -d
```
Windows 用户请使用 `curl.exe` 命令。

### 配置与使用
1. 启动后访问前端 http://localhost:3000
2. 进入系统设置，填入 LLM 配置信息（API 地址、模型名称、密钥等）
3. 导入目标项目（上传 ZIP 源码包或填写 Git 仓库地址）
4. 创建审计任务，选择“智能审计”模式进行 CVE 挖掘
5. 在审计页面实时跟踪 Agent 动态，完成后在漏洞管理查看结果并导出 CVE 报告

### 源码部署（开发用）
```bash
git clone https://github.com/larlarua/AutoCVE.git
cd AutoCVE
docker compose up -d --build
```
服务列表：前端 3000，后端 8000，API 文档 8000/docs，数据库管理 8080