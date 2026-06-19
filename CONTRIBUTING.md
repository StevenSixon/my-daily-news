# Contributing

Thanks for your interest in improving **AI Daily Digest**! This is a small,
file-based pipeline, so it's easy to get into. This guide covers the setup, the
non-negotiable security rules, and the highest-value places to contribute.

> 中文用户：开发约定与安全红线另见 [`CLAUDE.md`](./CLAUDE.md) 与 [`SECURITY.md`](./SECURITY.md)。

## 🔴 Security first — this is a public repo

**Never commit any key, credential, or token.** This rule overrides everything
else in this guide.

- Never commit `.env`, `*.pem`, `*.key`, `*secret*.json`, `data/.feishu_token.json`,
  or any file containing a real secret. These are already in `.gitignore` — do
  **not** force them in with `git add -f`.
- Never hard-code secrets. Read them from the environment via `env("KEY")` /
  `require_env("KEY")`. When you add a new secret, add only an **empty placeholder
  key** to `.env.example`.
- Before committing, run `git status` / `git diff --cached` and confirm there are
  no secrets, tokens, private keys, absolute home paths, or internal addresses.
- A `pre-commit` hook (`scripts/git-hooks/pre-commit`) is a backstop, **not** an
  excuse. Don't bypass it with `--no-verify` unless you are 100% sure it's a false
  positive.

Full policy and "what if a secret leaks" steps: [`SECURITY.md`](./SECURITY.md).

## 🛠️ Local setup

One-command setup (creates the venv, installs deps, copies `.env`):

```bash
bash bin/setup.sh
```

Or manually:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt        # runtime + test deps
cp .env.example .env                         # then fill in your own keys
```

Enable the secret-scan pre-commit hook (recommended — it's the backstop that
keeps keys out of commits):

```bash
git config core.hooksPath scripts/git-hooks
```

Requires **Python 3.11+**.

## ✅ Before you open a PR

```bash
pytest                      # tests live in tests/, config in pytest.ini
```

- Keep changes focused; one logical change per PR.
- Match the surrounding code's style, naming, and comment density.
- If you change behavior, add or update a test under `tests/`.
- Runtime dependencies in `requirements.txt` are **pinned on purpose** (libraries
  like `litellm` move fast and can break the pipeline). To bump one: change the
  version → run `pytest` locally → commit.
- Commit messages follow Conventional Commits, e.g. `feat:`, `fix:`, `docs:`,
  `data:`, `chore:`. Scope is optional, e.g. `fix(ci): …`.

## 🌟 Good places to contribute

The architecture deliberately separates concerns, so these are clean extension
points (see [`docs/DESIGN.md`](./docs/DESIGN.md) for the full picture):

- **New delivery channels** — Feishu is the only one built in today. Telegram,
  Slack, Discord, and email are all natural additions. The pipeline produces
  `daily/<date>.json`; a channel just needs to read it and send.
- **New data sources** — beyond GitHub Trending + Search (e.g. Hacker News,
  Product Hunt), feeding into the same dedupe/index step.
- **New LLM providers** — the provider layer is pluggable via `config/config.yaml`
  (`llm.provider` / `llm.model`); adding one with failover support is welcome.
- **Non-AI categories** — the focus scope is config-driven (`focus.search_topics`);
  the architecture reserves room to expand beyond AI apps.
- **Docs & i18n** — improvements to the README, the English/Chinese parity, or
  the design doc.

Not sure where to start? Open an issue describing the idea first — happy to
discuss the approach before you write code.

## 📄 License

By contributing, you agree that your contributions are licensed under the
project's [MIT License](./LICENSE).
