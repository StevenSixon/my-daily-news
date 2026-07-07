## 安装
```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
# Windows (PowerShell)
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
# 或通过包管理器
brew install officecli        # macOS
npm install -g @officecli/officecli
```

## 最小可用示例
```bash
# 创建空白 PPT
officecli create deck.pptx

# 开启实时预览（浏览器打开 http://localhost:26315）
officecli watch deck.pptx

# 在另一个终端添加幻灯片，浏览器自动刷新
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

## 依赖前提
无。单二进制文件，无需安装 Office、Python 或任何运行时。