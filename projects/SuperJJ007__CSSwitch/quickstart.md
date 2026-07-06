### 安装
1. 从 [GitHub Releases](https://github.com/SuperJJ007/CSSwitch/releases/latest) 下载 `CSSwitch_*.dmg`
2. 将 CSSwitch 拖入“应用程序”文件夹
3. 首次打开若被 Gatekeeper 拦截，请右键点击应用并选择“打开”
4. 确保已安装 Claude Science 和 Python3

### 最小可用示例
1. 启动 CSSwitch，保持“第三方模型”模式
2. 点击“+ 新建”，选择 provider（如 DeepSeek）
3. 填入 API Key、模型名（如 `deepseek-chat`）
4. 点击“创建”，然后在列表中将该配置“设为当前”
5. 点击“一键开始”，CSSwitch 会自动启动隔离的 Claude Science
6. 在 Science 中提问，推理请求将通过本地代理发送到你配置的 API

### 依赖前提
- macOS Apple Silicon 设备
- 已安装 [Claude Science](https://claude.com)
- 系统中存在 `python3`
- 拥有至少一个第三方模型 API Key