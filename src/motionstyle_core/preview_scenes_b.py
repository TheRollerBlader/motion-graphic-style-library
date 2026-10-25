"""Remaining signature animations."""

from __future__ import annotations

import math

from motionstyle_core.model import Style
from motionstyle_core.preview import H, W, SCALE, Stage, _drawer, _lag, _mix


def _burst(stage: Stage, cx, cy, outer, inner, fill, outline) -> None:
    points = []
    spikes = 14
    for index in range(spikes * 2):
        angle = -math.pi / 2 + index * math.pi / spikes
        radius = outer if index % 2 == 0 else inner
        points.append((cx + math.cos(angle) * radius, cy + math.sin(angle) * radius * 0.8))
    stage.poly(points, fill)
    stage.polyline(points + [points[0]], 1, outline, 4)


@_drawer("papercut")
def _papercut(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    sheets = (
        (palette.secondary, -1, 0.0, 130, 110, 400, 190),
        (palette.spot("sheet_pink"), 1, 0.16, 168, 78, 370, 180),
        (palette.surface, -1, 0.34, 200, 48, 340, 190),
    )
    placed = (200, 48, 340)
    for color, direction, delay, x, y, w, h in sheets:
        amount = _lag(tri, delay)
        dx = _mix(style, "sheet_x", amount) * direction
        dy = _mix(style, "sheet_y", amount)
        stage.rrect(x + dx, y + dy + 16, w, h, 18, stage.rgba(palette.ink, 30))
        stage.rrect(x + dx, y + dy, w, h, 18, stage.rgba(color))
        placed = (x + dx, y + dy, w)
    float_y = math.sin(phase * math.tau) * 3
    stage.text(
        placed[0] + placed[2] / 2,
        placed[1] + 96 + float_y,
        "Story",
        "serif",
        64,
        stage.rgba(palette.ink),
        anchor="center",
        valign="middle",
    )


@_drawer("neon")
def _neon(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    stage.line(0, 250, W, 250, stage.rgba(palette.accent, 40), 1)
    for index in range(-6, 7):
        stage.line(W / 2, 250, W / 2 + index * 80, H, stage.rgba(palette.secondary, 50), 1)
    amount = min(1.0, phase / 0.2)
    opacity = _mix(style, "flicker", amount)
    glow = _mix(style, "glow", amount)
    if opacity < 0.04:
        return
    layer = stage.Image.new("RGBA", stage.im.size, (0, 0, 0, 0))
    stage.d = stage.Draw(layer)
    stage.text(
        W / 2,
        145,
        "NEON",
        "black",
        100,
        stage.rgba(palette.primary, int(255 * opacity)),
        tracking=6,
        anchor="center",
        valign="middle",
    )
    blurred = layer.filter(stage.Filter.GaussianBlur(radius=max(2, glow * SCALE * 0.45)))
    stage.im = stage.Image.alpha_composite(stage.im, blurred)
    stage.im = stage.Image.alpha_composite(stage.im, layer)
    stage.d = stage.Draw(stage.im)
    stage.arc(255, 205, 210, 64, 200, 340, stage.rgba(palette.accent, int(255 * opacity)), 3)


@_drawer("documentary")
def _documentary(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    scale = 1.0 + 0.06 * tri
    photo = stage.Image.new("RGBA", (int(680 * SCALE), int(280 * SCALE)), stage.rgba(palette.info))
    draw = stage.Draw(photo)
    draw.rectangle((0, 0, photo.size[0], int(140 * SCALE)), fill=stage.rgba(palette.primary))
    draw.ellipse((int(460 * SCALE), int(28 * SCALE), int(560 * SCALE), int(128 * SCALE)), fill=stage.rgba(palette.accent))
    draw.polygon(
        [
            (0, int(170 * SCALE)),
            (int(240 * SCALE), int(80 * SCALE)),
            (int(460 * SCALE), int(190 * SCALE)),
            (0, int(230 * SCALE)),
        ],
        fill=stage.rgba(palette.secondary),
    )
    draw.rectangle((0, int(190 * SCALE), photo.size[0], photo.size[1]), fill=stage.rgba(palette.background_raised))
    sw, sh = int(photo.size[0] * scale), int(photo.size[1] * scale)
    photo = photo.resize((sw, sh), stage.Image.Resampling.LANCZOS)
    stage.im.alpha_composite(photo, ((W * SCALE - sw) // 2, int(16 * SCALE)))
    stage.d = stage.Draw(stage.im)
    fade = _mix(style, "fade_in", tri)
    bar_y = 318 + _mix(style, "lower_third", tri)
    stage.rect(0, bar_y, 340, 48, stage.rgba(palette.primary, int(255 * fade)))
    stage.text(24, bar_y + 24, "Field notes", "serif", 26, stage.rgba(palette.background, int(255 * fade)), valign="middle")


@_drawer("playful")
def _playful(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    specs = (
        (160, 175, 116, palette.primary),
        (340, 155, 148, palette.secondary),
        (530, 185, 108, palette.accent),
    )
    for index, (x, y, size, color) in enumerate(specs):
        amount = _lag(tri, index * 0.14)
        scale = _mix(style, "pop_scale", amount)
        squash = _mix(style, "squash", amount)
        bob = math.sin(phase * math.tau) * 7 if index == 1 else 0
        width = size * scale * squash
        height = size * scale * (2 - squash)
        stage.ellipse(x - width / 2, y + height * 0.42 + bob, width, 16, stage.rgba("#F0C2B4"))
        stage.ellipse(x - width / 2, y - height / 2 + bob, width, height, stage.rgba(color))
    stage.text(W / 2, 318, "Hello", "rounded", 40, stage.rgba(palette.ink), anchor="center")


@_drawer("blueprint")
def _blueprint(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    for x in range(0, W, 24):
        stage.line(x, 0, x, H, stage.rgba(palette.primary, 32), 1)
    for y in range(0, H, 24):
        stage.line(0, y, W, y, stage.rgba(palette.primary, 32), 1)
    drawn = 1 - _mix(style, "stroke_draw", tri)
    stage.polyline([(110, 70), (600, 70), (600, 270), (110, 270), (110, 70)], drawn, stage.rgba(palette.primary), 2)
    ticks = int(255 * _mix(style, "tick_in", _lag(tri, 0.5)))
    stage.line(110, 292, 600, 292, stage.rgba(palette.secondary, ticks), 1)
    stage.line(110, 284, 110, 300, stage.rgba(palette.secondary, ticks), 2)
    stage.line(600, 284, 600, 300, stage.rgba(palette.secondary, ticks), 2)
    label = int(255 * _mix(style, "label_in", _lag(tri, 0.66)))
    stage.text(355, 322, "490", "mono", 16, stage.rgba(palette.secondary, label), anchor="center")
    stage.text(28, 22, "A-01", "din", 18, stage.rgba(palette.ink), tracking=2)


@_drawer("gradient")
def _gradient(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    blobs = (
        (palette.spot("violet"), 40, 10, 380, 300),
        (palette.spot("peach"), 280, 130, 360, 280),
        (palette.spot("blue"), 150, 180, 320, 240),
        (palette.spot("magenta"), 430, -30, 300, 250),
    )
    for index, (color, x, y, w, h) in enumerate(blobs):
        shift = math.sin(phase * math.tau + index) * 30
        lift = math.cos(phase * math.tau + index * 0.8) * 20
        stage.ellipse(x + shift, y + lift, w, h, stage.rgba(color, 220))
    stage.blur(26)
    alpha = int(255 * min(1, tri * 1.3))
    stage.text(W / 2, 188 + _mix(style, "fade_up", tri), "Flow", "bold", 76, stage.rgba(palette.ink, alpha), anchor="center", valign="middle")


@_drawer("comic")
def _comic(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.accent))
    stage.rrect(14, 14, W - 28, H - 28, 2, outline=stage.rgba(palette.ink), width=6)
    y = 36
    row = 0
    while y < 250:
        x = 48 + (8 if row % 2 else 0)
        while x < 420:
            stage.ellipse(x, y, 6, 6, stage.rgba(palette.primary, 80))
            x += 18
        y += 18
        row += 1
    scale = _mix(style, "pop_scale", tri)
    shake = _mix(style, "shake_x", _lag(tri, 0.5))
    _burst(stage, 230 + shake, 185, 138 * scale, 82 * scale, stage.rgba(palette.primary), stage.rgba(palette.ink))
    stage.text(230 + shake, 185, "POW", "comic", max(12, int(40 * scale)), stage.rgba(palette.ink), anchor="center", valign="middle")
    if tri <= 0.22:
        return
    bubble = _mix(style, "bubble_in", _lag(tri, 0.22))
    stage.rrect(450, 58, 210 * bubble, 96 * bubble, 18, stage.rgba(palette.surface), stage.rgba(palette.ink), 4)
    stage.poly([(470, 140), (438, 188), (520, 148)], stage.rgba(palette.surface))
    stage.line(470, 140, 438, 188, stage.rgba(palette.ink), 4)
    stage.line(438, 188, 520, 148, stage.rgba(palette.ink), 4)
    stage.text(450 + 105 * bubble, 100, "Again!", "comic", 26, stage.rgba(palette.ink), anchor="center", valign="middle")
