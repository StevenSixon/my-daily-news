## 安装
### 方式一：一行命令部署
```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml \
  | docker compose -f - up -d
```
Windows PowerShell:
```bash
curl.exe -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml | docker compose -f - up -d
```

### 方式二：源码部署（开发）
```bash
git clone https://github.com/larlarua/AutoCVE.git
cd AutoCVE
docker compose up -d --build
```

### 依赖前提
- Docker Engine 与 Docker Compose
- 有效的 LLM API 密钥（需在平台内配置模型）
- 至少 4 GB 可用内存（推荐 8 GB）

### 最小可用示例
1. 访问 http://localhost:3000 打开前端。
2. 在“模型配置”页添加你的 LLM 提供商（支持 OpenAI 式接口）。
3. 导入一个 GitHub 仓库（或使用内置示例项目）。
4. 选择一种审计模式（如“智能审计”），创建任务，Agent 将自动执行。
5. 在“漏洞管理”查看发现的漏洞，并导出 CVE 报告。

如需深入使用一键 CVE，参考用户手册配置 GitHub Token 和筛选规则。