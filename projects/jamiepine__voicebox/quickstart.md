## 安装
1. 根据平台下载安装包（macOS Apple Silicon 推荐）：  
   - macOS: 下载 DMG 安装  
   - Windows: 下载 MSI 安装  
   - Docker: `docker compose up`  
2. 首次启动会引导授予系统权限（macOS 需开启辅助功能和输入监控）。

## 最小可用示例
1. **克隆声音**：打开Voicebox，点击“New Voice Profile”，上传一段3~30秒的清晰人声样本，引擎自动克隆。  
2. **生成语音**：在输入框输入文字，选择刚创建的声音和引擎，点击生成，播放结果。  
3. **试试全局听写**：按住默认热键（macOS: 右Cmd+右Option）不放，说话，松开后文字直接粘贴到当前焦点输入框。

**依赖前提**：  
- 操作系统需支持 GPU 加速（Apple Silicon 或 NVIDIA GPU 推荐）以保证低延迟。  
- 若用 Docker，需 nvidia-docker（GPU）或 CPU 后端。  
- 模型下载需网络，后续完全离线使用。