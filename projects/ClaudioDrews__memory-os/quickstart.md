## 安装
### 前提
- Hermes Agent（需先安装并运行）
- Docker 及 docker-compose
- Python 3.11+
- curl

### 一键安装
```bash
curl -sSL https://raw.githubusercontent.com/ClaudioDrews/memory-os/main/setup.sh | bash
```
该命令将自动完成：服务启动（Qdrant、Redis、ARQ）、数据库初始化、插件安装、环境配置。

### 手动安装（故障排查用）
详细步骤见 `setup/install.md`。

## 最小可用示例
1. 执行一键安装
2. 启动 Hermes Agent，Memory OS 将自动注入系统提示及记忆上下文
3. 在对话中自然提及项目信息、决策等，系统会自动捕获并索引
4. 下次会话即可观察到智能体主动引用历史事实

## 依赖核心
- 计算资源：支持 Docker 运行的标准机器（真实环境验证包括中低配机器）
- 持久化：会创建 SQLite 数据库文件和 Qdrant 数据卷