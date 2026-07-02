**前提**：Python 3.11+，git，或直接下载标准包。

**安装（源码）**
```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-webui.txt
```

**启动 WebUI**
- macOS: `open "Start WebUI.command"` 或手动 `uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787`
- Windows: 双击 `Start WebUI.bat`

访问 `http://127.0.0.1:8787/`。

**最小示例（CLI）**
```bash
.venv/bin/python -m codex_image generate --prompt "一只戴着帽子的猫" --out output.png
```

**使用标准包（推荐新手）**
1. 从 [Release 页面](https://github.com/kadevin/ilab-gpt-conjure/releases/tag/v0.5.5) 下载对应平台的 DMG 或 ZIP。
2. macOS 将 .app 拖入 Applications；Windows 解压后双击 exe。
3. 首次启动配置 API 供应商（OpenAI‑compatible 模式），输入 Base URL 和 API Key。
4. 通过 `@` 图库 Chip、`~` 提示词片段快速构建提示词，设置参数后点击生成。

**注意**：默认推荐 API 模式。若使用高级 OAuth 模式，需本机已登录 ChatGPT，风险自负。