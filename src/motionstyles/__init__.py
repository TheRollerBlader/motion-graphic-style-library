"""Catalog of every motion-graphic style library."""

from motionstyle_blueprint import STYLE as BLUEPRINT
from motionstyle_brutalist import STYLE as BRUTALIST
from motionstyle_chalk import STYLE as CHALK
from motionstyle_comic import STYLE as COMIC
from motionstyle_documentary import STYLE as DOCUMENTARY
from motionstyle_glass import STYLE as GLASS
from motionstyle_gradient import STYLE as GRADIENT
from motionstyle_isometric import STYLE as ISOMETRIC
from motionstyle_kinetic import STYLE as KINETIC
from motionstyle_neon import STYLE as NEON
from motionstyle_papercut import STYLE as PAPERCUT
from motionstyle_playful import STYLE as PLAYFUL
from motionstyle_signal import STYLE as SIGNAL
from motionstyle_swiss import STYLE as SWISS

STYLES = (
    SWISS,
    KINETIC,
    GLASS,
    BRUTALIST,
    CHALK,
    ISOMETRIC,
    SIGNAL,
    PAPERCUT,
    NEON,
    DOCUMENTARY,
    PLAYFUL,
    BLUEPRINT,
    GRADIENT,
    COMIC,
)

CATALOG = {style.id: style for style in STYLES}


def catalog():
    return STYLES


def get_style(style_id: str):
    key = style_id.strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "neo_brutalist": "brutalist",
        "neo_brutalism": "brutalist",
        "chalkboard": "chalk",
        "glassmorphism": "glass",
        "data": "signal",
        "dataviz": "signal",
        "paper": "papercut",
        "paper_cut": "papercut",
        "mesh": "gradient",
        "liquid": "gradient",
        "pop": "comic",
        "schematic": "blueprint",
    }
    key = aliases.get(key, key)
    try:
        return CATALOG[key]
    except KeyError as exc:
        known = ", ".join(CATALOG)
        raise KeyError(f"Unknown style {style_id!r}. Known styles: {known}") from exc


__all__ = ["CATALOG", "STYLES", "catalog", "get_style"]
