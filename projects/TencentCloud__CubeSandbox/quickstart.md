## 环境要求
- x86_64 Linux（Ubuntu 20.04+ 推荐）
- KVM 支持（需开启硬件虚拟化）

## 安装
一键脚本部署，详见 [PVM 部署指南](https://github.com/tencentcloud/CubeSandbox/blob/main/docs/guide/pvm-deploy.md) 或 [裸金属指南](https://github.com/tencentcloud/CubeSandbox/blob/main/docs/guide/bare-metal-deploy.md)。安装后 Web 控制台访问 `:12088`。

## 最小示例
1. 创建模板：`cubecli template create my-template`
2. 启动沙箱：`cubecli sandbox create --template my-template`
3. 使用 E2B SDK 连接（需设置环境变量 `E2B_API_URL=http://localhost:49982`）：
```python
from e2b import Sandbox
sandbox = Sandbox()
sandbox.run_code("print('Hello')")
```

## 常用命令
- `cubecli logs` 查看容器日志
- `cubecli version` 查看组件版本矩阵
- Web UI 管理模板、沙箱、节点

详细示例参见 examples/ 目录。