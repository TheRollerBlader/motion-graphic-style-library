# Style Guide — Blueprint

Library: `motionstyle_blueprint`
Style id: `blueprint`

A plan on navy paper. Lines draw, then the dimensions appear.

Best for: engineering, how it's built, process, technical explainers.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #071E36
bgRaised      #0A2744
surface       #071E36
ink           #E5F6FF
text          #E5F6FF
textDim       #8FB4C9
primary       #7FDBFF
primaryLight  #C7F1FF
primaryDark   #3AA7CC
secondary     #F2C14E
accent        #FFFFFF
danger        #FF8A7A
ok            #9BE7C4
info          #7FDBFF
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking 0.140em. Case: uppercase. Line height 1.0.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 400. Tracking 0.040em. Case: as written. Line height 1.4.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 500. Tracking 0.080em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 0px.
- Border: 1px solid #7FDBFF.
- Shadow: `none`.
- Backdrop blur: 0px.
- Everything is a stroke. Large fills, if any, are primary at about 8% opacity. Corners are square. Dimension text is secondary, the construction yellow.
## Motion

A draftsman's hand. The outline draws, ticks appear when the line reaches them, then the label fades. No bounce and no fill animation.

Stagger between repeated elements: 0.04s.

Idle: A small cursor or an endpoint blinks. Finished lines hold.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

No springs. Use the clip easings only.

### Clips

Sample a clip with `sample_clip(style.clip("stroke_draw"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `stroke_draw`

- Duration: 1.05s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `strokeOffset`
- Keyframes:
  - 0.00 → 1
  - 1.00 → 0
- Draw closed shapes as a single path so the line does not appear on all four sides at once.

### `tick_in`

- Duration: 0.2s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Start when stroke_draw reaches the corner or measurement the tick belongs to.

### `label_in`

- Duration: 0.35s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `opacity`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Labels follow ticks. They do not lead the line.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- A fine grid covers the sheet in primary at about 12% opacity.
- A title block sits in one corner: style name, sheet number, mono.
- Dimension strings use secondary and sit off the object, with extension lines.
- Callouts are leaders, not speech bubbles.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Sheet: navy background plus the fine grid and a title block.
- PlanStroke: square-cornered path driven by stroke_draw.
- Dimension: extension lines, ticks, and a yellow measure driven by tick_in and label_in.
- Leader: a short elbow line pointing at a part, label at the end.

## Captions

Mono, bottom margin, inside the sheet border. Wrap the current phrase in square brackets. Color the brackets and the current phrase primary. The rest is text_dim.

## Do

- Explain by drawing the object, then labeling the part just drawn.
- Keep strokes at one or two weights: hairline for the grid, 2px for the object.
- Use yellow only for dimensions and warnings.

## Don't

- Do not fill shapes with solid cyan.
- Do not round the plan geometry.
- Do not use photos, glass, or soft shadows.
- Do not drop the whole schematic in already drawn.
