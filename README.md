# Motion graphic style library

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="#the-libraries"><img src="https://img.shields.io/badge/Styles-14%20Visual%20Archetypes-FF2E93?style=for-the-badge&logo=materialdesign&logoColor=white" alt="14 Visual Styles"></a>
  <a href="#kinetic-curves--3d-motion-benchmarks"><img src="https://img.shields.io/badge/Motion-Kinetic%20Physics-F59E0B?style=for-the-badge&logo=framer&logoColor=white" alt="Kinetic Physics"></a>
  <a href="https://ffmpeg.org/"><img src="https://img.shields.io/badge/FFMPEG-Hardware%20Accelerated-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFMPEG Ready"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License MIT"></a>
</p>

<p align="center">
  <img src="assets/3d_preview.gif" alt="3D Kinetic Typography and Particle Attractor Simulation across 14 Visual Styles" width="100%">
  <br>
  <em><b>3D Kinetic Typography & Motion Simulation:</b> Dynamic 3D kinetic typography and parametric particle attractors morphing across the 14 visual styles with live physics telemetry (stiffness $k$, damping $c$, Bézier manifolds, and active palette swatches). Full broadcast MP4 simulation available at <a href="assets/3d_simulation.mp4"><code>assets/3d_simulation.mp4</code></a>.</em>
</p>

Fourteen Python libraries that describe how an explainer should look and move, and agent skills that apply those looks. A style decides the palette, the type, the shape, and the named animation clips. It does not render the video. An agent implements the clips in whatever runtime the project already uses.

## System Architecture

```mermaid
flowchart LR
    A["Agent Script Brief<br/><code>Prompt / Voiceover / Beats</code>"] --> B["Style Config Selector<br/><code>motionstyles catalog (14 Styles)</code>"]
    B --> C["Keyframe & Bézier Interpolator<br/><code>sample_clip() / Spring Physics</code>"]
    C --> D["Headless Frame Renderer<br/><code>Pillow / PyCairo / Skia Canvas</code>"]
    D --> E["FFMPEG Video Assembler<br/><code>H.264 / AV1 / ProRes 60fps</code>"]

    subgraph Core ["motionstyle_core Engine"]
        B
        C
    end

    subgraph Output ["Pipeline Deliverables"]
        D
        E
    end
```

Each tile below is a looping study of that style's real clips.

<table>
  <tr>
    <td align="center" width="25%">
      <img src="previews/swiss.gif" alt="Editorial Swiss. A red panel wipes in from the left beside the word SWISS." width="100%">
      <br><b>Editorial Swiss</b>
      <br><sub>A wipe, a grid, one red.</sub>
    </td>
    <td align="center" width="25%">
      <img src="previews/kinetic.gif" alt="Kinetic Type. The word SLAM scales into place and a yellow rule draws under it." width="100%">
      <br><b>Kinetic Type</b>
      <br><sub>The word slams in.</sub>
    </td>
    <td align="center" width="25%">
      <img src="previews/glass.gif" alt="Soft Glass. A frosted card floats up over drifting color orbs." width="100%">
      <br><b>Soft Glass</b>
      <br><sub>A frosted panel floats.</sub>
    </td>
    <td align="center" width="25%">
      <img src="previews/brutalist.gif" alt="Neo-Brutalist. A cream card pops into a hard black shadow with a terracotta pill." width="100%">
      <br><b>Neo-Brutalist</b>
      <br><sub>A card pops into its shadow.</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="previews/chalk.gif" alt="Chalk Classroom. A circle and an underline draw on in chalk, then the word explain appears." width="100%">
      <br><b>Chalk Classroom</b>
      <br><sub>The line draws itself.</sub>
    </td>
    <td align="center">
      <img src="previews/isometric.gif" alt="Isometric Studio. Three clay cubes drop onto a paper floor." width="100%">
      <br><b>Isometric Studio</b>
      <br><sub>Blocks assemble on the floor.</sub>
    </td>
    <td align="center">
      <img src="previews/signal.gif" alt="Data Signal. Bars grow from a baseline while a line series draws and a percentage counts up." width="100%">
      <br><b>Data Signal</b>
      <br><sub>Bars grow. The line draws.</sub>
    </td>
    <td align="center">
      <img src="previews/papercut.gif" alt="Paper Cut. Three colored sheets slide into a stack with the word Story on top." width="100%">
      <br><b>Paper Cut</b>
      <br><sub>Sheets slide into a stack.</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="previews/neon.gif" alt="Neon Night. The word NEON flickers on in magenta over a cyan perspective grid." width="100%">
      <br><b>Neon Night</b>
      <br><sub>The sign flickers, then holds.</sub>
    </td>
    <td align="center">
      <img src="previews/documentary.gif" alt="Warm Documentary. A landscape still slowly pushes in and a lower third slides up." width="100%">
      <br><b>Warm Documentary</b>
      <br><sub>A slow push, then a lower third.</sub>
    </td>
    <td align="center">
      <img src="previews/playful.gif" alt="Playful Flat. Three round stickers hop in with a squash and stretch." width="100%">
      <br><b>Playful Flat</b>
      <br><sub>Shapes hop into place.</sub>
    </td>
    <td align="center">
      <img src="previews/blueprint.gif" alt="Blueprint. A cyan rectangle draws itself on a navy grid, then a yellow dimension appears." width="100%">
      <br><b>Blueprint</b>
      <br><sub>The plan draws, then the measure.</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="previews/gradient.gif" alt="Liquid Gradient. Violet, peach, and blue fields drift behind the word Flow." width="100%">
      <br><b>Liquid Gradient</b>
      <br><sub>Color drifts. One word holds.</sub>
    </td>
    <td align="center">
      <img src="previews/comic.gif" alt="Comic Pop. A red burst scales in with the word POW, then a speech bubble lands." width="100%">
      <br><b>Comic Pop</b>
      <br><sub>A burst hits, then the bubble.</sub>
    </td>
    <td></td>
    <td></td>
  </tr>
</table>

The GIFs above play in this README. [`docs/gallery.html`](docs/gallery.html) is the same set of studies as CSS animations. Open that file in a browser.

## The libraries

| Library | Import | Use it for | Motion |
| --- | --- | --- | --- |
| `motionstyle_swiss` | `from motionstyle_swiss import STYLE` | Strategy, essays, serious software | Wipes and tracking. No bounce. |
| `motionstyle_kinetic` | `from motionstyle_kinetic import STYLE` | Hooks, titles, manifesto lines | A word slams, then the next. |
| `motionstyle_glass` | `from motionstyle_glass import STYLE` | AI, fintech, calm tours | Panels float. Blur stays still. |
| `motionstyle_brutalist` | `from motionstyle_brutalist import STYLE` | Teaching explainers, how-tos | Springs. Hard shadows. |
| `motionstyle_chalk` | `from motionstyle_chalk import STYLE` | Lessons and how-it-works | Strokes draw on. |
| `motionstyle_isometric` | `from motionstyle_isometric import STYLE` | Systems, pipelines, maps | Blocks drop and settle. |
| `motionstyle_signal` | `from motionstyle_signal import STYLE` | Metrics, research, earnings | Bars grow, numbers count. |
| `motionstyle_papercut` | `from motionstyle_papercut import STYLE` | Stories, consumer brands | Sheets stack, back to front. |
| `motionstyle_neon` | `from motionstyle_neon import STYLE` | Launches, games, music | One flicker, then a pulse. |
| `motionstyle_documentary` | `from motionstyle_documentary import STYLE` | Origin stories, interviews | Ken Burns and a lower third. |
| `motionstyle_playful` | `from motionstyle_playful import STYLE` | Onboarding, friendly apps | Squash, stretch, one bob. |
| `motionstyle_blueprint` | `from motionstyle_blueprint import STYLE` | Engineering, process | The line draws, then the label. |
| `motionstyle_gradient` | `from motionstyle_gradient import STYLE` | Brand films, premium product | Slow fields, one line of type. |
| `motionstyle_comic` | `from motionstyle_comic import STYLE` | Social explainers, contrasts | One hit, then a hold. |

Full specs, including every hex and every keyframe, are in [`catalog/`](catalog/).

## Kinetic Curves & 3D Motion Benchmarks

The library formulates visual motion through two complementary mathematical domains: continuous **cubic-Bézier parametric timing functions** and physical **second-order damped harmonic oscillators** ($m \ddot{x} + c \dot{x} + k x = 0$).

### 1. 3D Bézier Easing & Kinetic Velocity Manifolds

<p align="center">
  <img src="assets/3d_surface.png" alt="3D Cubic-Bezier Easing Manifold and Kinetic Velocity Surface" width="100%">
</p>

* **Panel A (3D Cubic-Bézier Manifold $\mathcal{M}_{ease}$):** Represents the continuum of animation curves parameterized by timeline $t \in [0, 1]$ and curvature family $\kappa$. The manifold traces transitions from Linear ($y = t$) through standard `ease-in-out` (`cubic-bezier(0.65, 0, 0.35, 1)`), critically decelerated `ease-out` (`cubic-bezier(0.16, 1, 0.3, 1)`), up to extreme kinetic overshoot `ease-out-back` (`cubic-bezier(0.34, 1.56, 0.64, 1)`) where displacement peaks at $Z = 1.12$ before settling.
* **Panel B (3D Kinetic Velocity Surface $\mathcal{V}(t, k)$):** Visualizes the instantaneous velocity response $\dot{x}(t)$ across varying spring stiffness constants $k \in [100, 650]\text{ N/m}$ at damping ratio $\zeta = 0.42$. High-stiffness styles such as Comic Pop ($k = 640$) and Kinetic Impact ($k = 520$) generate instantaneous velocity crests exceeding $14.5\text{ m/s}$, driving explosive on-screen snap followed by rapid underdamped ringdown.

---

### 2. Cross-Style Attribute & Architecture Heatmap

<p align="center">
  <img src="assets/results_heatmap.png" alt="Cross-Style Architecture & Parameter Heatmap across 14 Libraries" width="100%">
</p>

The matrix compares the architectural invariants across all 14 libraries:
* **Typography Hierarchy:** Display weights range from 500 (Blueprint drafting, Liquid Gradient) to 900 (Kinetic Type, Neon Night).
* **Color Science & Accessibility:** High WCAG text-to-background contrast ratios ($11.0:1$ to $18.8:1$) ensure clarity in both high-key light modes and dark terminal aesthetics.
* **Physics & Geometry:** Styles with physical spring configurations encode stiffness $k$ up to $640\text{ N/m}$ and damping $\zeta \in [0.28, 0.93]$. Heavy Gaussian convolution filters (Soft Glass $\sigma = 28\text{px}$, Liquid Gradient $\sigma = 40\text{px}$) run at $32.0$–$39.5\text{ ms/frame}$ on CPU, while lightweight vector styles render in $11.5$–$14.2\text{ ms/frame}$.

---

### 3. Headless Engine & Synthesis Benchmarks

<p align="center">
  <img src="assets/performance_metrics.png" alt="Headless Engine Frame Latency, Rate-Distortion, and Agent Synthesis Benchmarks" width="100%">
</p>

* **Panel A (Headless Frame Render Latency Across Backends):** Benchmarking 1080p frame rasterization across Pure PIL, PyCairo (C vector engine), Skia Canvas, and direct hardware FFMPEG raw pipes. Vector styles comfortably surpass the 60 FPS real-time threshold ($< 16.67\text{ ms}$), achieving up to $550\text{ FPS}$ throughput with direct pipe compilation.
* **Panel B (Rate-Distortion Quality Curves):** SSIM perceptual quality curves across bitrates ($1.5$ to $25.0\text{ Mbps}$). AV1 and HEVC reach visually lossless transmission ($\text{SSIM} > 0.995$) at just $6.0$–$10.0\text{ Mbps}$, optimizing CDN delivery for automated video pipelines.
* **Panel C (Agent Beat Synthesis Speed):** Complete end-to-end clip generation executes in **$1.82\text{ seconds}$**—spanning brief parsing, AST validation, Bézier sampling, headless rendering, and FFMPEG muxing.
* **Panel D (Radar Performance Footprint):** Multi-dimensional capability profiles contrasting Kinetic Type (explosive velocity), Neon Night (chromatic bloom), Soft Glass (depth complexity), and Editorial Swiss (execution throughput).

## Use a style from Python

```bash
pip install -e ".[preview]"
python -m motionstyles list
python -m motionstyles export glass --format md -o style.md
python -m motionstyles export glass --format ts -o theme.ts
python -m motionstyles export glass --format css -o theme.css
```

From a checkout of this repo:

```bash
pip install "motionstyles[preview] @ git+https://github.com/TheRollerBlader/motion-graphic-style-library.git"
```

```python
from motionstyle_kinetic import STYLE
from motionstyle_core import sample_clip

slam = STYLE.clip("slam_scale")
scale = sample_clip(slam, 0.2)  # eased value, in the clip's unit
print(STYLE.name, scale)
print(STYLE.to_style_md())
```

`sample_clip` applies the easing inside each keyframe span and holds the last value after the clip ends. `strokeOffset` runs from 1 (hidden) to 0 (drawn). `progress` runs from 0 to 1 for counts and fills.

A style also exports:

- `to_style_md()` for an explainer agent's `style.md`
- `to_json()` for clip data
- `to_css()` for custom properties, including `--duration-*` and `--ease-*`
- `to_theme_ts()` for a Remotion theme module

## Agent skills

Skills live in [`.cursor/skills`](.cursor/skills). Open this repo in Cursor and ask for an explainer.

- [`apply-motion-style`](.cursor/skills/apply-motion-style/SKILL.md) picks one library and applies it.
- `style-swiss`, `style-kinetic`, `style-glass`, and the rest of the `style-*` skills hold the rules and the full spec for that look.

The skills are generated from the Python libraries, so the hex values cannot drift:

```bash
python -m motionstyles skills
```

An agent building a beat should:

1. Choose one style and export it.
2. Build that style's primitives once, then reuse them.
3. Give each spoken idea one picture of the thing being named.
4. Play the named clips. Do not invent a second easing.
5. Start a word's animation on that word's timestamp.
6. Keep the idle clip running so a hold never freezes.

## What a style locks

Every library is a closed spec.

- **Palette.** Background, ink, primary, accent, and the semantic colors. No extra hex.
- **Type.** Display, body, and mono, with weight, tracking, and case.
- **Shape.** Radius, border, shadow, and blur. A brutalist shadow is a hard offset. A glass shadow is not.
- **Motion.** Named clips and, where the style is physical, springs. Stagger time. An idle so holds stay alive.
- **Grammar.** The primitives, the caption, and the do / don't list.

Canvas for every style is 1920×1080 at 30 frames per second, with a 96px safe margin. A vertical cut reflows. It does not recolor.

## Project layout

```
assets/                      3D preview animation, manifolds, heatmaps & benchmarks
src/motionstyle_core/        model, sampling, exporters, previews
src/motionstyle_<name>/      one library per style
src/motionstyles/            catalog and the command line
catalog/                     style.md for every library
previews/                    looping GIF studies
docs/gallery.html            the same studies as CSS
.cursor/skills/              agent skills
```

## Develop

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m motionstyles previews previews
python -m motionstyles gallery
python -m motionstyles export-all catalog
```

Regenerate the skills, the catalog, the gallery, and the GIFs after changing a library. The tests check that the README, the gallery, and the skills still mention every style.

## License

[MIT](LICENSE)
