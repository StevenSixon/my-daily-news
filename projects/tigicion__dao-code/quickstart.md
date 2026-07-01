**依赖**：Node.js ≥20

**安装**：
```bash
npm i -g dao-code
# 或一键脚本: curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh
```

**运行**：
```bash
dao                  # 首次自动提示输入 DeepSeek API Key
# 单次任务
dao "修复 src/utils.ts 中的时区 bug"
```

**常用命令**：
- `/init` 生成 DAO.md 项目指南
- `/cost` 查看 token 用量与缓存命中率
- `@` 路径引用文件
- `Esc` 中断当前回合