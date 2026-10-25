---
name: style-neon
description: "Apply the Neon Night motion-graphic style from the motionstyle_neon Python library when building an explainer, title card, or narration-synced video. Use when the user asks for neon, synthwave, glow type, night city, cyber glow, names Neon Night, or the style id neon. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Neon Night

Apply this when the picture should be Neon Night. Two tubes of light on a black street. They flicker on, then hold a pulse.

## Rules agents miss

- Two glow colors maximum in a frame: magenta and cyan.
- The flicker clip plays once. Idle is the pulse.
- If the background is light, stop and switch styles. Neon does not sit on paper.

The spec below is generated from `motionstyle_neon`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Neon Night

Library: `motionstyle_neon`
Style id: `neon`

Two tubes of light on a black street. They flicker on, then hold a pulse.

Best for: launches, games, music, nightlife products.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #07060F
bgRaised      #120E1C
surface       #120E1C
ink           #F8F6FF
text          #F8F6FF
textDim       #9A93B0
primary       #FF2BD6
primaryLight  #FF8AE8
primaryDark   #C0009A
secondary     #8A7CFF
accent        #27F2FF
danger        #FF2BD6
ok            #B6FF3C
info          #27F2FF
```

## Typography

- Display: Arial Black, Impact, Helvetica Neue, sans-serif. Weight 900. Tracking 0.080em. Case: uppercase. Line height 0.9.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking 0.040em. Case: as written. Line height 1.4.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.120em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 2px.
- Border: 1.5px solid #27F2FF.
- Shadow: `0 0 16px #27F2FF`.
- Backdrop blur: 0px.
- Borders are the neon tube: 1.5px accent or primary, plus a matching glow. Filled panels are rare. Pills can go fully round. Do not frost the panel like glass.
## Motion

A tube flickers on, then the glow breathes. The flicker is short and happens once. The pulse is the idle, not another flicker.

Stagger between repeated elements: 0.05s.

Idle: The tube's glow radius eases between about 10px and 18px. The word stays sharp on top.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("flicker"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `flicker`

- Duration: 0.45s
- Ease: `linear` (CSS `linear`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 0.15 → 1
  - 0.22 → 0.15
  - 0.35 → 1
  - 1.00 → 1
- Play once on entrance. Do not loop the off frame.

### `glow`

- Duration: 0.45s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `blur` (px)
- Keyframes:
  - 0.00 → 2
  - 1.00 → 16
- This is the glow radius, not a backdrop blur. Apply it to a duplicate of the stroke sitting behind the sharp tube.

### `idle_pulse`

- Duration: 1.8s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 1
  - 0.50 → 1.03
  - 1.00 → 1
- Loop the glow's strength or the scale. Do not restroke the word.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Background stays near black. A few perspective lines in text_dim at 25% opacity are enough city.
- Primary magenta and accent cyan are the two tubes. Do not introduce a third glow color in the same frame.
- Display type is uppercase and tracked out. It is the sign.
- Ok green is a status pip, not a fill.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Night: background plus optional one-point perspective lines.
- TubeWord: display type, flicker then glow, sharp ink copy on top of the blurred copy.
- TubeRule: a horizontal or circular stroke in accent, same flicker and glow.
- SignBox: 2px radius frame in accent, used once, not around every label.

## Captions

Small mono line, text_dim, under the sign. The current word switches to accent. No filled caption bar.

## Do

- Keep a sharp copy of every glowing stroke so the word stays readable.
- Flicker once, then pulse.
- Leave the frame mostly black. Neon needs the dark.

## Don't

- Do not use this style for finance, medicine, or anything that should feel careful.
- Do not fill large rectangles with magenta.
- Do not loop the flicker. It reads as a broken sign.
- Do not add glass blur behind the type.

