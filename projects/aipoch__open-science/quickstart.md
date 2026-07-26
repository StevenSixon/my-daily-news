## 安装
前往 GitHub [latest release](https://github.com/aipoch/open-science/releases/latest) 下载对应平台安装包：
- macOS：Apple Silicon 或 Intel 的 DMG
- Windows：x64 安装器
- Linux：x64 AppImage 或 Deb 包

下载后直接安装。首次启动会自动引导环境检查（兼容性、凭证存储、Claude 运行时）和模型供应商配置（API Key / 订阅 token / ChatGPT 登录）。可选启用 Python Notebook 支持。

## 最小可用示例
1. 创建新项目，命名并描述。
2. 开启会话，用自然语言描述研究问题、所需输出，可附加数据文件。
3. 选择模型和审批模式，发送任务。
4. 观察 agent 工具调用，批准敏感操作，最终在预览区查看生成的报告/图表。

## 前提
- 操作系统：macOS, Windows, Linux (x64)
- 网络：用于模型 API 调用和数据连接器（可离线使用部分本地功能）。
- 可选：Python 环境用于 Notebook 内核（应用可选自动安装 micromamba 管理）。