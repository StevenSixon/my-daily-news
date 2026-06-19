## 快速开始
### 前提
- Python 3.10+
- FFmpeg (`brew install ffmpeg` 或 `sudo apt install ffmpeg`)
- Node.js 18+
- 一个 AI 编程助手（Claude Code、Cursor、Copilot、Windsurf 或 Codex）

### 安装与运行
```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```
在 AI 编程助手中打开项目文件夹，直接下达指令，例如：
```text
"Make a 60-second animated explainer about how neural networks learn"
```
系统会自动执行调研、脚本、资产生成、编辑和渲染。如需更丰富的工具，可在 `.env` 中添加 API 密钥（可选），支持 OpenAI、Fal、ElevenLabs 等。

### 零 API 密钥方案
不添加任何密钥，系统将自动使用 Piper TTS（免费离线语音合成）、Pexels/Unsplash 等免费素材库以及 Remotion 或 HyperFrames 动画引擎，完成从图像生成到字幕合成的全流程。