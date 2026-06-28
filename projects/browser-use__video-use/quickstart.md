## 快速安装
```bash
# 克隆并链接到代理技能目录
git clone https://github.com/browser-use/video-use ~/Developer/video-use
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use

# 安装依赖
cd ~/Developer/video-use
uv sync
brew install ffmpeg
brew install yt-dlp   # 可选

# 配置 API 密钥
cp .env.example .env
# 编辑 .env 填入 ELEVENLABS_API_KEY=...
```

## 最小使用示例
1. 将视频文件放入一个文件夹，例如 `~/Videos/my_shoot/`。
2. 在终端进入该目录并启动 Claude Code：
```bash
cd ~/Videos/my_shoot
claude
```
3. 在会话中输入：
> edit these into a launch video
4. 代理会列出素材、提出策略，待你确认后自动剪辑。
5. 最终输出在 `<videos_dir>/edit/final.mp4`。

依赖前提：Python 3.10+，ffmpeg，ElevenLabs API 账号。若需动画功能需额外安装 Remotion/Manim。