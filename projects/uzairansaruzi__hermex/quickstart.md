## 前提
- 一台安装了 [hermes-webui](https://github.com/nesquena/hermes-webui) 的服务器（Python 3.11+，设置 `HERMES_WEBUI_PASSWORD`）
- 服务器需通过 HTTPS 隧道/反向代理 或 Tailscale 使 iPhone 可达
- iOS 18+ 设备或模拟器

## 安装
从 [App Store](https://apps.apple.com/app/hermex/id6767006319) 下载 Hermex（推荐），或从源代码构建：
```zsh
git clone https://github.com/uzairansaruzi/hermex.git
cd hermex
xcodebuild -project HermesMobile.xcodeproj -scheme HermesMobile -destination 'platform=iOS Simulator,name=iPhone 17' build
```

## 最小可用示例
1. 在服务器启动 hermes-webui，确认 `/health` 可访问（`curl https://<你的域名>/health`）。
2. 打开 Hermex，输入服务器 URL（如 `https://hermes.yourdomain.com`）及密码。
3. 连接成功后，进入聊天界面，选择模型，发送一条消息，代理会实时流式回复。