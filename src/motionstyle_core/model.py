"""Data model for a motion-graphic style.

A style is a closed spec: palette, type, shape, motion clips, and the rules
an agent needs to stage an explainer without inventing a second look.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_HEX = re.compile(r"^#[0-9A-F]{6}$")
_ID = re.compile(r"^[a-z][a-z0-9]*$")

PROPERTIES: dict[str, str] = {
    "opacity": "",
    "x": "px",
    "y": "px",
    "scale": "",
    "scaleX": "",
    "scaleY": "",
    "rotate": "deg",
    "letterSpacing": "em",
    "strokeOffset": "",
    "shadowOffset": "px",
    "blur": "px",
    "progress": "",
}


def _hex(value: str, label: str) -> str:
    text = value.strip().upper()
    if not _HEX.match(text):
        raise ValueError(f"{label} must be #RRGGBB, got {value!r}")
    return text


@dataclass(frozen=True)
class Keyframe:
    t: float
    value: float


@dataclass(frozen=True)
class Clip:
    """One reusable motion, sampled by agents and by the preview studies."""

    name: str
    duration_s: float
    ease: str
    property: str
    keyframes: tuple[Keyframe, ...]
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.name or not re.fullmatch(r"[a-z][a-z0-9_]*", self.name):
            raise ValueError(f"Clip name must be snake_case, got {self.name!r}")
        if self.duration_s <= 0:
            raise ValueError(f"{self.name} duration must be positive")
        if self.property not in PROPERTIES:
            raise ValueError(f"{self.name} uses unknown property {self.property!r}")
        if len(self.keyframes) < 2:
            raise ValueError(f"{self.name} needs at least two keyframes")
        times = [frame.t for frame in self.keyframes]
        if times != sorted(times):
            raise ValueError(f"{self.name} keyframes must be sorted by t")
        if times[0] != 0 or times[-1] != 1:
            raise ValueError(f"{self.name} keyframes must start at 0 and end at 1")
        # Imported lazily so model can finish loading before motion imports Clip.
        from motionstyle_core.motion import apply_ease

        apply_ease(self.ease, 0.5)

    @property
    def unit(self) -> str:
        return PROPERTIES[self.property]


@dataclass(frozen=True)
class Spring:
    name: str
    stiffness: float
    damping: float
    mass: float = 1.0

    def __post_init__(self) -> None:
        if self.stiffness <= 0 or self.damping <= 0 or self.mass <= 0:
            raise ValueError(f"Spring {self.name} needs positive stiffness, damping, and mass")


@dataclass(frozen=True)
class FontRole:
    family: str
    weight: int
    tracking_em: float = 0.0
    case: str = "none"
    line_height: float = 1.1

    def __post_init__(self) -> None:
        if self.case not in {"none", "upper"}:
            raise ValueError(f"Font case must be none or upper, got {self.case!r}")
        if not 100 <= self.weight <= 900:
            raise ValueError(f"Font weight out of range: {self.weight}")


@dataclass(frozen=True)
class Palette:
    background: str
    background_raised: str
    surface: str
    ink: str
    text: str
    text_dim: str
    primary: str
    primary_light: str
    primary_dark: str
    secondary: str
    accent: str
    danger: str
    ok: str
    info: str
    spots: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "background",
            "background_raised",
            "surface",
            "ink",
            "text",
            "text_dim",
            "primary",
            "primary_light",
            "primary_dark",
            "secondary",
            "accent",
            "danger",
            "ok",
            "info",
        ):
            object.__setattr__(self, name, _hex(getattr(self, name), name))
        cleaned = []
        seen = set()
        for name, value in self.spots:
            if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
                raise ValueError(f"Spot name must be snake_case, got {name!r}")
            if name in seen:
                raise ValueError(f"Duplicate spot {name}")
            seen.add(name)
            cleaned.append((name, _hex(value, name)))
        object.__setattr__(self, "spots", tuple(cleaned))

    def pairs(self) -> tuple[tuple[str, str], ...]:
        base = (
            ("bg", self.background),
            ("bgRaised", self.background_raised),
            ("surface", self.surface),
            ("ink", self.ink),
            ("text", self.text),
            ("textDim", self.text_dim),
            ("primary", self.primary),
            ("primaryLight", self.primary_light),
            ("primaryDark", self.primary_dark),
            ("secondary", self.secondary),
            ("accent", self.accent),
            ("danger", self.danger),
            ("ok", self.ok),
            ("info", self.info),
        )
        return base + self.spots

    def spot(self, name: str) -> str:
        for key, value in self.spots:
            if key == name:
                return value
        raise KeyError(name)


@dataclass(frozen=True)
class Shape:
    radius_px: float
    border_px: float
    border_color: str
    shadow: str
    blur_px: float = 0.0
    notes: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "border_color", _hex(self.border_color, "border_color"))
        if self.radius_px < 0 or self.border_px < 0 or self.blur_px < 0:
            raise ValueError("Shape sizes cannot be negative")


@dataclass(frozen=True)
class Motion:
    character: str
    springs: tuple[Spring, ...]
    clips: tuple[Clip, ...]
    stagger_s: float
    idle: str

    def __post_init__(self) -> None:
        names = [clip.name for clip in self.clips]
        if len(names) != len(set(names)):
            raise ValueError("Clip names must be unique inside a style")
        if len(self.clips) < 3:
            raise ValueError("A style needs at least three clips: an entrance, a build, and an idle")
        if self.stagger_s < 0:
            raise ValueError("stagger_s cannot be negative")


@dataclass(frozen=True)
class Canvas:
    width: int = 1920
    height: int = 1080
    fps: int = 30
    safe_px: int = 96


@dataclass(frozen=True)
class Style:
    id: str
    name: str
    tagline: str
    best_for: tuple[str, ...]
    aliases: tuple[str, ...]
    palette: Palette
    display: FontRole
    body: FontRole
    mono: FontRole
    shape: Shape
    motion: Motion
    chrome: tuple[str, ...]
    primitives: tuple[str, ...]
    caption: str
    dos: tuple[str, ...]
    donts: tuple[str, ...]
    agent_rules: tuple[str, ...]
    canvas: Canvas = Canvas()

    def __post_init__(self) -> None:
        if not _ID.match(self.id):
            raise ValueError(f"Style id must be lowercase letters, got {self.id!r}")
        for label, items, minimum in (
            ("best_for", self.best_for, 2),
            ("aliases", self.aliases, 2),
            ("chrome", self.chrome, 3),
            ("primitives", self.primitives, 3),
            ("dos", self.dos, 2),
            ("donts", self.donts, 2),
            ("agent_rules", self.agent_rules, 2),
        ):
            if len(items) < minimum:
                raise ValueError(f"{self.id} needs at least {minimum} {label}")

    @property
    def library(self) -> str:
        return f"motionstyle_{self.id}"

    def clip(self, name: str) -> Clip:
        for item in self.motion.clips:
            if item.name == name:
                return item
        raise KeyError(f"{self.id} has no clip {name!r}")

    def to_dict(self) -> dict:
        def font(role: FontRole) -> dict:
            return {
                "family": role.family,
                "weight": role.weight,
                "trackingEm": role.tracking_em,
                "case": role.case,
                "lineHeight": role.line_height,
            }

        from motionstyle_core.motion import css_ease

        return {
            "id": self.id,
            "name": self.name,
            "library": self.library,
            "tagline": self.tagline,
            "bestFor": list(self.best_for),
            "canvas": {
                "width": self.canvas.width,
                "height": self.canvas.height,
                "fps": self.canvas.fps,
                "safePx": self.canvas.safe_px,
            },
            "palette": {key: value for key, value in self.palette.pairs()},
            "typography": {"display": font(self.display), "body": font(self.body), "mono": font(self.mono)},
            "shape": {
                "radiusPx": self.shape.radius_px,
                "borderPx": self.shape.border_px,
                "borderColor": self.shape.border_color,
                "shadow": self.shape.shadow,
                "blurPx": self.shape.blur_px,
                "notes": self.shape.notes,
            },
            "motion": {
                "character": self.motion.character,
                "staggerS": self.motion.stagger_s,
                "idle": self.motion.idle,
                "springs": [
                    {"name": item.name, "stiffness": item.stiffness, "damping": item.damping, "mass": item.mass}
                    for item in self.motion.springs
                ],
                "clips": [
                    {
                        "name": item.name,
                        "durationS": item.duration_s,
                        "ease": item.ease,
                        "cssEase": css_ease(item.ease),
                        "property": item.property,
                        "unit": item.unit,
                        "keyframes": [[frame.t, frame.value] for frame in item.keyframes],
                        "notes": item.notes,
                    }
                    for item in self.motion.clips
                ],
            },
            "chrome": list(self.chrome),
            "primitives": list(self.primitives),
            "caption": self.caption,
            "do": list(self.dos),
            "dont": list(self.donts),
        }

    def to_style_md(self) -> str:
        from motionstyle_core.export import render_style_md

        return render_style_md(self)

    def to_json(self) -> str:
        from motionstyle_core.export import render_json

        return render_json(self)

    def to_css(self) -> str:
        from motionstyle_core.export import render_css

        return render_css(self)

    def to_theme_ts(self) -> str:
        from motionstyle_core.export import render_theme_ts

        return render_theme_ts(self)


def font(
    family: str,
    weight: int,
    tracking_em: float = 0.0,
    case: str = "none",
    line_height: float = 1.1,
) -> FontRole:
    return FontRole(family, weight, tracking_em, case, line_height)


def spring(name: str, stiffness: float, damping: float, mass: float = 1.0) -> Spring:
    return Spring(name, stiffness, damping, mass)


def clip(
    name: str,
    duration_s: float,
    ease: str,
    property: str,
    keyframes: tuple[tuple[float, float], ...],
    notes: str = "",
) -> Clip:
    frames = tuple(Keyframe(float(t), float(value)) for t, value in keyframes)
    return Clip(name, duration_s, ease, property, frames, notes)


def make_style(
    *,
    id: str,
    name: str,
    tagline: str,
    best_for: tuple[str, ...],
    aliases: tuple[str, ...],
    palette: dict[str, str],
    spots: tuple[tuple[str, str], ...] = (),
    display: FontRole,
    body: FontRole,
    mono: FontRole,
    shape: dict,
    motion_character: str,
    springs: tuple[Spring, ...] = (),
    clips: tuple[Clip, ...],
    stagger_s: float,
    idle: str,
    chrome: tuple[str, ...],
    primitives: tuple[str, ...],
    caption: str,
    dos: tuple[str, ...],
    donts: tuple[str, ...],
    agent_rules: tuple[str, ...],
) -> Style:
    shape_data = dict(shape)
    notes = shape_data.pop("notes", "")
    return Style(
        id=id,
        name=name,
        tagline=tagline,
        best_for=best_for,
        aliases=aliases,
        palette=Palette(spots=spots, **palette),
        display=display,
        body=body,
        mono=mono,
        shape=Shape(notes=notes, **shape_data),
        motion=Motion(motion_character, springs, clips, stagger_s, idle),
        chrome=chrome,
        primitives=primitives,
        caption=caption,
        dos=dos,
        donts=donts,
        agent_rules=agent_rules,
    )
