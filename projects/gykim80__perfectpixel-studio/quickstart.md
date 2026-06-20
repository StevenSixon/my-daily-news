## 环境准备
- 安装 Go 1.25+
- 安装 Node.js 18+
- 安装 Wails CLI v2：`go install github.com/wailsapp/wails/v2/cmd/wails@latest`
- 检查平台依赖：`wails doctor`
- （可选）准备至少一个 AI 提供方的 API 密钥

## 克隆并运行
```bash
git clone https://github.com/gykim80/perfectpixel-studio
cd perfectpixel-studio
go mod tidy
cd frontend && npm install && cd ..
wails dev
```

## 最小可用示例
1. 启动应用后在设置中选择 AI 提供方，并输入 API 密钥
2. 在角色描述框输入“fire mage with red robe”，选择风格（pixel art）
3. 点击生成基础角色
4. 在动作列表中选择“walk”，点击生成动画
5. 查看生成的精灵集，导出为 sprite sheet 或 GIF