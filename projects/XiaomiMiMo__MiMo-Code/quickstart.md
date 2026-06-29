### 安装
```bash
# 一键安装（macOS/Linux）
curl -fsSL https://mimo.xiaomi.com/install | bash

# 或通过 npm
npm install -g @mimo-ai/cli
```

### 首次运行
```bash
mimo
```
按提示选择配置：
- **MiMo Auto**（限时免费，零配置）
- Xiaomi MiMo 平台（OAuth 登录）
- 从 Claude Code 迁移认证
- 自定义 OpenAI 兼容 API 提供商

### 依赖前提
- **系统要求**：终端环境（macOS/Linux/WSL/Windows）。
- **语音输入（可选）**：需安装 `sox`（`brew install sox` / `apt install sox`），且需要 MiMo 账户。
- **WSL 用户**：若遇剪贴板问题，安装 `xsel`。
- **Windows 非 UTF-8 系统**：CJK 字符可能乱码，需在系统设置中启用 UTF-8 支持。

### 最小使用示例
进入交互后，直接在提示符与 AI 对话，或使用 `/build`、`/plan`、`/compose` 切换代理模式。例如：
```
> 在 src/utils 下创建日期格式化工具函数并编写测试
```
MiMoCode 将读取项目上下文、生成代码、运行测试，并在完成后更新检查点。