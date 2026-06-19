### 前提依赖
* Node.js ≥20
* pnpm ≥9
* ffmpeg（任意近期版本）
* Playwright 的 Chromium 浏览器（`npx playwright install chromium`）

### 安装与启动
```bash
git clone <repo-url>
cd html-video
pnpm install
pnpm -r build
```

### 本地 Studio
```bash
node packages/cli/dist/bin.js studio
# 浏览器打开 http://127.0.0.1:3071
# 在界面中挑选模板、粘贴链接或描述视频，与代理交互，导出 MP4
```

### CLI 最小示例
```bash
# 检测已安装的代理和引擎状态
node packages/cli/dist/bin.js doctor
# 其他工具脚本见 packages/cli 下的命令
```
