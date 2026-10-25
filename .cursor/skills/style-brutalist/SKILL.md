---
name: style-brutalist
description: "Apply the Neo-Brutalist motion-graphic style from the motionstyle_brutalist Python library when building an explainer, title card, or narration-synced video. Use when the user asks for neo-brutalist, neo brutalism, brutalist, hard shadow, terracotta cards, names Neo-Brutalist, or the style id brutalist. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Neo-Brutalist

Apply this when the picture should be Neo-Brutalist. Chunky cards, hard shadows, and type that behaves like an object.

## Rules agents miss

- If a shadow is blurred, it is no longer this style. Redraw it as a solid offset.
- One title treatment per beat. Corner chip or title card.
- Springs are shared. Do not hand-tune a new easing for a single scene.

The spec below is generated from `motionstyle_brutalist`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Neo-Brutalist

Library: `motionstyle_brutalist`
Style id: `brutalist`

Chunky cards, hard shadows, and type that behaves like an object.

Best for: teaching explainers, product how-tos, opinionated software, classroom-to-camera lessons.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg               #1A1A2E
bgRaised         #23233A
surface          #F7F4F0
ink              #0B0B12
text             #F7F4F0
textDim          #A0978C
primary          #CC785C
primaryLight     #E09880
primaryDark      #A85A40
secondary        #4A5568
accent           #D4845A
danger           #E35D5D
ok               #5CB88A
info             #5B8DEF
cream_muted      #E8E2DA
secondary_light  #718096
secondary_dark   #2D3748
```

## Typography

- Display: Avenir Next, Segoe UI, Helvetica Neue, Arial, sans-serif. Weight 800. Tracking 0.040em. Case: uppercase. Line height 0.92.
- Body: Avenir Next, Segoe UI, Helvetica Neue, Arial, sans-serif. Weight 700. Tracking 0.010em. Case: as written. Line height 1.3.
- Mono: SF Mono, ui-monospace, Menlo, Monaco, Consolas, monospace. Weight 700. Tracking 0.020em. Case: as written. Line height 1.2.

## Shape and shadow

- Corner radius: 24px.
- Border: 5px solid #0B0B12.
- Shadow: `8px 8px 0px 0px #0B0B12`.
- Backdrop blur: 0px.
- The shadow is a flat offset block with no blur. Small elements use 5px 5px. Large cards use 12px 12px. Pills use a 3px border and a fully round radius.
## Motion

Physical and springy. Cards pop into their shadow. The shadow grows with the card, it is not a fade. Held cards rock by a fraction of a degree.

Stagger between repeated elements: 0.07s.

Idle: Held cards rock under half a degree. Pills do not rock if a card already is.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `chip`: stiffness 420, damping 20, mass 0.8.
- `panel`: stiffness 260, damping 18, mass 1.

### Clips

Sample a clip with `sample_clip(style.clip("pop_scale"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `pop_scale`

- Duration: 0.45s
- Ease: `ease-out-back` (CSS `cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 0.86
  - 1.00 → 1
- Use the panel spring for cards and the chip spring for pills. The overshoot is short.

### `shadow_drop`

- Duration: 0.45s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `shadowOffset` (px)
- Keyframes:
  - 0.00 → 0
  - 1.00 → 8
- Grows the hard shadow from nothing to 8px. Large cards end at 12. Pills end at 5.

### `idle_rock`

- Duration: 3.4s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `rotate` (deg)
- Keyframes:
  - 0.00 → -0.4
  - 0.50 → 0.4
  - 1.00 → -0.4
- Loop. A held card is never frozen.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Every surface is a card: ink border, cream or colored fill, hard shadow.
- Pick one header per beat. Either a corner chip or a big title card, never both.
- The corner chip is uppercase, primary or accent, top-left, with a hard text shadow.
- Semantic colors (danger, ok, info) are for state, not decoration.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- HardCard: 5px ink border, 24px radius, hard shadow. Fill is surface, primary, or info.
- Pill: 3px border, fully round, chip spring, smaller shadow.
- TitleCard: display type inside a colored HardCard. Optional text_dim line under it.
- CornerChip: small uppercase label. Do not combine with TitleCard.

## Captions

Karaoke inside a HardCard along the bottom. The full sentence is visible. The current word is primary. The card uses the same border and shadow as everything else.

## Do

- Reuse HardCard, Pill, and one title treatment for every beat.
- Drive entrances with pop_scale and shadow_drop together.
- Keep the background flat navy. Do not put a gradient behind the cards.

## Don't

- Do not use soft shadows, glow, or backdrop blur.
- Do not mix a corner chip with a centered title card.
- Do not leave a beat on a blank background.
- Do not invent hex values outside the palette.

