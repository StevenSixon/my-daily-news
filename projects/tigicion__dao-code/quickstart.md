## 快速上手

### 安装

**方式一：一键脚本**
```bash
curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh
```

**方式二：npm（需 Node ≥ 20）**
```bash
npx dao-code  # 零安装试用
# 或全局安装
npm i -g dao-code
```

### 配置
获取 DeepSeek API key：https://platform.deepseek.com/api_keys

启动 `dao`（若未检测到 key，会引导粘贴并存入 `~/.dao/config.json`）。

### 最小示例
```bash
dao "把 src/utils.ts 里的 formatDate 改成支持时区"
```

交互模式：
```bash
dao
```
- 输入问题后回车发送，`@` 引用文件，`/cost` 查看花费，`/compact` 手动压缩上下文。
- 写/执行类操作需经过审批（输入 y/n/a）。

长任务自主模式：
```bash
dao --goal "重构错误处理逻辑，并通过 npm test"
```