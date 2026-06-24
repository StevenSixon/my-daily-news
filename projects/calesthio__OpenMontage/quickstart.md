## 安装
```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```
若无 make，可手动：
```bash
pip install -r requirements.txt
cd remotion-composer && npm install && cd ..
pip install piper-tts
cp .env.example .env
```
可选：添加 API 密钥到 .env（FAL_KEY, OPENAI_API_KEY 等），或配置本地 GPU (`make install-gpu`)。

## 最小示例
在 AI 编程助手（Claude Code/Cursor 等）中打开项目，输入：
```text
"Make a 60-second animated explainer about how neural networks learn"
```
Agent 会自动选择管道、生成素材、合成并渲染视频。若需使用免费真实素材制作纪录片风格：
```text
"Make a 75-second documentary montage about city life in the rain. Use real footage only, no narration, elegiac tone, with music."
```
无需任何付费 API 密钥即可运行，首次会下载 Piper 语音模型等依赖。