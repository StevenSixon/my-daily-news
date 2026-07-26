### 环境要求
- 操作系统：macOS / Linux / Windows
- 无需预装 Python，安装脚本将自动使用 uv 创建隔离虚拟环境。

### 安装
```bash
# macOS/Linux 一键安装
curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash

# Windows PowerShell
irm https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.ps1 | iex

# 也可通过 PyPI 安装（需自行管理 Python）
pip install octop
```

### 初始化并运行
```bash
octop init        # 创建管理员账户和数据库
octop run         # 启动服务（默认 http://127.0.0.1:8088）
```
打开浏览器访问 `http://127.0.0.1:8088`，使用 `admin` / `octop` 登录（请立即修改密码）。

### 最小可用示例
1. 在 Web 仪表板配置 LLM 提供商（OpenAI 兼容接口或 Ollama 等）。
2. 创建新的智能体，选择预置专家模板。
3. 通过聊天界面发送消息，尝试 `@agent` 切换或 `/compact` 压缩上下文。

### Docker 部署
```bash
docker compose -f docker/docker-compose.yml up -d
```
数据目录映射至宿主机 `octop-data` 卷。