"""Render a style as markdown, JSON, CSS variables, or a Remotion theme module."""

from __future__ import annotations

import json

from motionstyle_core.model import PROPERTIES, Style
from motionstyle_core.motion import css_ease


def render_style_md(style: Style) -> str:
    """Markdown spec in the shape explainer agents already expect from style.md."""
    palette_lines = ["```"]
    width = max(len(label) for label, _ in style.palette.pairs())
    for label, value in style.palette.pairs():
        palette_lines.append(f"{label.ljust(width)}  {value}")
    palette_lines.append("```")

    def font_block(title: str, role) -> str:
        case = "uppercase" if role.case == "upper" else "as written"
        return (
            f"- {title}: {role.family}. Weight {role.weight}. "
            f"Tracking {role.tracking_em:.3f}em. Case: {case}. "
            f"Line height {role.line_height}."
        )

    springs = "No springs. Use the clip easings only."
    if style.motion.springs:
        springs = "\n".join(
            f"- `{item.name}`: stiffness {item.stiffness:g}, damping {item.damping:g}, mass {item.mass:g}."
            for item in style.motion.springs
        )

    clip_blocks = []
    for item in style.motion.clips:
        unit = f" ({item.unit})" if item.unit else ""
        lines = [
            f"### `{item.name}`",
            "",
            f"- Duration: {item.duration_s:g}s",
            f"- Ease: `{item.ease}` (CSS `{css_ease(item.ease)}`)",
            f"- Property: `{item.property}`{unit}",
            "- Keyframes:",
        ]
        for frame in item.keyframes:
            lines.append(f"  - {frame.t:.2f} → {frame.value:g}")
        if item.notes:
            lines.append(f"- {item.notes}")
        clip_blocks.append("\n".join(lines))
    clips = "\n\n".join(clip_blocks)

    notes = f"- {style.shape.notes}\n" if style.shape.notes else ""
    chrome = "\n".join(f"- {line}" for line in style.chrome)
    primitives = "\n".join(f"- {line}" for line in style.primitives)
    dos = "\n".join(f"- {line}" for line in style.dos)
    donts = "\n".join(f"- {line}" for line in style.donts)
    best = ", ".join(style.best_for)

    return f"""# Style Guide — {style.name}

Library: `{style.library}`
Style id: `{style.id}`

{style.tagline}

Best for: {best}.

Follow this file literally when building an explainer. Copy colors and type verbatim. Reproduce the shape and the named motion clips. Do not add a second palette, a second easing family, or decoration this file does not describe.

Canvas: {style.canvas.width}×{style.canvas.height} at {style.canvas.fps}fps. Keep content inside a {style.canvas.safe_px}px safe margin. For a 9:16 cut, keep these tokens and reflow to one column. Do not recolor.

## Palette

{chr(10).join(palette_lines)}

## Typography

{font_block("Display", style.display)}
{font_block("Body", style.body)}
{font_block("Mono", style.mono)}

## Shape and shadow

- Corner radius: {style.shape.radius_px:g}px.
- Border: {style.shape.border_px:g}px solid {style.shape.border_color}.
- Shadow: `{style.shape.shadow}`.
- Backdrop blur: {style.shape.blur_px:g}px.
{notes}## Motion

{style.motion.character}

Stagger between repeated elements: {style.motion.stagger_s:g}s.

Idle: {style.motion.idle}

Nothing on screen stays perfectly still for more than about one second. Sub-animations that illustrate a spoken word start on that word's timestamp, not on a fixed offset from the scene start.

### Springs

{springs}

### Clips

Sample a clip with `sample_clip(style.clip("{style.motion.clips[0].name}"), seconds)`. Easing runs inside each keyframe span. Hold the last value when the clip ends.

{clips}

Property units: {", ".join(f"`{name}`{' ' + unit if unit else ''}" for name, unit in PROPERTIES.items())}.

`strokeOffset` runs from 1 (hidden) to 0 (fully drawn). `progress` runs from 0 to 1 for counts and fills.

## Chrome

{chrome}

## Scene primitives

Build these once and reuse them for every beat. A new beat composes primitives. It does not invent a new card, shadow, or type treatment.

{primitives}

## Captions

{style.caption}

## Do

{dos}

## Don't

{donts}
"""


def render_json(style: Style) -> str:
    return json.dumps(style.to_dict(), indent=2) + "\n"


def render_css(style: Style) -> str:
    lines = [
        f"/* {style.library} — {style.name} */",
        ":root {",
    ]
    for label, value in style.palette.pairs():
        css_name = "--" + _kebab(label)
        lines.append(f"  {css_name}: {value};")
    lines.append(f"  --radius: {style.shape.radius_px:g}px;")
    lines.append(f"  --border-width: {style.shape.border_px:g}px;")
    lines.append(f"  --border-color: {style.shape.border_color};")
    lines.append(f"  --shadow: {style.shape.shadow};")
    lines.append(f"  --blur: {style.shape.blur_px:g}px;")
    lines.append(f"  --font-display: {style.display.family};")
    lines.append(f"  --font-body: {style.body.family};")
    lines.append(f"  --font-mono: {style.mono.family};")
    lines.append(f"  --stagger: {style.motion.stagger_s:g}s;")
    for item in style.motion.clips:
        lines.append(f"  --duration-{_kebab(item.name)}: {item.duration_s:g}s;")
        lines.append(f"  --ease-{_kebab(item.name)}: {css_ease(item.ease)};")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def render_theme_ts(style: Style) -> str:
    body = json.dumps(style.to_dict(), indent=2)
    return (
        f"// {style.library} — {style.name}\n"
        "// Drop-in theme for a Remotion (or other TS) explainer.\n"
        "// Durations are seconds. Map springs to spring({ stiffness, damping, mass }).\n"
        "// Map clips with interpolate() over keyframes, using cssEase.\n"
        f"export const theme = {body} as const;\n"
        f"export const styleId = {json.dumps(style.id)} as const;\n"
    )


def _kebab(value: str) -> str:
    out = []
    for char in value:
        if char.isupper():
            out.append("-")
            out.append(char.lower())
        else:
            out.append(char.replace("_", "-"))
    return "".join(out).lstrip("-")
