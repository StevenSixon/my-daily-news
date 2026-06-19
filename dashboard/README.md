# AI 项目日报 · Dashboard

A single-file HTML dashboard that renders the `my-daily-news` pipeline output —
trending AI GitHub projects with star deltas, tech stack, and the deep-dive
analysis (它是什么 / 为什么火 / 技术栈 / 核心能力 / 适用场景 / 同类对比 / 版本动态).

**Stack:** React 18 + TypeScript + Vite + Tailwind CSS + shadcn/ui, bundled with
Parcel into one self-contained `bundle.html` (all JS/CSS inlined) for use as a
claude.ai artifact or standalone page.

## Develop

```bash
pnpm install
pnpm dev          # http://localhost:5173
```

## Bundle to a single HTML file

```bash
bash ~/.claude/skills/artifacts-builder/scripts/bundle-artifact.sh
# → dashboard/bundle.html
```

> Note: this machine's `~/.npmrc` points pnpm at a corporate registry that lacks
> `create-vite`/`parcel`. If installs 404, prefix commands with
> `npm_config_registry=https://registry.npmjs.org/`.

## Data

`src/data.ts` holds a typed snapshot (`Daily` / `Project[]`) sourced from
`daily/<date>.json` + `projects/<name>/metadata.json` + `analysis.md`.
