### 安装
无需 Node.js：
- macOS/Linux:
```sh
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```
- Windows (PowerShell):
```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```
Windows 需提前安装 Git for Windows（自定义路径可通过 `KIMI_SHELL_PATH` 指定）。

### 最小可用
```sh
cd your-project
kimi
```
首次运行会进入 TUI，输入 `/login` 选择 OAuth 或 Moonshot AI 平台 API 密钥登录。之后可直接下达任务：
```
Take a look at this project and explain its main directories.
```
代理会自主浏览文件并解释。想退出按 `Ctrl+C`。

### 编辑器集成（可选）
Zed 用户可在 `~/.config/zed/settings.json` 添加：
```json
{
  "agent_servers": {
    "Kimi Code CLI": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```
然后在 Zed Agent 面板新建会话即可使用。