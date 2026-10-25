# Style Guide — Kinetic Type

Library: `motionstyle_kinetic`
Style id: `kinetic`

One word hits, then the next. The sentence is the animation.

Best for: hooks, title cards, manifesto lines, social openers.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: 1920×1080 at 30fps. Keep content inside a 96px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

```
bg            #090909
bgRaised      #141414
surface       #090909
ink           #F4F4F0
text          #F4F4F0
textDim       #9A9A92
primary       #F5E642
primaryLight  #FFF38A
primaryDark   #C9B400
secondary     #F4F4F0
accent        #F5E642
danger        #FF5A36
ok            #B6F25C
info          #8AB4FF
```

## Typography

- Display: Arial Black, Impact, Haettenschweiler, sans-serif. Weight 900. Tracking -0.030em. Case: uppercase. Line height 0.82.
- Body: Helvetica Neue, Helvetica, Arial, sans-serif. Weight 700. Tracking 0.080em. Case: uppercase. Line height 1.1.
- Mono: SF Mono, ui-monospace, Menlo, Consolas, monospace. Weight 600. Tracking 0.040em. Case: uppercase. Line height 1.0.

## Shape and shadow

- Corner radius: 0px.
- Border: 0px solid #F4F4F0.
- Shadow: `none`.
- Backdrop blur: 0px.
- No cards. A yellow rule or a yellow word is the only chrome.
## Motion

Heavy and fast. Words scale down into place and land with a short overshoot. The underline finishes after the word, not before it.

Stagger between repeated elements: 0.08s.

Idle: The held word breathes by about two percent. The underline stays.

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

- `impact`: stiffness 520, damping 18, mass 0.7.

### Clips

Sample a clip with `sample_clip(style.clip("slam_scale"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

### `slam_scale`

- Duration: 0.42s
- Ease: `ease-out-back` (CSS `cubic-bezier(0.34, 1.56, 0.64, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 1.22
  - 1.00 → 1
- Origin is the word's center. One word per slam.

### `word_y`

- Duration: 0.42s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `y` (px)
- Keyframes:
  - 0.00 → 22
  - 1.00 → 0
- Pairs with slam_scale. Do not also fade from 0 if the scale read is already clear.

### `underline_wipe`

- Duration: 0.28s
- Ease: `ease-out` (CSS `cubic-bezier(0.16, 1, 0.3, 1)`)
- Property: `scaleX`
- Keyframes:
  - 0.00 → 0
  - 1.00 → 1
- Origin left, under the word that just landed. Color is primary.

### `idle_pulse`

- Duration: 1.6s
- Ease: `ease-in-out` (CSS `cubic-bezier(0.65, 0, 0.35, 1)`)
- Property: `scale`
- Keyframes:
  - 0.00 → 1
  - 0.50 → 1.025
  - 1.00 → 1
- A breath on the held word. Do not loop the slam.

Property units: `opacity`, `x` px, `y` px, `scale`, `scaleX`, `scaleY`, `rotate` deg, `letterSpacing` em, `strokeOffset`, `shadowOffset` px, `blur` px, `progress`.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

- One idea per frame, usually one to four words. If the sentence is longer, advance word by word.
- The emphasized word is primary yellow. Supporting words are ink.
- Safe margins stay large. Type can bleed only when it is the slam itself.
- No icons, windows, or device frames. If a symbol is required, set it in the display face.

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

- SlamWord: display word driven by slam_scale and word_y.
- SupportLine: smaller uppercase words in text_dim, staggered by stagger_s.
- YellowRule: underline_wipe in primary, thickness about 0.08 of the word height.
- HoldBreath: idle_pulse on the word that should stay after the line is done.

## Captions

Kinetic frames usually are the caption. Do not add a second subtitle line. If narration must be visible, set the current word in primary and the rest in text_dim, in the display face, not a small UI font.

## Do

- Time each slam to the syllable being spoken.
- Use scale and position. A pure opacity fade is not kinetic type.
- Keep the background flat so the word reads at a glance.

## Don't

- Do not put a paragraph on screen.
- Do not use rounded cards, glass, or soft shadows.
- Do not slam two words at the same time.
- Do not animate tracking so wide that the word breaks apart.
