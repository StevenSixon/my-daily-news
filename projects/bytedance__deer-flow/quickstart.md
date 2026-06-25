## 环境要求
- Python 3.12+
- Node.js 22+
- Docker（推荐用于沙盒隔离）
- 至少 4 vCPU、8 GB 内存（本地评估）

## 安装与运行
```bash
# 1. 克隆仓库
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow

# 2. 执行设置向导（生成 .env 和 config.yaml）
make setup

# 3. 验证配置
make doctor

# 4. 使用 Docker 开发模式启动（热重载）
make docker-init   # 拉取沙盒镜像（仅首次）
make docker-start  # 启动服务，访问 http://localhost:2026
```

## 最小可用示例
1. 浏览器打开 `http://localhost:2026`，在聊天界面选择模型。
2. 输入一个多步研究任务（例如“调研 Mistral 和 Llama 3 的性能对比，生成报告”）。
3. 观察子代理调度、搜索工具调用、沙盒内代码执行，最终获得完整报告。

详细配置（如切换模型、添加搜索工具）参见 `config.example.yaml` 或重新运行 `make setup`。