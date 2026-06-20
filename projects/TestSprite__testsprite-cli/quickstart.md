## 安装前提
- Node.js ≥ 20
- 已注册TestSprite账号并获取API密钥（https://www.testsprite.com）

## 安装
```bash
npm install -g @testsprite/testsprite-cli
```
或使用npx临时运行：
```bash
npx @testsprite/testsprite-cli
```

## 快速上手
```bash
# 一键配置API密钥并安装智能体技能（以claude为例）
testsprite setup
# 按提示输入API Key，选择智能体目标（如claude）
# 非交互模式：
TESTSPRITE_API_KEY=sk-... testsprite setup --from-env --yes --agent claude
```

## 最小可用循环示例
```bash
# 1. 创建并运行一个前端测试（假设已有项目proj_8f0f6和计划文件）
testsprite test create --project proj_8f0f6 --type frontend \
  --plan-from ./checkout-flow.plan.json --run --wait --output json
# 若失败，exit code为1

# 2. 获取失败定位包
testsprite test failure get test_3a9f21c7 --out ./.testsprite/failure

# 3. 修复代码后重跑
testsprite test rerun test_3a9f21c7 --wait --output json
```