## 安装
- **一行命令（无需 Node）**：`curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh`（macOS/Linux/Windows 预编译二进制）
- **npm**：`npx dao-code`（零安装试用）或 `npm i -g dao-code`（命令名 `dao`）
- **源码构建**：`git clone` 后 `npm install && npm run build && npm link`

**前置条件**：Node ≥20（npm 方式）；DeepSeek API key（从 platform.deepseek.com/api_keys 获取）

## 最小可用示例
```bash
# 首次运行，按提示输入 API key
dao
# 或携带 key 单次执行
dao --api-key sk-xxx --provider deepseek "告诉我一个笑话"

# 交互模式：进入后直接提问
dao
> 给 src/utils.ts 的 formatDate 函数添加时区支持

# 单次执行模式
dao "把 package.json 里的版本升级到 2.0.0"

# 查看成本与缓存命中率
/cost
```

## 关键快捷键/命令
- `/init`：扫描仓库生成 DAO.md 项目说明
- `/model [id]`：切换模型（无参在 pro/flash 间切换）
- `/mode [x]`：切换权限模式（default/acceptEdits/auto/plan）
- `Ctrl+O`：展开/折叠完整输出
- `ESC`：中断当前 turn
- `--yolo`：启动后自动批准所有操作