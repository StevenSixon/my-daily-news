## 安装
```bash
npm install @flue/runtime @flue/cli
```
（可能需要 Node.js 18+ 和 npm 7+）

## 最小可用示例
以下展示一个 bug 分诊代理。创建 `agents/triage.ts`：
```ts
import { createAgent, type AgentRouteHandler } from '@flue/runtime';
import { local } from '@flue/runtime/node';
import triage from '../skills/triage/SKILL.md' with { type: 'skill' };
import verify from '../skills/verify/SKILL.md' with { type: 'skill' };
import * as githubTools from '../tools/github.ts';

const instructions = `
Triage a bug report end-to-end: reproduce the bug,
diagnose the root cause, verify whether the behavior is
intentional, and attempt a fix.
`;

export const route: AgentRouteHandler = async (_c, next) => next();

export default createAgent(() => ({
  model: 'anthropic/claude-sonnet-4-6',
  tools: [...githubTools],
  skills: [triage, verify],
  sandbox: local(),
  instructions,
}));
```
启动代理（需配置 API key 等）：
```bash
flue run agent ./agents/triage.ts
```
更多示例见 `examples/` 目录下的 helper、channels 等。