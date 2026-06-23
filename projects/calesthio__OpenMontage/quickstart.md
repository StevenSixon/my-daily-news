### 前提条件
- Python 3.10+
- FFmpeg
- Node.js 18+
- 任一 AI 编程助手（Claude Code、Cursor 等）

### 安装
```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```
若没有 `make`：
```bash
pip install -r requirements.txt
cd remotion-composer && npm install && cd ..
pip install piper-tts
cp .env.example .env
```

### 最小示例
在 AI 编程助手中打开项目，输入：
```text
"Make a 60-second animated explainer about how neural networks learn"
```
代理将自动研究、生成图像、合成视频。无需 API 密钥。

### 使用参考视频
```text
"Here's a YouTube Short I love. Make me something like this, but about quantum computing."
```