## 快速开始
### 1. 云体验
直接注册 [twenty.com](https://twenty.com) 创建工作区，无需安装。

### 2. 构建应用（最小可用示例）
```bash
npx create-twenty-app my-app
cd my-app
```
定义业务对象（如 Deals）：
```ts
import { defineObject, FieldType } from 'twenty-sdk/define';

export default defineObject({
  nameSingular: 'deal',
  namePlural: 'deals',
  labelSingular: 'Deal',
  labelPlural: 'Deals',
  fields: [
    { name: 'name', label: 'Name', type: FieldType.TEXT },
    { name: 'amount', label: 'Amount', type: FieldType.CURRENCY },
    { name: 'closeDate', label: 'Close Date', type: FieldType.DATE_TIME },
  ],
});
```
发布到工作区：
```bash
npx twenty app:publish --private
```

### 3. 自托管
使用 Docker Compose：
```bash
git clone https://github.com/twentyhq/twenty.git
cd twenty
docker compose up -d
```
详细见[自托管指南](https://docs.twenty.com/developers/self-host/capabilities/docker-compose)。

### 依赖前提
- Node.js 18+，pnpm（本地开发）
- Docker 和 Docker Compose（自托管）
- PostgreSQL、Redis 容器化依赖已内置在 compose 文件中。