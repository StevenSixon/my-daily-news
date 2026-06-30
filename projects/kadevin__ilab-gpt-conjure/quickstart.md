## 安装
**方式一：免安装一键包（推荐）**
1. 前往 [Releases](https://github.com/kadevin/ilab-gpt-conjure/releases) 下载对应平台（Windows x64 / macOS arm64 / macOS x64）的 portable zip。
2. 解压到用户目录，双击 `Start WebUI Portable.bat`（Win）或 `Start WebUI Portable.command`（Mac）。
3. 若浏览器未自动打开，手动访问 `http://127.0.0.1:8787/`。

**方式二：从源码运行**
```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/pip install -r requirements-webui.txt
.venv/bin/python -m uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787 --no-access-log
```

## 最小可用示例
1. 打开 WebUI 后，进入系统设置（右上角齿轮），在 API 供应商卡中添加你的 OpenAI API Key 和 Base URL。
2. 选择“API”认证模式，确保模型为 GPT-image-2。
3. 在主界面提示词框输入：“A cute cat wearing a wizard hat, digital art”。
4. 点击“生成”，任务将进入左侧队列，生成完成后在预览区查看结果，可下载或保存至历史库。

**CLI 快速测试**：
```bash
.venv/bin/python -m codex_image generate --prompt "A clean product photo of a ceramic mug" --out mug.png
```

## 依赖前提
- 一键包自带 Python 3.11+ 和所有依赖，无需额外安装。
- 源码部署需要 Python 3.11+ 和 `pip install -r requirements-webui.txt`。
- 若修改前端 TypeScript/CSS，需安装 Node.js 并执行 `npm install`，构建后静态资源输出到 `codex_image/webui/static/`。
- macOS 用户首次启动时若被拦截，执行 `xattr -dr com.apple.quarantine /path/to/ilab-gpt-conjure_macos_portable_xxx` 或右键启动脚本选择 Open。