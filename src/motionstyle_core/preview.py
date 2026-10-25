"""Looping GIF studies. Each study samples that style's real clips."""

from __future__ import annotations

import os
from functools import lru_cache

from motionstyle_core.model import Style
from motionstyle_core.motion import pose

W, H = 720, 405
SCALE = 2

FONTS: dict[str, tuple[str, ...]] = {
    "sans": (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ),
    "bold": (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "black": (
        "/System/Library/Fonts/Supplemental/Arial Black.ttf",
        "/System/Library/Fonts/Supplemental/Impact.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "narrow": (
        "/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "serif": (
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    ),
    "mono": (
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    ),
    "chalk": (
        "/System/Library/Fonts/Supplemental/Chalkduster.ttf",
        "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "comic": (
        "/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "rounded": (
        "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
    "din": (
        "/System/Library/Fonts/Supplemental/DIN Alternate Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ),
}


def _require_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFilter, ImageFont
    except ImportError as exc:
        raise RuntimeError("Rendering previews needs Pillow. Install it with: pip install pillow") from exc
    return Image, ImageDraw, ImageFilter, ImageFont


@lru_cache(maxsize=64)
def _font(kind: str, size: int):
    _, _, _, ImageFont = _require_pillow()
    px = max(8, int(size * SCALE))
    for path in FONTS.get(kind, FONTS["sans"]):
        if os.path.exists(path):
            return ImageFont.truetype(path, px)
    loader = getattr(ImageFont, "load_default", None)
    try:
        return loader(px)
    except TypeError:
        return loader()


def _mix(style: Style, name: str, amount: float) -> float:
    return pose(style.clip(name), amount)


def _lag(amount: float, start: float) -> float:
    if amount <= start:
        return 0.0
    return min(1.0, (amount - start) / (1 - start))


class Stage:
    """Logical 720×405 drawing surface, rasterized at 2× and downscaled."""

    def __init__(self) -> None:
        Image, ImageDraw, ImageFilter, _ = _require_pillow()
        self.Image = Image
        self.Draw = ImageDraw.Draw
        self.Filter = ImageFilter
        self.im = Image.new("RGBA", (W * SCALE, H * SCALE), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)

    def rgba(self, hex_color: str, alpha: int = 255) -> tuple[int, int, int, int]:
        value = hex_color.lstrip("#")
        channels = tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))
        return channels[0], channels[1], channels[2], max(0, min(255, int(alpha)))

    def _box(self, x: float, y: float, w: float, h: float) -> list[float]:
        return [x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE]

    def rect(self, x, y, w, h, fill) -> None:
        if w <= 0 or h <= 0:
            return
        self.d.rectangle(self._box(x, y, w, h), fill=fill)

    def rrect(self, x, y, w, h, radius, fill=None, outline=None, width=0) -> None:
        if w <= 0 or h <= 0:
            return
        kwargs = {}
        if fill is not None:
            kwargs["fill"] = fill
        if outline is not None and width:
            kwargs["outline"] = outline
            kwargs["width"] = max(1, int(width * SCALE))
        self.d.rounded_rectangle(self._box(x, y, w, h), radius=max(0, radius * SCALE), **kwargs)

    def ellipse(self, x, y, w, h, fill) -> None:
        if w <= 0 or h <= 0:
            return
        self.d.ellipse(self._box(x, y, w, h), fill=fill)

    def line(self, x1, y1, x2, y2, fill, width=2) -> None:
        self.d.line(
            [(x1 * SCALE, y1 * SCALE), (x2 * SCALE, y2 * SCALE)],
            fill=fill,
            width=max(1, int(width * SCALE)),
        )

    def poly(self, points, fill) -> None:
        self.d.polygon([(x * SCALE, y * SCALE) for x, y in points], fill=fill)

    def arc(self, x, y, w, h, start, end, fill, width=6) -> None:
        self.d.arc(
            self._box(x, y, w, h),
            start=start,
            end=end,
            fill=fill,
            width=max(1, int(width * SCALE)),
        )

    def text(self, x, y, content, kind, size, fill, tracking=0, anchor="left", valign="top") -> None:
        if not content:
            return
        font = _font(kind, size)
        track = tracking * SCALE
        widths = []
        for char in content:
            glyph = font.getlength(char) if hasattr(font, "getlength") else font.getbbox(char)[2]
            widths.append(glyph + track)
        total = sum(widths) - track
        dx = x * SCALE
        dy = y * SCALE
        if anchor == "center":
            dx -= total / 2
        elif anchor == "right":
            dx -= total
        bbox = font.getbbox(content)
        height = max(1, bbox[3] - bbox[1])
        if valign == "middle":
            dy -= height / 2 + bbox[1]
        elif valign == "bottom":
            dy -= bbox[3]
        for char, step in zip(content, widths):
            self.d.text((dx, dy - bbox[1]), char, font=font, fill=fill)
            dx += step

    def polyline(self, points, amount, fill, width=3) -> None:
        if len(points) < 2 or amount <= 0:
            return
        spans = []
        total = 0.0
        for start, end in zip(points, points[1:]):
            dist = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5
            spans.append((start, end, dist))
            total += dist
        remain = total * min(1.0, amount)
        for start, end, dist in spans:
            if remain <= 0:
                break
            local = 1.0 if dist == 0 else min(1.0, remain / dist)
            self.line(
                start[0],
                start[1],
                start[0] + (end[0] - start[0]) * local,
                start[1] + (end[1] - start[1]) * local,
                fill,
                width,
            )
            remain -= dist

    def frost(self, x, y, w, h, radius, tint="#FFFFFF", tint_a=48, border="#FFFFFF", border_a=90) -> None:
        box = (int(x * SCALE), int(y * SCALE), int((x + w) * SCALE), int((y + h) * SCALE))
        panel = self.im.crop(box).filter(self.Filter.GaussianBlur(radius=16))
        veil = self.Image.new("RGBA", panel.size, self.rgba(tint, tint_a))
        panel = self.Image.alpha_composite(panel, veil)
        mask = self.Image.new("L", panel.size, 0)
        self.Draw(mask).rounded_rectangle(
            (0, 0, panel.size[0] - 1, panel.size[1] - 1),
            radius=radius * SCALE,
            fill=255,
        )
        self.im.paste(panel, box[:2], mask)
        self.d = self.Draw(self.im)
        self.rrect(x, y, w, h, radius, outline=self.rgba(border, border_a), width=1.5)

    def blur(self, radius: float) -> None:
        self.im = self.im.filter(self.Filter.GaussianBlur(radius=radius))
        self.d = self.Draw(self.im)

    def finish(self, background: str):
        sheet = self.im.resize((W, H), self.Image.Resampling.LANCZOS)
        base = self.Image.new("RGBA", (W, H), self.rgba(background))
        base.alpha_composite(sheet)
        return base.convert("RGB")


DRAWERS: dict[str, object] = {}


def _drawer(style_id: str):
    def wrap(fn):
        DRAWERS[style_id] = fn
        return fn

    return wrap


def _ensure_drawers() -> None:
    if not DRAWERS:
        from motionstyle_core import preview_scenes  # noqa: F401
        from motionstyle_core import preview_scenes_b  # noqa: F401


def _tri(frame: int, count: int) -> float:
    return 1 - abs(2 * (frame / count) - 1)


def render_frame(style: Style, frame: int, count: int = 36):
    _ensure_drawers()
    drawer = DRAWERS.get(style.id)
    if drawer is None:
        raise KeyError(f"No preview animation for {style.id}")
    stage = Stage()
    drawer(stage, style, _tri(frame, count), frame / count)
    return stage.finish(style.palette.background)


def render_gif(style: Style, path: str, frames: int = 36) -> None:
    Image, _, _, _ = _require_pillow()
    rendered = [render_frame(style, index, frames) for index in range(frames)]
    colors = 128 if style.id in {"gradient", "glass", "neon", "documentary"} else 80
    palette = rendered[frames // 2].quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    paletted = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in rendered]
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    paletted[0].save(
        path,
        save_all=True,
        append_images=paletted[1:],
        duration=80,
        loop=0,
        disposal=2,
        optimize=False,
    )


def render_all(directory: str, frames: int = 36) -> list[str]:
    from motionstyles import catalog

    paths = []
    for style in catalog():
        path = os.path.join(directory, f"{style.id}.gif")
        render_gif(style, path, frames=frames)
        paths.append(path)
    return paths
