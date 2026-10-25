---
name: apply-motion-style
description: "Choose and apply one motion-graphic style from the motionstyles Python libraries when building an explainer, title card, promo, or narration-synced video. Use when the user asks for an explainer video, motion graphics, kinetic type, a visual style, glassmorphism, brutalist, chalk, blueprint, or any named style in this repo."
---

# Apply a motion style

Skin the video with exactly one library from this repo. The library decides palette, type, shape, and the named motion clips. It does not render the video. You implement those clips in the renderer the project already uses.

## Pick a style

1. If the user named a look, use that style even if another also fits.
2. If they did not, read [catalog.md](catalog.md) and match their subject to "Use it for".
3. Tell them which style you chose and why, in one sentence. If two styles fit equally, ask before drawing.
4. Read that style's skill next: `.cursor/skills/style-<id>/SKILL.md`. Follow it literally. Do not keep a second palette in your head.

One video, one style. Do not mix Swiss type with a glass panel, or chalk strokes with a neon glow.

## Load the tokens

From the repo root, with the package installed:

```bash
python -m motionstyles export <id> --format md -o style.md
python -m motionstyles export <id> --format json -o style.json
```

Use `style.md` as the spec. Use `style.json` when you need clip durations, easings, and keyframes. CSS variables (`--format css`) and a Remotion theme (`--format ts`) are the same data.

Colors in the spec are the only colors. If a hex is not in the palette, it does not go on screen.

## Build the picture

1. Build the style's scene primitives once.
2. Read the narration, if there is any. One spoken idea gets one visual. A diagram of the thing being named, not a metaphor next to it.
3. Entrance, build, and idle come from the named clips. Do not invent a second easing family. Sample a clip with `sample_clip` from `motionstyle_core`, or copy its keyframes into the renderer.
4. Stagger repeated elements by the spec's stagger, not by a new number.
5. A sub-animation that illustrates a word starts on that word's timestamp.
6. Play the idle clip on anything that holds. Nothing sits perfectly still for more than about a second.
7. Captions follow the Captions section. Do not add a second caption treatment.
8. Canvas is 1920×1080 at 30fps unless the user asked for another frame. A 9:16 cut reflows the layout and keeps the tokens. It does not recolor.

## Map a clip onto a renderer

A clip has a duration, an easing, a property, and keyframes. Easing applies inside each keyframe span. Hold the last value after the clip ends.

- Remotion: `interpolate` over the keyframe times, with the clip's `cssEase`. Springs in the spec map to `spring({ stiffness, damping, mass })`.
- HyperFrames or plain CSS: use the exported variables `--duration-<clip>` and `--ease-<clip>`.
- `strokeOffset` runs from 1 (hidden) to 0 (drawn). `progress` runs from 0 to 1 for counts and bar fills.

The GIFs in `previews/` and the tiles in `docs/gallery.html` are studies of these clips. Do not paste the GIFs into the explainer as the scenes.

## Regenerating

The style skills are generated from the Python libraries. After a library change:

```bash
python -m motionstyles skills
python -m motionstyles export-all catalog
python -m motionstyles gallery
python -m motionstyles previews previews
```
