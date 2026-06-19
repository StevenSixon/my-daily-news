```bash
git clone https://github.com/koala73/worldmonitor.git
cd worldmonitor
npm install
npm run dev          # 打开 http://localhost:3000
# 变体开发：
npm run dev:tech     # 科技变体
npm run dev:finance  # 金融变体
# 无需任何环境变量即可运行核心功能。可选功能需API密钥（见.env.example）
```
桌面构建需Rust与Tauri 2环境，详见文档。部署支持Vercel、Docker或静态导出。