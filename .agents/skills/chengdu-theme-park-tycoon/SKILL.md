---
name: chengdu-theme-park-tycoon
description: Create, modify, or ship a low-poly Web3D Theme Park Tycoon simulation based on Chengdu Chunxi Road and Taikoo Li, including Three.js camera controls, dynamic visitors, rides, tycoon HUD, and agent-ready static HTML output.
---

# Chengdu Theme Park Tycoon

Use this skill when the user asks for a Web3D/Three.js low-poly theme park, tycoon simulation, Chengdu Chunxi Road/Taikoo Li scene, or a reusable agent scaffold for this game.

## Outputs

Default output is a standalone HTML file using Three.js from CDN. It should run from a local static server and includes:

- Low-poly Chengdu landmarks: Chunxi Road, Taikoo Li blocks, IFS panda wall, Daci Temple, metro entrance, commercial streets.
- Dynamic simulation: visitors, queues, parade traffic, monorail, rides, income, happiness, cash, time, weather, day/night lighting.
- Controls: mouse orbit/zoom/pan, view presets, speed/flow sliders, pause, weather toggle, build actions.
- Verification: open in a browser, confirm the canvas renders nonblank, view buttons work, and mobile has no horizontal overflow.

## Quick Start

To create the default game in the current project:

```bash
python .agents/skills/chengdu-theme-park-tycoon/scripts/create_theme_park.py --output theme-park-tycoon.html
```

For a custom title:

```bash
python .agents/skills/chengdu-theme-park-tycoon/scripts/create_theme_park.py --output game.html --title "成都太古里主题公园"
```

If the agent cannot run the script, copy `assets/theme-park-tycoon.html` to the requested output path and make focused edits.

## Workflow

1. Clarify the target only if the output path, framework, or deployment surface is genuinely ambiguous.
2. Use `scripts/create_theme_park.py` for the baseline static HTML.
3. Modify the generated file directly for requested features, keeping the simulation as a first-screen playable app rather than a landing page.
4. Keep the 3D scene full-bleed. Do not wrap the canvas in a decorative card.
5. Preserve mouse camera controls and at least four view presets unless the user asks to simplify.
6. For richer versions, add systems that visibly change over time: new rides, visitor AI, economy, weather, lighting, queues, transit, events, or build upgrades.
7. Verify with a local static server and browser automation when available.

## Visual Direction

- Low-poly geometry, flat shading, clear silhouettes, readable landmarks.
- Palette should mix greenery, pavement, warm retail facades, muted glass, red/gold signs, and blue transport accents.
- UI should be dense and useful: stats, controls, log, build actions. Avoid marketing hero sections.
- Mobile UI may be compact and scrollable, but the canvas must remain full-screen behind it.

## Interoperability Notes

- Codex: repo-scoped discovery works from `.agents/skills/chengdu-theme-park-tycoon`.
- Claude Code, OpenClaw, Hermes, or other agents: point them at this folder or copy the folder into their local skill/library directory. The skill is self-contained and only requires file access plus optional Python for the scaffold script.
- The generated game imports Three.js from `https://unpkg.com`; if offline use is required, vendor Three.js and update the import map.

## Validation Checklist

- `Invoke-WebRequest http://127.0.0.1:<port>/<file>` returns 200.
- Browser console has no page errors.
- A `canvas` exists and has many color buckets/non-sky samples after 1-3 seconds.
- View buttons update active state and move the camera.
- Build buttons change cash and add a visible object or event.
- Mobile viewport has no horizontal overflow.
