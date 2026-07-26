## 安装
macOS/Linux：
```bash
curl -fsSL https://jcode.sh/install | bash
```
Windows 11（PowerShell）：
```powershell
irm https://jcode.sh/install.ps1 | iex
```
其他方式包括 Homebrew、源码编译，详见 [官方文档](https://jcode.sh/docs)。

## 最小可用示例
安装后运行 `jcode` 进入交互式 TUI，首次启动按提示配置 LLM API 密钥。直接输入自然语言任务即可开始编码交互。多会话可通过快捷键创建新标签或新窗口。

## 依赖前提
- 系统无特殊依赖，二进制自带所有运行时
- 如需本地嵌入功能可能需要额外库（但默认开启）
- 需要有效的 OpenAI / Claude 等 API 密钥