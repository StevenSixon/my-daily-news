## 安装
```bash
npm install -g klaatcode
```
或使用 curl 一键脚本：
```bash
curl -fsSL https://klaatai.com/api/install | bash
```

## 快速开始
1. 登录账号：
```bash
klaatcode login
```
2. 在项目目录启动：
```bash
klaatcode
```
或指定项目路径：
```bash
klaatcode ~/projects/my-app
```
3. 无头模式执行任务：
```bash
klaatcode run "Fix all TS errors"
```

## 依赖前提
- Node.js ≥18 或 Bun ≥1（编译安装无需运行时）
- KlaatAI 账号（登录即绑定，无需管理 API 密钥）