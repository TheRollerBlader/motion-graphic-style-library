---
name: style-papercut
description: "Apply the Paper Cut motion-graphic style from the motionstyle_papercut Python library when building an explainer, title card, or narration-synced video. Use when the user asks for paper cut, paper craft, layered paper, construction paper, cut paper, names Paper Cut, or the style id papercut. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Paper Cut

Apply this when the picture should be Paper Cut. Colored sheets slide into a stack. The diagram has thickness.

## Rules agents miss

- Layer order is the explanation. Back sheet first, top sheet last.
- Every sheet is a flat color from the palette. No photos as paper texture.
- The shadow is soft and downward. A hard offset shadow belongs to a different style.

The spec below is generated from `motionstyle_papercut`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Paper Cut

Library: `motionstyle_papercut`
Style id: `papercut`

Colored sheets slide into a stack. The diagram has thickness.

Best for: stories, consumer brands, process steps, gentle explainers.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #E7D7C3
bgRaised      #F3E6D4
surface       #FFF8F0
ink           #2A2118
text          #2A2118
textDim       #7A6556
primary       #E25B45
primaryLight  #F08A76
primaryDark   #B93E2C
secondary     #2F6F6A
accent        #F0C14A
danger        #C44536
ok            #2F6F6A
info          #3E6BA8
sheet         #F6E4D4
sheet_pink    #F6D6D0
```

## Typography

- Display: Iowan Old Style, Palatino, Georgia, serif. Weight 700. Tracking -0.010em. Case: as written. Line height 1.0.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking 0.000em. Case: as written. Line height 1.4.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.040em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 18px.
- Border: 0px solid #2A2118.
- Shadow: `0 16px 24px rgba(80, 50, 30, 0.18)`.
- Backdrop blur: 0px.
- Each sheet is a flat color with a soft, long shadow. Shadows fall down and slightly right. Do not add a hard comic outline.
## Motion

Sheets travel a short distance into the stack, back layer first. The top sheet arrives last. Motion eases out. The stack then breathes one or two pixels.

Stagger between repeated elements: 0.1s.

Idle: The top sheet lifts three pixels and settles. Shadows stay under the sheets.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("sheet_x"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `sheet_x`

- Duration: 0.55s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `x` (px)
- Keyframes:
  - 0.00 → -36
  - 1.00 → 0
- Alternate the sign per layer so they do not all enter from the same side.

### `sheet_y`

- Duration: 0.55s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 24
  - 1.00 → 0
- A small drop as the sheet lands. Combine with sheet_x.

### `idle_float`

- Duration: 3.8s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 0
  - 0.50 → -3
  - 1.00 → 0
- Only the top sheet. Lower sheets stay, or the stack looks nervous.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- The desk is the background. No horizon, no room, no device.
- Three to five sheets is a scene. More than that is clutter.
- Type sits on the top sheet in ink. Display is serif. Labels can be the sans body face.
- Cut edges are simple: rounded rectangles, circles, and one custom silhouette if the noun needs it.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Desk: the background color, nothing else.
- Sheet: a solid palette fill, 18px radius, soft shadow, entered with sheet_x and sheet_y.
- TopType: serif title on the front sheet.
- Tab: a small sheet peeking out, used as a step label.

## Captions

On the desk, below the stack, ink type. No extra sheet unless the caption is the point of the beat. Current word is primary.

## Do

- Send the back sheet in first so the stack builds toward the camera.
- Give each step its own sheet color from the palette.
- Keep silhouettes bold enough to read without an outline.

## Don't

- Do not use black comic strokes, neon glow, or glass blur.
- Do not slide a sheet across the whole frame. The travel is short.
- Do not put a paragraph on a sheet. One title and one line.
- Do not cast a shadow upward.

