## 安装
从 App Store 下载 Hermex（https://apps.apple.com/app/hermex/id6767006319），或从源码构建（需 Xcode 26+，编译 scheme `HermesMobile`）。

## 前提
1. 一台运行 hermes-webui 的机器（Python 3.11+，macOS/Linux/WSL2）
2. 服务端设置密码（环境变量 `HERMES_WEBUI_PASSWORD`）
3. 使服务器可从 iPhone 访问（推荐 Cloudflare Tunnel 或反向代理获取 HTTPS；也可用 Tailscale 组成虚拟局域网）

## 最小连接示例
- **HTTPS 推荐**：建立隧道后获得公开域名（如 `https://hermes.yourdomain.com`），在 Hermex 中输入该 URL 和密码即可。
- **Tailscale**：在服务器上绑定所有接口启动，手机安装 Tailscale 加入同一网络，连接时输入 `http://<tailscale-ip>:8787`（允许该范围的 HTTP），输入密码。
- **模拟器测试**：Mac 本地运行服务器后，在 Xcode 模拟器中使用 `http://localhost:8787` 连接。

## 故障排查
检查服务器是否存活：`curl https://<your-server>/health` 应返回成功；确认隧道或 Tailscale 路由正常；核对密码正确。