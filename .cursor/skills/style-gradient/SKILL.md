---
name: style-gradient
description: "Apply the Liquid Gradient motion-graphic style from the motionstyle_gradient Python library when building an explainer, title card, or narration-synced video. Use when the user asks for gradient, mesh gradient, liquid, blob, aurora, brand film, names Liquid Gradient, or the style id gradient. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Liquid Gradient

Apply this when the picture should be Liquid Gradient. Color fields drift. One line of type is enough.

## Rules agents miss

- One line of type is the layout. A card grid means the wrong style.
- Blob motion is an 8 second loop with staggered phases, not a one-shot entrance.
- White type only. Colored type disappears into the field.

The spec below is generated from `motionstyle_gradient`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Liquid Gradient

Library: `motionstyle_gradient`
Style id: `gradient`

Color fields drift. One line of type is enough.

Best for: brand films, premium product, wellness, launch titles.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #1A1030
bgRaised      #2A1848
surface       #FFFFFF
ink           #FFFFFF
text          #FFFFFF
textDim       #F3E9FF
primary       #FFFFFF
primaryLight  #FFFFFF
primaryDark   #E4D8FF
secondary     #6D5BFF
accent        #FFB199
danger        #FF6B8A
ok            #9EF0D0
info          #69D2FF
violet        #6D5BFF
peach         #FFB199
blue          #69D2FF
magenta       #FF6BCB
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking -0.030em. Case: as written. Line height 1.0.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 400. Tracking 0.010em. Case: as written. Line height 1.45.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.080em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 32px.
- Border: 0px solid #FFFFFF.
- Shadow: `none`.
- Backdrop blur: 40px.
- Blobs are large ellipses in the spot colors at about 80% opacity, blurred so edges disappear. Type sits in white with no card. A frost panel is allowed only when body copy would otherwise fail contrast.
## Motion

Ambient and slow. Blobs drift on long loops. Type rises a few pixels and fades. Nothing snaps, slams, or draws on.

Stagger between repeated elements: 0.12s.

Idle: The field never holds still. Type, once in, holds.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("fade_up"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `fade_up`

- Duration: 0.8s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 12
  - 1.00 → 0
- Pair with an opacity move from 0 to 1 over the same duration. The distance stays short.

### `blob_drift`

- Duration: 8s
- Ease: `linear` (CSS `linear`)
- Property: `x` (px)
- Keyframes:
  - 0.00 → -24
  - 0.50 → 24
  - 1.00 → -24
- Loop. Each blob gets its own phase so they do not travel as a group.

### `idle_drift`

- Duration: 8s
- Ease: `linear` (CSS `linear`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 0
  - 0.50 → 18
  - 1.00 → 0
- Vertical companion to blob_drift. Same duration, offset phase.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Three or four blobs cover the frame. The background color only shows in the gaps.
- One display line. A second line, if needed, is small and text_dim.
- No icons, no cards, no progress bars, unless the sentence is a single number.
- If a number is the idea, set it in the display face, white, and let the field move behind it.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Field: background plus three blurred spot-color blobs on blob_drift and idle_drift.
- QuietTitle: white display line, fade_up, often centered.
- Whisper: a smaller text_dim line under the title, delayed by stagger_s.
- Frost: optional 32px-radius panel at 12% white, blur 24, only for a sentence that cannot sit on the color.

## Captions

Avoid a caption bar. Burn the current phrase as the QuietTitle, or set a whisper line. If a full sentence must sit on screen, use Frost so the type stays white and readable.

## Do

- Keep type to a handful of words.
- Move the field even when the type is holding.
- Pick blob colors from the spots. Do not add a new hue.

## Don't

- Do not use hard shadows, thick borders, or sharp-edged shapes.
- Do not slam, bounce, or wipe.
- Do not put a dashboard, a chart, or a paragraph on this field.
- Do not stop the blobs to make the type easier. Fix contrast with Frost instead.

