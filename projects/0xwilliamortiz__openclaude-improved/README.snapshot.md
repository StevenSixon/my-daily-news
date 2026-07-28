<div align="center">

<img src="docs/assets/openclaude-wordmark.svg" alt="OpenClaude Improved" width="640">

### OpenClaude — Improved Version

**runs anywhere. uses anything.**

An open-source coding agent for the CLI. Cloud APIs, gateways, and local models —
same tools, same agents, same workflow.

<br>

![node](https://img.shields.io/badge/node-%E2%89%A522-3c873a?style=flat-square)
![bun](https://img.shields.io/badge/bun-1.3.13%2B-fbf0df?style=flat-square&labelColor=14151a)
![platform](https://img.shields.io/badge/windows%20%C2%B7%20macos%20%C2%B7%20linux-0ea5e9?style=flat-square)
[![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square)](LICENSE)

**[Install](#install)** · **[Quick start](#quick-start)** · **[Providers](#providers)** · **[Sessions](#sessions)** · **[Config](#config)** · **[Docs](#docs)**

</div>

---

## Install

Built from source. Windows examples below; macOS and Linux are identical minus the
shell syntax.

**Prerequisites** — Node `>=22` (enforced by `engines.node`) and Bun.

```powershell
node --version
bun --version
```

No Bun? `winget install Oven-sh.Bun` or [bun.sh](https://bun.sh).

**Build and link**

```powershell
cd openclaude-main
bun install
bun run build
npm install -g .
openclaude
```

That's it — `openclaude` is now on your PATH.

---

## Quick start

Run `/provider` inside OpenClaude for guided setup with saved profiles — this is the
recommended path. Credentials land in `.openclaude-profile.json`.

Prefer env vars? Pick one:

<details open>
<summary><b>OpenAI</b></summary>

```powershell
$env:CLAUDE_CODE_USE_OPENAI="1"
$env:OPENAI_API_KEY="sk-..."
$env:OPENAI_MODEL="gpt-4o"
openclaude
```

</details>

<details>
<summary><b>Ollama</b> — local, no key</summary>

```powershell
$env:CLAUDE_CODE_USE_OPENAI="1"
$env:OPENAI_BASE_URL="http://localhost:11434/v1"
$env:OPENAI_MODEL="qwen2.5-coder:7b"
openclaude
```

OpenClaude talks to Ollama's native chat API and requests a 32768-token window per
request, so same-session history isn't silently trimmed by the OpenAI-compat shim.
Override with `OPENCLAUDE_OLLAMA_NUM_CTX` or `OLLAMA_CONTEXT_LENGTH`.

</details>

<details>
<summary><b>GitHub Models</b></summary>

Run `/onboard-github` inside OpenClaude. Interactive, credentials saved.

</details>

<details>
<summary>macOS / Linux syntax</summary>

```bash
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_API_KEY=sk-...
export OPENAI_MODEL=gpt-4o
openclaude
```

</details>

> Project `.env` files are **not** auto-loaded. Use `--provider-env-file .env` for
> provider vars, or export runtime knobs from your shell.

---

## Providers

| Provider | Setup | Key detail |
|---|---|---|
| **OpenAI-compatible** | `/provider` · env | Any `/v1` server — OpenRouter, DeepSeek, Groq, Mistral, LM Studio |
| **Ollama** | `/provider` · env | Local, no API key |
| **Gemini** | `/provider` · env | API key only |
| **GitHub Models** | `/onboard-github` | Saved credentials |
| **Codex / Codex OAuth** | `/provider` | Browser sign-in or existing Codex CLI auth |
| **Gitlawb Opengateway** | default · `/provider` | Startup default on fresh installs; [get a key](https://gitlawb.com/opengateway/keys) |
| **Bedrock · Vertex · Foundry** | env | Anthropic-family routes |

<details>
<summary><b>Full provider list</b> (12 more)</summary>

| Provider | Endpoint / key | Default model |
|---|---|---|
| Z.AI GLM Coding Plan | `api.z.ai/api/coding/paas/v4` · `OPENAI_API_KEY` | `glm-5.2` |
| AI/ML API | `api.aimlapi.com/v1` · `AIMLAPI_API_KEY` | `gpt-4o` |
| Hicap | `api-key` auth, Responses mode for `gpt-*` | — |
| Fireworks AI | `FIREWORKS_API_KEY` | 276 curated models |
| LongCat | `api.longcat.chat/openai/v1` · `LONGCAT_API_KEY` | `LongCat-2.0` |
| ClinePass | `api.cline.bot/api/v1` · `CLINE_API_KEY` | 5h / weekly / monthly caps |
| OpenCode Zen | `opencode.ai/zen/v1` · `OPENCODE_API_KEY` | 48 models, PAYG |
| OpenCode Go | `opencode.ai/zen/go/v1` · `OPENCODE_API_KEY` | 13 models, $10/mo |
| Xiaomi MiMo | `mimo.mi.com` · `MIMO_API_KEY` | `mimo-v2.5-pro` |
| NEAR AI | `cloud-api.near.ai/v1` · `NEARAI_API_KEY` | Claude / GPT / Gemini + TEE |
| Cloudflare Workers AI | `api.cloudflare.com/.../ai/v1` · `CLOUDFLARE_API_TOKEN` | — |
| Atomic Chat | `/provider` · `bun run dev:atomic-chat` | Auto-detects loaded models |

**Gotchas worth knowing**

- Anthropic-only features don't exist on every backend. Tool quality tracks model quality — small local models struggle with long multi-step tool loops.
- Some providers cap output below CLI defaults; OpenClaude adapts where it can.
- Opengateway uses one base URL — switch models with `/model`, don't pin the URL to `/v1/xiaomi-mimo`.
- GLM reasoning: `glm-5.2?reasoning=high`, `?reasoning=xhigh`, or `?thinking=disabled`.
- MiMo uses `api-key` header auth and has no `/usage` reporting yet.
- GitHub Copilot serializes sub-agents by default to save Premium Requests — see [agent routing](docs/agent-routing.md#github-copilot-sub-agent-optimization).

</details>

---

## What you get

| | |
|---|---|
| **Tools** | Bash, read/write/edit, grep, glob, agents, tasks, MCP, slash commands |
| **Streaming** | Live tokens and tool progress |
| **Tool loops** | Multi-step: model call → execution → follow-up |
| **Vision** | URL and base64 images where the provider supports it |
| **Repo map** | PageRank-ranked structural map, auto-injected behind the `REPO_MAP` flag. Inspect with `/repomap` ([docs](docs/repo-map.md)) |
| **Agent routing** | Per-agent provider/model overrides, `maxSteps` caps, routable built-ins (`Explore`, `Plan`, `verification`) ([docs](docs/agent-routing.md)) |
| **Web** | `WebSearch` via DuckDuckGo free by default; drop in `FIRECRAWL_API_KEY` for JS-rendered pages |
| **gRPC** | Headless bidirectional-streaming server for CI and custom UIs (`npm run dev:grpc`) ([docs](docs/grpc-server.md)) |
| **VS Code** | Bundled extension: launch integration, Control Center, in-editor chat, Foundry/Azure config |

---

## Sessions

```bash
openclaude --continue                             # most recent, this directory
openclaude --resume <session-id>
openclaude --resume <session-id> --fork-session   # branch history, new ID
```

Forking branches conversation history only — no worktree, no filesystem isolation.

<details>
<summary><b>Background sessions</b></summary>

```bash
openclaude --bg "fix failing tests"
openclaude --bg --name auth-refactor "refactor auth middleware"

openclaude ps
openclaude logs auth-refactor -f
openclaude kill auth-refactor
```

Plain local child processes — no daemon, no network service. Metadata and logs live
in `~/.openclaude/bg-sessions/`. Names are reusable once a session is terminal; use
the ID to reach older logs sharing a name. `attach` currently just points you at
`logs <id> -f`.

</details>

---

## Config

OpenClaude owns `~/.openclaude/` and `~/.openclaude.json`. It does **not** read
`~/.claude`, project `.claude/` directories, or `CLAUDE_CONFIG_DIR`. Fresh installs
start empty and don't need Claude Code present.

Migrating from a `.claude`-era setup? Copy only files *you* wrote — settings,
commands, agents, skills, scheduled tasks — into the matching `.openclaude` path.
Don't blanket-copy, and don't move credentials; re-run provider setup instead.

`OPENCLAUDE_CONFIG_DIR` relocates everything.

---

## Buddy

`/buddy` hatches a truecolor pixel-art companion that stands beside your prompt and
fires its signature move on every Enter.

```
/buddy set robinhood    green archer — arrow shot
/buddy set kaio         full-width energy wave
/buddy set strawhat     stretchy snap-back punch
/buddy set merlin       sparkle stream
/buddy set kage         spinning shuriken
/buddy set ember        dragon fire, real heat gradient
/buddy set corsair      cannonball with smoke trail
```

Respects `prefersReducedMotion`, degrades to line art on low-color terminals,
`/buddy mute` silences it. Needs ~100 columns for the full sprite.

---

## Development

```bash
bun run dev        # build and launch from source
bun test           # full suite
```

Before opening a PR:

```bash
bun run build
bun run smoke
bun test path/to/changed.test.ts
bun run test:coverage          # if you touched shared runtime or provider logic
```

<details>
<summary>Other commands and layout</summary>

```bash
bun run test:coverage:ui                        # rebuild HTML report only
bun run test:provider
bun run test:provider-recommendation
bun run doctor:runtime
bun run verify:privacy
bun run security:pr-scan -- --base origin/main
```

```
src/                                   core CLI and runtime
scripts/                               build, verify, maintenance
docs/                                  setup and contributor docs
bin/                                   launcher entrypoints
vscode-extension/openclaude-vscode/    VS Code extension
```

Coverage lands at `coverage/lcov.info` plus a browsable report at `coverage/index.html`.

If startup reports `ripgrep not found`, install ripgrep system-wide and confirm
`rg --version` resolves in the same shell.

</details>

---

## Docs

**Getting started** — [Non-technical](docs/non-technical-setup.md) · [Windows](docs/quick-start-windows.md) · [macOS / Linux](docs/quick-start-mac-linux.md) · [Android](ANDROID_INSTALL.md)

**Going deeper** — [Advanced setup](docs/advanced-setup.md) · [Smart auto-routing](docs/smart-routing.md) · [Agent routing](docs/agent-routing.md) · [Repo map](docs/repo-map.md) · [gRPC server](docs/grpc-server.md)

---

## Contributing

Open an issue first for anything large, so scope is settled before code. Bugs and
actionable feature work go to
[Issues](https://github.com/0xwilliamortiz/openclaude-improved/issues); questions
and ideas to
[Discussions](https://github.com/0xwilliamortiz/openclaude-improved/discussions).
Security reports: [SECURITY.md](SECURITY.md).

---

<div align="center">
<sub>

MIT for contributor modifications; derived Claude Code code remains Anthropic's — see [LICENSE](LICENSE).

An independent community project. Not affiliated with, endorsed by, or sponsored by Anthropic.
"Claude" and "Claude Code" are trademarks of Anthropic PBC.

</sub>
</div>
