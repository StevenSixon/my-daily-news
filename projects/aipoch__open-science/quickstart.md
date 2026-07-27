## 安装
从 [GitHub Releases](https://github.com/aipoch/open-science/releases/latest) 下载对应平台的安装包 (macOS Apple Silicon/Intel, Windows x64, Linux x64 AppImage/Deb)，直接安装。
⚠️ 安全：若出现未认证开发者警告，确认包来自官方后放行。

## 最小可用示例
1. 首次启动完成环境检测（自动检查兼容性、存储、可选 Claude 运行时和 Python Notebook 支持）  
2. 配置模型：选择内置提供商、自定义兼容网关，或使用 Claude/ChatGPT 订阅登录  
3. 创建新项目 → 新建会话 → 用自然语言描述研究任务，附加数据文件  
4. 发送任务，审批敏感操作（文件编辑、网络调用等）  
5. 在预览面板查看生成的报告、表格、图表，后续会话用 `@` 引用文件，`/` 选择技能

## 依赖前提
- 操作系统：macOS, Windows, Linux  
- 离线模型需网络连接（使用云 API）  
- 可选 Python 安装（用于 Notebook 内核，非必选）  
- 模型凭证：API Key 或支持的订阅登录方式