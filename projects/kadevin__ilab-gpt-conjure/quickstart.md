## 安装与快速上手

### 免安装一键包（推荐）
1. 从 [Releases](https://github.com/kadevin/ilab-gpt-conjure/releases) 下载对应系统的一键包：
   - Windows x64: `ilab-gpt-conjure_windows_portable_x64_0.5.1.zip`
   - macOS Apple Silicon: `ilab-gpt-conjure_macos_portable_arm64_0.5.1.zip`
   - macOS Intel: `ilab-gpt-conjure_macos_portable_x64_0.5.1.zip`
2. 解压到普通用户目录。
3. Windows 双击 `Start WebUI Portable.bat`；macOS 双击 `Start WebUI Portable.command`（如被拦截，右键 Open 或移除 quarantine 属性）。
4. 浏览器打开 `http://127.0.0.1:8787/`。

### 手动安装（需要 Python 3.11+）
```bash
git clone https://github.com/kadevin/ilab-gpt-conjure.git
cd ilab-gpt-conjure
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-webui.txt
.venv/bin/python -m uvicorn codex_image.webui.app:app --host 127.0.0.1 --port 8787 --no-access-log
```

### 最小可用示例
- 启动 WebUI 后，在顶部认证来源选择 `API`（推荐），点击右上角进入系统设置，添加你的 OpenAI 兼容 API 供应商（Base URL、Key、模型名）。
- 输入提示词，如 “A clean product photo of a ceramic mug”，按需添加参考图或颜色 chip，点击“开始生成”。
- 通过 CLI 生成：
```bash
.venv/bin/python -m codex_image generate --prompt "A cute cat" --out cat.png
```

依赖前提：无额外系统依赖，Python 环境下仅需 `requirements-webui.txt` 中的包；若修改前端则需 Node.js 和环境。