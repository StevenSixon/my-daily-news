## 前提
- **硬件**：x86_64 服务器（必须支持 KVM）
- **系统**：Linux（推荐 Ubuntu 20.04+ 或 CentOS 8+）
- **网络**：可访问外网拉取组件

## 安装
1. 准备一台满足 KVM 的 Linux 主机（裸金属或云 VM，推荐 PVM）
2. 按照官方部署文档选择路径：
   - [PVM 云 VM 一键部署](https://cubesandbox.com/docs/guide/pvm-deploy)
   - [裸金属手动部署](https://cubesandbox.com/docs/guide/bare-metal-deploy)
3. 运行提供的安装脚本，自动完成所有依赖和服务配置
4. 部署完成后可通过 Web 控制台（默认端口 12088）管理节点和模板

## 最小可用示例
安装后，通过 Python SDK 快速体验（需先创建模板）：
```bash
pip install cubesandbox
```

创建沙箱并执行代码（需设置 `CUBESANDBOX_API_URL` 为你的服务地址）：
```python
from cubesandbox import Sandbox

sandbox = Sandbox.create(template="代码解释器模板")
result = sandbox.run_code("print('Hello, AI Agent!')")
print(result.logs)
sandbox.kill()
```

更多示例和集成（如 OpenAI Agents、LangChain）见 [examples 目录](https://github.com/tencentcloud/CubeSandbox/tree/main/examples)。

> 注意：具体模板名称、API 地址等需根据实际部署调整，详细教程请参阅 [快速开始](https://cubesandbox.com/docs/guide/quickstart)。