## 安装
- **Windows**：从 [Releases](https://github.com/Zackriya-Solutions/meeting-minutes/releases/latest) 下载 `x64-setup.exe` 安装。
- **macOS**：下载 `meetily_0.4.0_aarch64.dmg`，拖入 Applications 即可。
- **Linux**：需从源码构建，参考 [docs/building_in_linux.md](docs/building_in_linux.md)。

## 快速体验
1. 启动 Meetily，系统托盘会出现图标。
2. 点击开始新的会议录制，选择音频源（麦克风+系统音频）。
3. 开始说话或播放音频，右侧可看到实时转录文字。
4. 结束录制后，点击生成摘要，本地 Ollama 或配置的 AI 接口将返回结构化总结。

## 依赖前提
- 无需安装 Python 或外部运行时，软件为独立可执行文件。
- 若使用本地摘要，需提前安装 [Ollama](https://ollama.com/) 并拉取模型（如 `llama3`、`mistral`）。
- GPU 加速自动启用，若有 NVIDIA/CUDA、AMD Vulkan 或 Apple Silicon 会透明使用。