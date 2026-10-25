---
name: style-comic
description: "Apply the Comic Pop motion-graphic style from the motionstyle_comic Python library when building an explainer, title card, or narration-synced video. Use when the user asks for comic, pop art, halftone, speech bubble, ben-day, names Comic Pop, or the style id comic. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Comic Pop

Apply this when the picture should be Comic Pop. A panel, a burst, and a bubble. The point lands like a sound effect.

## Rules agents miss

- The outline is 4px ink. A borderless shape has left the style.
- Shake plays once, on the hit. Idle is still.
- Halftone stays behind the burst. If it touches the letters, pull it back.

The spec below is generated from `motionstyle_comic`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Comic Pop

Library: `motionstyle_comic`
Style id: `comic`

A panel, a burst, and a bubble. The point lands like a sound effect.

Best for: social explainers, contrasts, punchy education, wrong versus right.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #FFF7E8
bgRaised      #FFE14A
surface       #FFFFFF
ink           #141414
text          #141414
textDim       #3A3A3A
primary       #FF3B30
primaryLight  #FF7A72
primaryDark   #C4121A
secondary     #1C6BFF
accent        #FFE14A
danger        #FF3B30
ok            #1F9D55
info          #1C6BFF
```

## Typography

- Display: Comic Sans MS, Comic Neue, cursive. Weight 700. Tracking 0.000em. Case: uppercase. Line height 0.9.
- Body: Comic Sans MS, Comic Neue, cursive. Weight 700. Tracking 0.000em. Case: as written. Line height 1.25.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 700. Tracking 0.040em. Case: uppercase. Line height 1.1.

## Shape and shadow

- Corner radius: 18px.
- Border: 4px solid #141414.
- Shadow: `6px 6px 0 #141414`.
- Backdrop blur: 0px.
- Every panel, bubble, and burst has a 4px ink outline and a hard shadow. Halftone dots sit behind the burst, in primary or secondary at about 35% opacity, not over the type.
## Motion

A hit. The burst scales in with a short overshoot, the bubble follows, and a two-step shake sells the impact. Then it holds. Do not keep shaking.

Stagger between repeated elements: 0.06s.

Idle: Halftone dots do not animate. A held panel stays. If the beat is long, blink a small star once. Do not loop the shake.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `impact`: stiffness 640, damping 14, mass 0.6.

### Clips

Sample a clip with `sample_clip(style.clip("pop_scale"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `pop_scale`

- Duration: 0.36s
- Ease: `ease-out-back` (CSS `cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 0.3
  - 1.00 → 1
- Use on the burst and on sound-effect words.

### `shake_x`

- Duration: 0.28s
- Ease: `linear` (CSS `linear`)
- Property: `x` (px)
- Keyframes:
  - 0.00 → 0
  - 0.25 → -8
  - 0.50 → 6
  - 0.75 → -3
  - 1.00 → 0
- Play once as the burst lands. Do not loop it.

### `bubble_in`

- Duration: 0.32s
- Ease: `ease-out-back` (CSS `cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 0.7
  - 1.00 → 1
- Starts a stagger after the burst. Origin is the tail of the bubble.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- The frame is a panel: 4px ink border inset from the canvas edge.
- One burst per beat for the idea that should feel like a hit. The other idea can be a plain panel.
- Speech bubbles have a tail aimed at the thing speaking. Tails are part of the shape, same border.
- Sound-effect words (the display face, uppercase, primary or accent) are allowed and encouraged.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Panel: full-frame ink border and hard shadow language, background paper or accent.
- Burst: a 12-point starburst, primary or accent fill, ink outline, pop_scale and a single shake_x.
- Bubble: white surface, 18px radius, tail, bubble_in.
- Halftone: dots behind the burst only.

## Captions

The speech bubble is the caption. Underline or recolor the current word in primary. Do not add a second caption bar outside the bubble.

## Do

- Stage contrasts as two panels or a burst against a quiet panel.
- Hit once, then hold so the line can be read.
- Keep the palette to paper, ink, red, blue, and yellow.

## Don't

- Do not use soft shadows, blur, or thin elegant type.
- Do not loop the shake.
- Do not cover the bubble text with halftone.
- Do not use this style for somber, legal, or medical stories.

