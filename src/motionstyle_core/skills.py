"""Render Cursor agent skills from the style libraries."""

from __future__ import annotations

from pathlib import Path

from motionstyle_core.export import render_style_md
from motionstyle_core.model import Style


def skill_name(style: Style) -> str:
    return f"style-{style.id}"


def skill_description(style: Style) -> str:
    triggers = ", ".join(style.aliases)
    return (
        f"Apply the {style.name} motion-graphic style from the {style.library} Python library "
        f"when building an explainer, title card, or narration-synced video. "
        f"Use when the user asks for {triggers}, names {style.name}, or the style id {style.id}. "
        f"Supplies the palette, type, shape, motion clips, captions, and scene grammar."
    )


def render_skill(style: Style) -> str:
    rules = "\n".join(f"- {rule}" for rule in style.agent_rules)
    description = skill_description(style).replace('"', "'")
    return f"""---
name: {skill_name(style)}
description: "{description}"
---

# {style.name}

Apply this when the picture should be {style.name}. {style.tagline}

## Rules agents miss

{rules}

The spec below is generated from `{style.library}`. Copy its colors, type, and clip names. Do not invent a second palette or a second easing.

{render_style_md(style)}
"""


def render_catalog_md(styles: tuple[Style, ...]) -> str:
    rows = ["| Style | Library | Use it for | How it moves |", "| --- | --- | --- | --- |"]
    for style in styles:
        best = ", ".join(style.best_for)
        rows.append(f"| `{style.id}` {style.name} | `{style.library}` | {best} | {style.motion.character} |")
    body = "\n".join(rows)
    return f"""# Style catalog

Pick one style for the whole video. Do not mix two.

Match the user's ask against "Use it for". If two styles fit equally well, ask which one before drawing. If they named a style, use that one even if another also fits.

{body}

After choosing, read that style's skill (`style-<id>/SKILL.md`) and follow it literally.
"""


def write_skills(styles: tuple[Style, ...], root: str | Path) -> list[Path]:
    base = Path(root)
    written = []
    catalog_path = base / "apply-motion-style" / "catalog.md"
    catalog_path.parent.mkdir(parents=True, exist_ok=True)
    catalog_path.write_text(render_catalog_md(styles), encoding="utf-8")
    written.append(catalog_path)
    for style in styles:
        path = base / skill_name(style) / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_skill(style), encoding="utf-8")
        written.append(path)
    return written
