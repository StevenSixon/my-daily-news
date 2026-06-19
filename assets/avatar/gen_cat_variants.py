#!/usr/bin/env python3
"""Generate color variants of the programmer-cat avatar (concept-h-cat).
Same geometry, different palette. Renders SVG; PNG is produced by rsvg-convert.
"""
import subprocess, os

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{bg1}"/><stop offset="0.55" stop-color="{bg2}"/><stop offset="1" stop-color="{bg3}"/>
    </linearGradient>
    <radialGradient id="g" cx="0.5" cy="0.42" r="0.6">
      <stop offset="0" stop-color="{glow}" stop-opacity="0.45"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fur" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{fur1}"/><stop offset="1" stop-color="{fur2}"/>
    </linearGradient>
    <linearGradient id="lens" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#16263f"/><stop offset="1" stop-color="#0f3a60"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#bg)"/>
  <rect width="512" height="512" rx="112" fill="url(#g)"/>
  <g fill="{code}" opacity="{codeop}" font-family="monospace" font-size="40" font-weight="700">
    <text x="42" y="92">&lt;/&gt;</text><text x="396" y="472">~$</text>
  </g>
  <!-- body -->
  <path d="M120 512 V470 a136 136 0 0 1 272 0 V512 Z" fill="url(#fur)"/>
  <!-- ears -->
  <path d="M150 196 L150 96 L244 168 Z" fill="url(#fur)"/>
  <path d="M362 196 L362 96 L268 168 Z" fill="url(#fur)"/>
  <path d="M166 178 L166 128 L214 166 Z" fill="{earin}"/>
  <path d="M346 178 L346 128 L298 166 Z" fill="{earin}"/>
  <!-- head -->
  <ellipse cx="256" cy="262" rx="146" ry="130" fill="url(#fur)"/>
  <ellipse cx="256" cy="286" rx="112" ry="96" fill="{face}" opacity="{faceop}"/>
  <!-- glasses -->
  <circle cx="206" cy="252" r="44" fill="url(#lens)" stroke="#120a26" stroke-width="8"/>
  <circle cx="306" cy="252" r="44" fill="url(#lens)" stroke="#120a26" stroke-width="8"/>
  <line x1="250" y1="252" x2="262" y2="252" stroke="#120a26" stroke-width="8"/>
  <g stroke="#7ff0ff" stroke-width="4.5" opacity="0.9" stroke-linecap="round">
    <line x1="186" y1="244" x2="216" y2="244"/><line x1="186" y1="258" x2="206" y2="258"/>
    <line x1="286" y1="244" x2="316" y2="244"/><line x1="286" y1="258" x2="306" y2="258"/>
  </g>
  <!-- nose + mouth -->
  <path d="M242 306 h28 l-14 16 Z" fill="{nose}"/>
  <path d="M256 322 q-20 22 -40 8 M256 322 q20 22 40 8" fill="none" stroke="{mouth}" stroke-width="6" stroke-linecap="round"/>
  <!-- whiskers -->
  <g stroke="{whisk}" stroke-width="5" opacity="0.7" stroke-linecap="round">
    <line x1="150" y1="300" x2="80" y2="288"/><line x1="150" y1="316" x2="84" y2="320"/>
    <line x1="362" y1="300" x2="432" y2="288"/><line x1="362" y1="316" x2="428" y2="320"/>
  </g>
</svg>
'''

PALETTES = {
    "purple": dict(bg1="#241551", bg2="#341a6b", bg3="#150b2e", glow="#8a2bff",
                   fur1="#9a5cff", fur2="#6f12f5", earin="#ff8fb0", face="#b88bff", faceop="0.35",
                   nose="#ff8fb0", mouth="#2c1b4d", whisk="#e9deff", code="#7ff0ff", codeop="0.16"),
    "mono": dict(bg1="#2a2d36", bg2="#3a3f4b", bg3="#15171d", glow="#aeb6c6",
                 fur1="#5b606e", fur2="#23262f", earin="#c9ccd6", face="#8a8f9c", faceop="0.30",
                 nose="#d98fa0", mouth="#101218", whisk="#ffffff", code="#cfd5e0", codeop="0.18"),
    "orange": dict(bg1="#3a2410", bg2="#5a3414", bg3="#1d1108", glow="#ff9a3c",
                   fur1="#ffb14e", fur2="#ef7d18", earin="#ffd0a0", face="#ffce8a", faceop="0.32",
                   nose="#e85d3c", mouth="#5a2a0f", whisk="#fff3e0", code="#ffd08a", codeop="0.18"),
    "blue": dict(bg1="#0e1f3a", bg2="#163058", bg3="#080f20", glow="#47bfff",
                 fur1="#5fc8ff", fur2="#2073d6", earin="#bfe4ff", face="#9fd6ff", faceop="0.32",
                 nose="#ff8fb0", mouth="#0d2748", whisk="#eaf6ff", code="#7ff0ff", codeop="0.18"),
    "green": dict(bg1="#0e2e22", bg2="#14503a", bg3="#08180f", glow="#3fe0a0",
                  fur1="#5fe0a0", fur2="#1f9f6a", earin="#bff3da", face="#9fe8c6", faceop="0.32",
                  nose="#ff8f7a", mouth="#0d3324", whisk="#eafff5", code="#9bffd6", codeop="0.18"),
    "pink": dict(bg1="#3a1230", bg2="#5e1c4c", bg3="#1d0a18", glow="#ff5fd0",
                 fur1="#ff8fc8", fur2="#e0489f", earin="#ffd0ec", face="#ffbfe2", faceop="0.32",
                 nose="#c13f8e", mouth="#5a1240", whisk="#fff0f8", code="#ffaee6", codeop="0.18"),
}

here = os.path.dirname(os.path.abspath(__file__))
for name, p in PALETTES.items():
    svg = TEMPLATE.format(**p)
    base = f"cat-{name}"
    svg_path = os.path.join(here, base + ".svg")
    png_path = os.path.join(here, base + ".png")
    with open(svg_path, "w") as f:
        f.write(svg)
    subprocess.run(["rsvg-convert", "-w", "512", "-h", "512", svg_path, "-o", png_path], check=True)
    print("generated", base)
