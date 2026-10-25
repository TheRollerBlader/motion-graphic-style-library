---
name: style-swiss
description: "Apply the Editorial Swiss motion-graphic style from the motionstyle_swiss Python library when building an explainer, title card, or narration-synced video. Use when the user asks for swiss style, international typographic style, helvetica grid, editorial print, bauhaus grid, names Editorial Swiss, or the style id swiss. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Editorial Swiss

Apply this when the picture should be Editorial Swiss. A grid, a grotesque, and one red. Type does the explaining.

## Rules agents miss

- A radius other than 0 is wrong for this style.
- A second red element means the frame is shouting. Remove one.
- Prefer a wipe or a crop over a fade.

The spec below is generated from `motionstyle_swiss`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Editorial Swiss

Library: `motionstyle_swiss`
Style id: `swiss`

A grid, a grotesque, and one red. Type does the explaining.

Best for: strategy explainers, essays, product positioning, serious software.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #F3F0E8
bgRaised      #E7E2D6
surface       #F7F4EC
ink           #111111
text          #111111
textDim       #5E594F
primary       #E10600
primaryLight  #FF3B30
primaryDark   #9E0500
secondary     #111111
accent        #E10600
danger        #E10600
ok            #1F6B4A
info          #1D4E89
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 700. Tracking 0.040em. Case: uppercase. Line height 0.9.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking 0.010em. Case: as written. Line height 1.35.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.080em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 0px.
- Border: 1px solid #111111.
- Shadow: `none`.
- Backdrop blur: 0px.
- Corners are square. Rules are 1px. Red is never a large fill except a single signal block.
## Motion

Mechanical and exact. Elements wipe, crop, and settle their tracking. They arrive and stop. Nothing bounces, blurs, or overshoots.

Stagger between repeated elements: 0.06s.

Idle: One hairline travels a single column and loops. Everything else holds.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("wipe_x"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `wipe_x`

- Duration: 0.55s
- Ease: `cubic-bezier(0.77, 0, 0.18, 1)` (CSS `cubic-bezier(0.77, 0, 0.18, 1)`)
- Property: `scaleX`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Transform origin is the left edge. Use for rules, red blocks, and masks.

### `tracking_settle`

- Duration: 0.7s
- Ease: `cubic-bezier(0.22, 1, 0.36, 1)` (CSS `cubic-bezier(0.22, 1, 0.36, 1)`)
- Property: `letterSpacing` (em)
- Keyframes:
  - 0.00 → 0.22
  - 1.00 → 0.04
- Display words tighten into the grid. Do not fade them in from nothing.

### `rise_mask`

- Duration: 0.5s
- Ease: `cubic-bezier(0.22, 1, 0.36, 1)` (CSS `cubic-bezier(0.22, 1, 0.36, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 28
  - 1.00 → 0
- Reveal through a crop. The type moves up and the mask stays put.

### `idle_rule`

- Duration: 3.2s
- Ease: `linear` (CSS `linear`)
- Property: `x` (px)
- Keyframes:
  - 0.00 → 0
  - 1.00 → 64
- A 1px rule travels one column, then loops. Type does not bob.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- 12 columns, 64px outer margin, 24px gutter on the 1920 canvas. Every edge lands on a column.
- The signal red appears once per frame: a square, a rule, or a single word.
- A mono index sits in the top safe margin, like 01 / 08. No pills, badges, or icons.
- Body copy is flush left, ragged right, never justified and never centered under a huge title.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- GridFrame: column lines in ink at low contrast, shown only when the beat is about structure.
- IndexMark: mono index plus a 10px red square.
- DisplayCrop: an oversized uppercase line revealed by rise_mask or wipe_x.
- Hairline: a 1px ink rule driven by wipe_x.

## Captions

Bottom margin, one line, flush left. A red square marks the current clause. The rest of the sentence is text_dim. No capsule behind the words.

## Do

- Align type and rules to the same column edges.
- Reveal type with a wipe, a crop, or a tracking settle.
- Leave more paper empty than you fill.

## Don't

- Do not round corners, add drop shadows, gradients, or glow.
- Do not bounce, overshoot, or ease with a spring.
- Do not use more than two type sizes in one frame.
- Do not center a paragraph.

