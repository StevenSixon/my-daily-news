## 安装
```bash
# 在项目根目录运行（需 Node.js ≥ 22, git, bash；Windows 用 Git Bash 或 WSL）
curl -fsSL https://raw.githubusercontent.com/withkynam/vibecode-pro-max-kit/main/install.sh | bash
```
安装完成后按输出提示操作：新项目会提示运行 `vc-setup`，旧项目会引导更新。

## 最小可用示例
1. 在项目根目录安装后，打开 AI 编码代理（如 Claude Code）
2. 输入 `Run vc-setup` 让代理扫描项目并初始化知识库
3. 然后通过 `/goal` 指令描述你的需求，例如：
   ````
   /goal Add user authentication with login and registration pages
   ````
代理将自动进入计划流程，依次完成研究、规格、设计、验证、编码和自我检查。

## 依赖前提
- Node.js ≥ 22
- git
- bash（macOS/Linux 自带；Windows 使用 Git Bash 或 WSL；Alpine 需 `apk add bash`）