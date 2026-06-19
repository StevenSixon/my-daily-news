# Avatar / brand assets

AI-themed avatar for the project, using the dashboard's purple + cyan palette.

| File | Use |
|---|---|
| `avatar.svg` | Source (vector, scalable, recolorable) |
| `avatar-1024.png` | High-res / social preview |
| `avatar-512.png` | **GitHub avatar** (recommended upload) |
| `avatar-280.png` | Minimum recommended size |
| `concept-b-core.svg` / `concept-c-trend.svg` | Alternate directions (neural core / trend spark) |

## How to set it on GitHub

GitHub avatars **can't be set via API** — upload through the web UI:

- **Personal profile:** Settings → Profile → *Profile picture* → upload `avatar-512.png`
- **Organization:** Org → Settings → *Profile picture*
- **Repo social preview** (the card shown when the repo is shared): repo → Settings → General → *Social preview* → upload `avatar-1024.png`

## Regenerate PNGs from the source

```bash
rsvg-convert -w 512 -h 512 avatar.svg -o avatar-512.png
```
