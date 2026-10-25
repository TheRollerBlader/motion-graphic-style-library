# Style Guide — Soft Glass

Library: `motionstyle_glass`
Style id: `glass`

Frosted panels float on a deep field. Motion is slow enough to feel expensive.

Best for: AI products, fintech, calm explainers, feature tours.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #0C1024
bgRaised      #171C36
surface       #F4F7FF
ink           #F7F8FF
text          #F4F6FF
textDim       #B7C0DC
primary       #A7B4FF
primaryLight  #D5DCFF
primaryDark   #6E7CFF
secondary     #6E7CFF
accent        #F2B8FF
danger        #FF8B9A
ok            #8EF0C4
info          #9FD4FF
glow          #7C6CFF
field         #24164A
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 560. Tracking -0.020em. Case: as written. Line height 1.0.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 450. Tracking 0.000em. Case: as written. Line height 1.45.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.020em. Case: as written. Line height 1.3.

## Shape and shadow

- Corner radius: 28px.
- Border: 1px solid #FFFFFF.
- Shadow: `0 24px 60px rgba(4, 6, 20, 0.35)`.
- Backdrop blur: 28px.
- Panels fill surface at 16% opacity over a 28px backdrop blur. The border is white at 22% opacity. Do not paint panels as solid white.
## Motion

Float, don't snap. Panels rise a short distance and fade. Nothing overshoots. Blur on the backdrop stays constant. Do not animate the blur radius.

Stagger between repeated elements: 0.1s.

Idle: Held panels drift up and down by a few pixels on a long loop. Background orbs drift even more slowly.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `panel`: stiffness 140, damping 22, mass 1.

### Clips

Sample a clip with `sample_clip(style.clip("card_y"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `card_y`

- Duration: 0.8s
- Ease: `cubic-bezier(0.22, 1, 0.36, 1)` (CSS `cubic-bezier(0.22, 1, 0.36, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 28
  - 1.00 → 0
- Short rise. The panel should feel placed, not dropped.

### `card_opacity`

- Duration: 0.6s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Starts with card_y. Do not fade the whole frame, only the panel.

### `idle_float`

- Duration: 4.5s
- Ease: `linear` (CSS `linear`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 0
  - 0.50 → -8
  - 1.00 → 0
- Loop the held panel. Amplitude stays inside 8px.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Background is a deep field with two or three large, soft orbs in primary, accent, and glow. Orbs are out of focus, never hard circles.
- One main panel per beat. A second panel only if the sentence is a comparison.
- Labels are small, text_dim, and sit just above the panel's title.
- Icons are thin strokes in ink, not filled glyphs and not emoji.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Field: background plus two drifting orbs. This is not a flat color.
- GlassPanel: radius, blur, 16% surface fill, 1px white border at 22% opacity.
- Eyebrow: 13px text_dim label, tracking 0.08em, uppercase.
- DisplayTitle: one line inside the panel, weight 560, never uppercase.

## Captions

A slim glass bar along the bottom safe margin. Current word is ink. Surrounding words are text_dim. The bar uses the same blur and border as GlassPanel, at a smaller radius of 16px.

## Do

- Keep contrast by putting type on the panel, not directly on a bright orb.
- Use accent sparingly, usually one number or one keyword.
- Let scenes breathe. Empty field around the panel is part of the style.

## Don't

- Do not use hard offset shadows, thick black borders, or 0px radius.
- Do not bounce or use a snappy spring.
- Do not stack more than two panels.
- Do not animate backdrop blur.
