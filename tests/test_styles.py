"""The style libraries stay closed, exportable, and animated."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from motionstyle_core.gallery import render_gallery
from motionstyle_core.motion import sample_clip
from motionstyle_core.preview import DRAWERS, _ensure_drawers, render_frame
from motionstyle_core.skills import render_skill, skill_description
from motionstyles import catalog, get_style

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_is_fourteen_distinct_libraries():
    styles = catalog()
    assert len(styles) == 14
    assert len({style.id for style in styles}) == 14
    for style in styles:
        assert style.library == f"motionstyle_{style.id}"
        module = __import__(style.library, fromlist=["STYLE"])
        assert module.STYLE is style or module.STYLE.id == style.id


def test_every_clip_samples_and_eases():
    for style in catalog():
        for clip in style.motion.clips:
            start = sample_clip(clip, 0)
            end = sample_clip(clip, clip.duration_s + 1)
            mid = sample_clip(clip, clip.duration_s * 0.5)
            assert start == clip.keyframes[0].value
            assert end == clip.keyframes[-1].value
            assert isinstance(mid, float)


def test_exports_contain_the_palette_and_clips():
    style = get_style("brutalist")
    markdown = style.to_style_md()
    assert style.palette.primary in markdown
    assert "pop_scale" in markdown
    assert "Do not use soft shadows" in markdown
    assert style.palette.primary in style.to_css()
    assert style.palette.primary in style.to_theme_ts()
    assert '"id": "brutalist"' in style.to_json()


def test_unknown_style_names_the_ones_that_exist():
    with pytest.raises(KeyError, match="swiss"):
        get_style("watercolor")


def test_aliases_resolve():
    assert get_style("glassmorphism").id == "glass"
    assert get_style("neo-brutalist").id == "brutalist"
    assert get_style("paper cut").id == "papercut"


def test_skills_embed_rules_and_colors_and_stay_short():
    for style in catalog():
        text = render_skill(style)
        assert len(text.splitlines()) < 500
        assert len(skill_description(style)) < 1024
        assert style.palette.primary in text
        assert style.agent_rules[0] in text
        assert f"name: style-{style.id}" in text


def test_gallery_animates_every_style():
    html = render_gallery(catalog())
    assert "@keyframes" in html
    assert "{primary}" not in html
    assert "{background}" not in html
    for style in catalog():
        assert f"s-{style.id}" in html
        assert style.palette.primary in html
        assert style.name in html


def test_readme_showcases_every_style():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for style in catalog():
        assert f"previews/{style.id}.gif" in readme
        assert style.library in readme
        assert style.name in readme


def test_committed_skills_match_the_libraries():
    for style in catalog():
        path = ROOT / ".cursor" / "skills" / f"style-{style.id}" / "SKILL.md"
        assert path.read_text(encoding="utf-8") == render_skill(style)


def test_router_skill_points_at_the_catalog():
    text = (ROOT / ".cursor" / "skills" / "apply-motion-style" / "SKILL.md").read_text(encoding="utf-8")
    assert "catalog.md" in text
    assert "one style" in text.lower() or "exactly one" in text


def test_preview_frame_renders_for_every_style():
    _ensure_drawers()
    assert set(DRAWERS) == {style.id for style in catalog()}
    for style in catalog():
        frame = render_frame(style, 18, 36)
        assert frame.size == (720, 405)


def test_style_modules_parse():
    for path in (ROOT / "src").glob("motionstyle_*/__init__.py"):
        ast.parse(path.read_text(encoding="utf-8"))
