# Style Guide — Data Signal

Library: `motionstyle_signal`
Style id: `signal`

A dark instrument panel. Numbers count and charts draw while the sentence does.

Best for: metrics, research findings, earnings explainers, product analytics.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #070B16
bgRaised      #101828
surface       #0E1728
ink           #E8F1FF
text          #E7F0FA
textDim       #8AA0B8
primary       #3EE0FF
primaryLight  #A8F4FF
primaryDark   #1498B8
secondary     #7AA2FF
accent        #FFB020
danger        #FF5D73
ok            #3DDC97
info          #7AA2FF
grid          #17304A
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 600. Tracking -0.030em. Case: as written. Line height 0.95.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 450. Tracking 0.000em. Case: as written. Line height 1.4.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.020em. Case: as written. Line height 1.1.

## Shape and shadow

- Corner radius: 8px.
- Border: 1px solid #17304A.
- Shadow: `none`.
- Backdrop blur: 0px.
- Panels are flat surface fills with a 1px grid-colored border. Bars and lines are the picture. Do not put a glow on every series.
## Motion

Instrument-like. Bars grow from the baseline, lines draw left to right, and numerals count. Easing arrives and stops. No bounce.

Stagger between repeated elements: 0.06s.

Idle: A caret or the latest point pulses opacity between 0.45 and 1. Axes do not move.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("bar_grow"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `bar_grow`

- Duration: 0.7s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `scaleY`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Transform origin is the baseline. Stagger neighboring bars.

### `line_draw`

- Duration: 0.9s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `strokeOffset`
- Keyframes:
  - 0.00 → 1
  - 1.00 → 0
- Draw the series in the direction of time, left to right.

### `count_up`

- Duration: 0.8s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `progress`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Map progress onto the displayed number. Do not spin digits like a slot machine.

### `tick_in`

- Duration: 0.25s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Axis ticks and the end dot appear as the series reaches them.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- A faint grid in the grid spot color sits behind the plot, not across the whole frame.
- One highlighted series uses primary. A comparison series uses secondary. Accent marks the annotated point, once.
- Units and axis labels are mono and text_dim.
- The big number and the chart must agree. Do not show 32% beside a bar that reads as almost full unless the scale says so.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- PlotFrame: surface panel, grid lines, baseline.
- Bar: scaleY from the baseline, primary or secondary.
- SeriesLine: a polyline driven by line_draw, with an end dot.
- BigNumber: mono or display numeral driven by count_up, with a text_dim unit.

## Captions

Bottom of the frame, mono, outside the plot. The current word is primary. Do not draw the caption through the chart.

## Do

- Reveal the chart in the same order the sentence makes the claim.
- Label the unit before or as the number counts, not three seconds later.
- Use accent for the one point the narration calls out.

## Don't

- Do not bounce bars past their final value.
- Do not use 3D pies, gradients on bars, or decorative glow.
- Do not plot a series that the narration does not mention.
- Do not use comic or chalk type for the figures.
