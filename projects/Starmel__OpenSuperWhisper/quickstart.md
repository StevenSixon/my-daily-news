## 安装
### 通过 Homebrew（推荐）
```bash
brew update
brew install opensuperwhisper
```

### 手动安装
1. 从 [GitHub Releases](https://github.com/Starmel/OpenSuperWhisper/releases) 下载 `OpenSuperWhisper.dmg`
2. 打开 DMG，将应用拖入 Applications
3. 首次启动需授予麦克风与辅助功能权限

## 最小可用示例
1. 启动后菜单栏出现图标，点击设置快捷键（如左 Cmd 单键长按录音）
2. 在设置中下载一个 Whisper 模型（如 tiny 或 base）
3. 按住设置的快捷键说话，松开后自动转写并粘贴到前台输入框

## 依赖前提
- **硬件**：Apple Silicon Mac（M系列芯片）
- **系统**：macOS 14.0 (Sonoma) 或更新
- **模型**：应用内可下载，无需手动配置（首次启动可自动复制默认模型）