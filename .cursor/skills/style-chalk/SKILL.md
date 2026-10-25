---
name: style-chalk
description: "Apply the Chalk Classroom motion-graphic style from the motionstyle_chalk Python library when building an explainer, title card, or narration-synced video. Use when the user asks for chalk, chalkboard, classroom, hand drawn lesson, blackboard, names Chalk Classroom, or the style id chalk. Supplies the palette, type, shape, motion clips, captions, and scene grammar."
---

# Chalk Classroom

Apply this when the picture should be Chalk Classroom. A dark board, a yellow stick of chalk, and lines that draw themselves.

## Rules agents miss

- If the type is Helvetica, it is the wrong style. Use the chalk face.
- Strokes draw on. They do not fade in as finished shapes.
- Yellow means now. Do not paint the whole diagram yellow.

The spec below is generated from `motionstyle_chalk`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

# Style Guide — Chalk Classroom

Library: `motionstyle_chalk`
Style id: `chalk`

A dark board, a yellow stick of chalk, and lines that draw themselves.

Best for: lessons, how-it-works, tutorials, classroom explainers.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #123127
bgRaised      #1A4334
surface       #16392C
ink           #F3EFE2
text          #F3EFE2
textDim       #C5D2C2
primary       #F2E37A
primaryLight  #FFF3B0
primaryDark   #CDB84A
secondary     #F2A3C7
accent        #9FD7C8
danger        #F0A08A
ok            #B7E3A1
info          #F2E37A
dust          #E7E2CC
```

## Typography

- Display: Chalkduster, Bradley Hand, Segoe Print, cursive. Weight 700. Tracking 0.010em. Case: as written. Line height 1.05.
- Body: Chalkduster, Bradley Hand, Segoe Print, cursive. Weight 500. Tracking 0.000em. Case: as written. Line height 1.35.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.000em. Case: as written. Line height 1.2.

## Shape and shadow

- Corner radius: 0px.
- Border: 0px solid #F3EFE2.
- Shadow: `none`.
- Backdrop blur: 0px.
- Strokes are 4 to 7px, slightly uneven, and capped round. A perfect vector circle is wrong unless you break it with a small hand wobble.
## Motion

Draw-on. Strokes reveal along their length, the way chalk leaves the stick. Words fade in only after the drawing they name has started. Dust settles. Nothing slams.

Stagger between repeated elements: 0.12s.

Idle: Dust motes pulse near the freshest line. Finished strokes stay put.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("stroke_draw"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `stroke_draw`

- Duration: 0.9s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `strokeOffset`
- Keyframes:
  - 0.00 → 1
  - 1.00 → 0
- 1 is hidden, 0 is fully drawn. Pair with a slightly wobbly path.

### `word_opacity`

- Duration: 0.4s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Start this when the related stroke is about halfway, not at the cut.

### `idle_dust`

- Duration: 2.8s
- Ease: `linear` (CSS `linear`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0.25
  - 0.50 → 0.55
  - 1.00 → 0.25
- A few dust specks near the last stroke. Loop. Do not flicker the whole board.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- The board is the whole frame. A faint wiped rectangle can mark the previous lesson. Do not float a card.
- Yellow chalk is the current idea. Pink is the aside. Mint is a supporting arrow or check.
- Underlines are drawn, not typed as a border.
- Leave the edges of the board a little darker than the center.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Board: background with a soft vignette and a handful of static dust specks.
- ChalkStroke: any line, circle, arrow, or box driven by stroke_draw.
- ChalkWord: display word in ink or primary, brought in with word_opacity.
- Aside: a short pink note, smaller, off to the side of the main drawing.

## Captions

The spoken line is written in chalk under the drawing. The current word is primary yellow. Do not put the caption in a pill or a sans-serif UI font.

## Do

- Draw the thing being named. An arrow, a circle, a tally, a simple face of a diagram.
- Start the stroke as the noun is spoken.
- Keep diagrams to a few marks. A board crammed with boxes is a slide, not chalk.

## Don't

- Do not use glass, gradients-as-fills, or hard UI shadows.
- Do not use a geometric sans for the lesson text.
- Do not pop elements in with a scale overshoot.
- Do not leave the board blank between sentences.

