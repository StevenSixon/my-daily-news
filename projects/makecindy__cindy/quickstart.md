## 前提
- Node.js 22.x
- pnpm 10.x（v11 未支持）
- Git LFS
- 建议对 GitHub 子模块和 pnpm monorepo 有基本了解

## 安装
```bash
git clone https://github.com/makecindy/cindy.git
cd cindy
git submodule update --init --recursive cindy-protocol
git lfs pull
pnpm install
```

## 最小运行
启动桌面端开发环境（远程模式，需 Cindy 账号）：
```bash
# 中国大陆账户
pnpm restart:desktop:remote --region=cn
# 全球账户
pnpm restart:desktop:remote --region=global
```
启动后客户端会连接官方云服务，利用现有登录状态继续开发。

若不想登录，可在登录界面选择“Local mode”仅使用本地代理（无服务端功能）。移动端及详细验证流程见 `CONTRIBUTING.en.md`。