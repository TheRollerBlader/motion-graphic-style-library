# Style Guide — Isometric Studio

Library: `motionstyle_isometric`
Style id: `isometric`

Clay-colored blocks assemble into the system you are explaining.

Best for: systems, architecture, pipelines, product maps.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #E6E1D8
bgRaised      #F7F4EF
surface       #F4EFE6
ink           #2B2A28
text          #2B2A28
textDim       #6E675F
primary       #E07A5F
primaryLight  #F0A48F
primaryDark   #C45B42
secondary     #3D405B
accent        #81B29A
danger        #C44536
ok            #81B29A
info          #3D5A80
sand          #F2CC8F
clay          #E07A5F
sage          #81B29A
```

## Typography

- Display: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 700. Tracking -0.020em. Case: as written. Line height 1.0.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 500. Tracking 0.000em. Case: as written. Line height 1.4.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.040em. Case: uppercase. Line height 1.2.

## Shape and shadow

- Corner radius: 14px.
- Border: 0px solid #2B2A28.
- Shadow: `0 18px 30px rgba(40, 36, 30, 0.16)`.
- Backdrop blur: 0px.
- Labels are soft rounded rectangles. The isometric objects themselves are hard geometry with three faces: top, left, right. Contact shadows are ellipses on the ground, not drop shadows copied onto the type.
## Motion

Blocks drop onto the ground plane and settle. Later blocks wait their stagger. Nothing spins in true 3D. The camera is locked to the isometric angle.

Stagger between repeated elements: 0.08s.

Idle: The hero block lifts four pixels and returns. Contact shadows stay on the floor.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `block`: stiffness 300, damping 24, mass 1.

### Clips

Sample a clip with `sample_clip(style.clip("block_y"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `block_y`

- Duration: 0.5s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → -48
  - 1.00 → 0
- Vertical in screen space, which reads as lowering onto the floor.

### `block_scale`

- Duration: 0.5s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 0.94
  - 1.00 → 1
- A small settle with block_y. No overshoot past 1.

### `idle_bob`

- Duration: 3.6s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 0
  - 0.50 → -4
  - 1.00 → 0
- Only the hero block bobs. The rest of the assembly stays put.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Ground is a warm paper color. A faint ellipse under the group is the floor, not a horizon line.
- Three face tones per object: light top, mid left, dark right, all mixed from one palette color.
- Labels sit beside objects, not on top of them, in a surface chip with the soft shadow.
- Arrows between blocks are short and flat, in ink, drawn after both blocks have landed.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Floor: background plus one soft contact ellipse.
- IsoBlock: three faces, entered with block_y and block_scale.
- LabelChip: surface fill, 14px radius, one line of body type.
- Connector: a short ink path that draws on after its two blocks exist.

## Captions

A quiet line under the floor group, ink on the paper, no card. The current noun is primary. Do not cover the blocks with the caption.

## Do

- Build the system in the order the narration names the parts.
- Keep the isometric angle consistent for the whole video.
- Use sand, clay, sage, and secondary so objects are distinguishable without labels doing all the work.

## Don't

- Do not rotate the camera or tumble a cube.
- Do not use neon, thick comic borders, or glass.
- Do not stack type on the top face unless it is a one-word label.
- Do not drop every block on the same frame.
