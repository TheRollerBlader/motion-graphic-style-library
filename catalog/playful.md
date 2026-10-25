# Style Guide — Playful Flat

Library: `motionstyle_playful`
Style id: `playful`

Round shapes, a short hop, and colors that feel like stickers.

Best for: onboarding, consumer apps, friendly explainers, first-run tours.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #FFF7F1
bgRaised      #FFE8D6
surface       #FFFFFF
ink           #241C18
text          #241C18
textDim       #7A6A62
primary       #FF6B57
primaryLight  #FF9B8A
primaryDark   #E14B38
secondary     #1FA7A0
accent        #FFC857
danger        #E14B38
ok            #1FA7A0
info          #5B6CFF
```

## Typography

- Display: Avenir Next Rounded, Arial Rounded MT Bold, Nunito, sans-serif. Weight 800. Tracking -0.020em. Case: as written. Line height 1.0.
- Body: Avenir Next Rounded, Nunito, Helvetica Neue, sans-serif. Weight 600. Tracking 0.000em. Case: as written. Line height 1.35.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.020em. Case: as written. Line height 1.2.

## Shape and shadow

- Corner radius: 28px.
- Border: 0px solid #241C18.
- Shadow: `0 8px 0 #F0C2B4`.
- Backdrop blur: 0px.
- The shadow is a short solid offset in a tint of the background, not a blur and not black. Shapes are squircles and circles.
## Motion

Squash and stretch, then a small overshoot. Elements hop into place one after another. The idle is a bob, not a spin.

Stagger between repeated elements: 0.07s.

Idle: The hero shape bobs six pixels. Friends stay still so the frame does not bounce everywhere.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `pop`: stiffness 280, damping 12, mass 0.7.

### Clips

Sample a clip with `sample_clip(style.clip("pop_scale"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `pop_scale`

- Duration: 0.48s
- Ease: `ease-out-back` (CSS `cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 0.4
  - 1.00 → 1
- Origin center. The back ease provides the overshoot. Do not add a second bounce keyframe.

### `squash`

- Duration: 0.48s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `scaleX`
- Keyframes:
  - 0.00 → 1.18
  - 1.00 → 1
- Pair with scaleY moving from 0.82 to 1 so volume feels constant.

### `idle_bob`

- Duration: 1.4s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 0
  - 0.50 → -6
  - 1.00 → 0
- Loop the hero only.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- Background is warm paper. Shapes sit on it like stickers.
- Use three fills at most in one frame, chosen from primary, secondary, accent, and info.
- Faces, if any, are two dots and a short line. No realistic illustration.
- Buttons and chips use the same radius and the same short shadow.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- Sticker: squircle or circle, flat fill, short shadow, pop_scale plus squash.
- HeroTitle: rounded display face, ink, one line.
- DotRow: a repeated sticker staggered by stagger_s.
- Chip: a small surface or accent sticker used as a label.

## Captions

A white sticker along the bottom with the short shadow. Current word is primary. The caption does not use a thin sans if the title is rounded. Match the rounded face.

## Do

- Squash on the way in, settle to a circle or squircle, then bob only the hero.
- Keep outlines off. Color edges are enough.
- Time the hops to the beats of the sentence.

## Don't

- Do not use black brutalist shadows, glass, or neon glow.
- Do not rotate stickers more than a few degrees.
- Do not fill the frame edge to edge. The paper margin is the smile.
- Do not use this style for bad news, legal, or medical content.
