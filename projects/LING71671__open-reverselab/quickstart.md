**前提**：Git、Python 3.8+、PowerShell 5.1+（Windows）或 pwsh（跨平台）。可选逆向工具需手动安装（Ghidra、Frida、Android SDK等）。

**安装**
```bash
git clone https://github.com/LING71671/open-reverselab.git
cd open-reverselab
.\scripts\misc\bootstrap.ps1              # 核心脚本包装，无下载
.\scripts\misc\install_tools.ps1 -Common   # Ghidra等公共依赖
.\scripts\misc\install_tools.ps1 -CTF      # Web工具
.\scripts\misc\install_tools.ps1 -Android  # APK工具
.\scripts\misc\install_tools.ps1 -Windows  # PE工具
```

**验证环境**
```bash
python scripts/misc/lab_healthcheck.py
python scripts/misc/ai_toolcheck.py --board misc
```

**最小使用示例**
1. 在你的AI编码助手（Claude Code、支持MCP的IDE）中打开此项目。
2. 自动加载上下文链后，直接提问：
   - “分析这个APK：app-debug.apk，查找硬编码密钥”
   - Agent 会识别 `android` 板，调用 `kb_router` 查找相关攻击链，再通过 MCP 执行 `android_crypto_unpack_recipe` 等工具。
3. 产出文件将自动落入 `exports/`、`reports/` 等约定目录。

**注意**：首次运行需确保 AI 工具已配置 MCP 服务器，可搭配 [codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) 一键生成项目级 `.codex/` 环境。