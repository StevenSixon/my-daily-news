## 安装
### 方式一：一键安装（推荐）
```bash
curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh
```
或从[Releases](https://github.com/tigicion/dao-code/releases)下载对应平台的二进制文件，Unix下添加执行权限后直接运行。

### 方式二：使用npx（需Node >=20）
```bash
npx dao-code
```

### 方式三：全局安装
```bash
npm i -g dao-code
```

## 初始配置
1. 获取DeepSeek API key：https://platform.deepseek.com/api_keys
2. 运行`dao`，首次启动时会引导输入key并自动保存至`~/.dao/config.json`。
   也可手动设置环境变量：
   ```bash
   export DEEPSEEK_API_KEY=sk-...
   ```

## 最小可用示例
```bash
# 交互模式（直接启动对话）
dao

# 一次性任务模式
dao "把我src/utils.ts里的formatDate函数改成支持时区"

# 自动批准模式（跳过询问）
dao --yolo "将README.md里所有的DAO_CODE改为DAO CODE"

# 长任务自主模式
dao --goal "实现用户登录功能，包含JWT和刷新token"
```

## 常用命令
- `/init`：扫描项目生成DAO.md，供后续会话自动加载项目上下文
- `/cost`：查看token用量与缓存命中率
- `/compact`：手动压缩对话历史，释放上下文窗口
- `/help`：查看所有命令
- `Ctrl+O`：展开/收齐工具输出的全量内容

## 依赖前提
- DeepSeek API key（必须）
- 终端环境（支持Unix shell或Windows CMD/PowerShell）
- 如使用npm方式，需Node.js >=20；二进制方式无额外依赖