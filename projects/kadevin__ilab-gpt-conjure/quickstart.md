## 安装与启动

1. 下载对应平台的一键 zip（见 Releases），解压到普通目录。
2. Windows 双击 `Start WebUI Portable.bat`；macOS 双击 `Start WebUI Portable.command`（若被拦截，右键选择 Open 或执行 `xattr -dr com.apple.quarantine 目录`）。
3. 浏览器自动打开 `http://127.0.0.1:8787`，进入设置页面配置 OpenAI 兼容 API（Base URL、Key、模型名称）。
4. 添加上传参考图，编写提示词，选择生成参数后开始生成。

## 源码安装

```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-webui.txt
.venv/bin/python -m uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787
```

## 最小 CLI 示例

```bash
.venv/bin/python -m codex_image generate --prompt "A clean product photo" --out output/mug.png
```

*前提*：需要 Python 3.11+，API 模式需具备有效的 OpenAI 兼容 API key。