### 前提依赖
- Node.js 22+
- FFmpeg

### 手动启动
```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview   # 浏览模式，实时预览
npx hyperframes render    # 渲染为 MP4
```

### 搭配 AI 代理
```bash
npx skills add heygen-com/hyperframes
```
然后向代理（如 Claude Code、Cursor）描述视频需求，它会自动使用 `/hyperframes` 技能完成制作。