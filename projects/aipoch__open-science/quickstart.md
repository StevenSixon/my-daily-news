## 安装
1. 访问 [最新Release](https://github.com/aipoch/open-science/releases/latest)，根据系统下载对应安装包：
   - macOS (Apple Silicon / Intel) 选择对应DMG
   - Windows 选择 x64 安装程序
   - Linux 选择 x64 AppImage 或 deb 包
2. 安装并首次启动，完成两个引导步骤：
   - **环境检测**：自动检查兼容性、存储、网络、Claude运行时（可应用内安装）及Python支持（可选）
   - **模型提供方**：选择内置厂商、Anthropic兼容网关、或复用Claude/ChatGPT订阅

## 最小可用示例
1. 点击 **New project**，命名（如“metabolite-analysis”）
2. 打开一个会话，用自然语言描述目标，例如：  
   “读取附件中CSV数据，执行差异代谢物筛选，生成火山图和表格。”
3. 附加上传CSV文件，从已验证模型列表中选择一个模型，选择批准模式（严格/自动等）
4. 发送任务，观察代理逐步读取文件、运行代码、调用工具（如需要可手动批准敏感操作）
5. 在预览面板查看生成的图表和表格，所有产物自动保存在项目文件库

## 依赖前提
- 操作系统满足要求，无需预先安装Node.js或Python（应用内可提供托管运行时）
- 模型调用需要自行提供API密钥或订阅凭据
- 若想从源码构建，需Node.js 20+ 和对应平台的构建工具链（见仓库Building From Source说明）