---
name: style-documentary
description: "Apply the Warm Documentary motion-graphic style from the motionstyle_documentary Python library when building an explainer, title card, or narration-synced video. Use when the user asks for documentary, ken burns, lower third, editorial film, warm narrative, names Warm Documentary, or the style id documentary. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Warm Documentary

Apply this when the picture should be Warm Documentary. A still, a slow push, and a lower third. The story is allowed to take its time.

## Rules agents miss

- If an element bounces, it has left the style.
- Ken Burns is a few percent of scale over the whole beat, not a punch-in.
- One still, one title treatment. A corner chip plus a lower third plus a title is too much.

The spec below is generated from `motionstyle_documentary`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Warm Documentary

Library: `motionstyle_documentary`
Style id: `documentary`

A still, a slow push, and a lower third. The story is allowed to take its time.

Best for: origin stories, interviews, narrative explainers, field notes.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #140E0A
bgRaised      #231710
surface       #1C140F
ink           #F6EFE4
text          #F3EBDF
textDim       #B6A494
primary       #E0A15A
primaryLight  #F0C48A
primaryDark   #B7793A
secondary     #8C3A2F
accent        #F3E6D4
danger        #A33B32
ok            #7E9A74
info          #C4A484
```

## Typography

- Display: Iowan Old Style, Palatino, Georgia, serif. Weight 600. Tracking -0.015em. Case: as written. Line height 1.05.
- Body: Iowan Old Style, Palatino, Georgia, serif. Weight 400. Tracking 0.000em. Case: as written. Line height 1.45.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.080em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 2px.
- Border: 0px solid #E0A15A.
- Shadow: `none`.
- Backdrop blur: 0px.
- Almost no chrome. A lower third is a flat primary bar or a simple rule, 2px radius at most. Photographs sit full-bleed or in a quiet frame.
## Motion

Slow. Pictures drift with a Ken Burns scale. Type fades. The lower third slides a short distance and stays. Nothing bounces, slams, or draws on like a diagram.

Stagger between repeated elements: 0s.

Idle: The still is still moving, very slowly, via ken_burns. Type holds.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("fade_in"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `fade_in`

- Duration: 0.6s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Use for titles and for the first moment of a still.

### `ken_burns`

- Duration: 8s
- Ease: `linear` (CSS `linear`)
- Property: `scale`
- Keyframes:
  - 0.00 → 1
  - 1.00 → 1.06
- Set the duration to the length of the beat when the beat is shorter or longer. Direction alternates: in, then out.

### `lower_third`

- Duration: 0.7s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 16
  - 1.00 → 0
- The bar also fades with fade_in. It does not travel in from offscreen.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- One still or one field of color per beat. Do not collage.
- Titles are serif, sentence case, often only a few words.
- The lower third carries a name or a place, in small mono or small serif, on a primary bar with ink text.
- Letterboxing is allowed. Busy lower-screen UI is not.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Still: a full-bleed image or a warm color field, always under ken_burns.
- Title: serif display, fade_in, placed on the left third, not dead center every time.
- LowerThird: primary bar, short slide, one line.
- Rule: a 1px accent line used in place of a bar when the frame is already quiet.

## Captions

The lower third is the caption. Highlight the current phrase in accent if the narration must be readable. Do not add a bouncing karaoke pill on top of it.

## Do

- Let a still last as long as the sentence.
- Alternate Ken Burns direction between beats so the push does not feel like a zoom bug.
- Use secondary sparingly, as a quiet color in a still's grade, not as UI.

## Don't

- Do not use springs, slams, or draw-on strokes.
- Do not put charts, isometric blocks, or neon in this style.
- Do not center every title.
- Do not cut the still every two seconds.

