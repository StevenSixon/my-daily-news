## 免安装一键包（推荐）
1. 从 [Releases](https://github.com/kadevin/ilab-gpt-conjure/releases) 下载对应平台的 zip（Windows x64 / macOS ARM / macOS Intel）。
2. 解压到普通用户目录。
3. Windows 双击 `Start WebUI Portable.bat`；macOS 双击 `Start WebUI Portable.command`（如被拦截，右键选择 Open）。
4. 浏览器打开 `http://127.0.0.1:8787/`。
5. 在设置中配置 OpenAI 兼容 API 供应商（Base URL、Key、模型），或使用本机 Codex OAuth（高级模式）。

## 源码安装
前提：Python 3.11+、Git。
```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-webui.txt
.venv/bin/python -m uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787 --no-access-log
```

## CLI 最小示例
```bash
.venv/bin/python -m codex_image generate --prompt "A clean product photo of a ceramic mug" --out output/mug.png
```