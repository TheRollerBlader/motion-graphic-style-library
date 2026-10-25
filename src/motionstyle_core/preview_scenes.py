"""Signature animations for the first seven styles. The rest register from preview_scenes_b."""

from __future__ import annotations

import math

from motionstyle_core.model import Style
from motionstyle_core.preview import H, W, SCALE, Stage, _drawer, _lag, _mix


def _shade(hex_color: str, factor: float) -> str:
    value = hex_color.lstrip("#")
    channels = [min(255, max(0, int(int(value[index : index + 2], 16) * factor))) for index in (0, 2, 4)]
    return "#" + "".join(f"{channel:02X}" for channel in channels)


def _cube(stage: Stage, cx: float, cy: float, color: str) -> None:
    w, h, d = 86, 44, 64
    top = [(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)]
    left = [(cx - w / 2, cy), (cx, cy + h / 2), (cx, cy + h / 2 + d), (cx - w / 2, cy + d)]
    right = [(cx + w / 2, cy), (cx, cy + h / 2), (cx, cy + h / 2 + d), (cx + w / 2, cy + d)]
    stage.poly(left, stage.rgba(_shade(color, 0.7)))
    stage.poly(right, stage.rgba(_shade(color, 0.52)))
    stage.poly(top, stage.rgba(_shade(color, 1.08)))


@_drawer("swiss")
def _swiss(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    stage.rect(0, 0, 220 * _mix(style, "wipe_x", tri), H, stage.rgba(palette.primary))
    stage.rect(48, 62, 120 * _mix(style, "wipe_x", tri), 2, stage.rgba(palette.background))
    tracking = _mix(style, "tracking_settle", tri) * 40
    stage.text(460, 175, "SWISS", "black", 84, stage.rgba(palette.ink), tracking=tracking, anchor="center", valign="middle")
    stage.text(48, 34, "01  /  08", "din", 16, stage.rgba(palette.background), tracking=1)
    rule_x = (64 + phase * 460) % 520
    stage.line(rule_x + 40, 310, rule_x + 110, 310, stage.rgba(palette.ink), 1)
    stage.text(460, 250, "ONE RED", "narrow", 16, stage.rgba(palette.text_dim), tracking=4, anchor="center")


@_drawer("kinetic")
def _kinetic(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    scale = _mix(style, "slam_scale", tri)
    layer = stage.Image.new("RGBA", stage.im.size, (0, 0, 0, 0))
    stage.d = stage.Draw(layer)
    y_shift = _mix(style, "word_y", tri)
    stage.text(W / 2, H / 2 + 8 + y_shift, "SLAM", "black", 104, stage.rgba(palette.ink), anchor="center", valign="middle")
    resized = layer.resize(
        (max(1, int(layer.size[0] * scale)), max(1, int(layer.size[1] * scale))),
        stage.Image.Resampling.LANCZOS,
    )
    stage.im.alpha_composite(resized, ((layer.size[0] - resized.size[0]) // 2, (layer.size[1] - resized.size[1]) // 2))
    stage.d = stage.Draw(stage.im)
    stage.text(W / 2, 58, "MAKE IT", "bold", 18, stage.rgba(palette.text_dim, int(255 * tri)), tracking=6, anchor="center")
    stage.rect(W / 2 - 150, 292, 300 * _mix(style, "underline_wipe", _lag(tri, 0.4)), 12, stage.rgba(palette.primary))


@_drawer("glass")
def _glass(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    drift = math.sin(phase * math.tau)
    stage.ellipse(40 + drift * 26, -20, 320, 300, stage.rgba(palette.spot("glow"), 220))
    stage.ellipse(380 - drift * 34, 120, 340, 280, stage.rgba(palette.accent, 180))
    stage.ellipse(220, 200 + drift * 18, 240, 200, stage.rgba(palette.primary, 150))
    stage.blur(10)
    card_y = 86 + _mix(style, "card_y", tri)
    alpha = _mix(style, "card_opacity", tri)
    stage.frost(146, card_y, 428, 220, 28, tint=palette.surface, tint_a=int(78 * max(alpha, 0)), border_a=int(120 * max(alpha, 0)))
    stage.text(360, card_y + 78, "Soft glass", "bold", 44, stage.rgba(palette.ink, int(255 * alpha)), anchor="center")
    stage.text(360, card_y + 132, "FROSTED PANEL", "sans", 15, stage.rgba(palette.text_dim, int(255 * alpha)), tracking=3, anchor="center")


@_drawer("brutalist")
def _brutalist(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    scale = _mix(style, "pop_scale", tri)
    shadow = _mix(style, "shadow_drop", tri)
    cw, ch = 420 * scale, 230 * scale
    cx = (W - cw) / 2
    cy = 88 + (1 - scale) * 36
    stage.rrect(cx + shadow, cy + shadow, cw, ch, 24, stage.rgba(palette.ink))
    stage.rrect(cx, cy, cw, ch, 24, stage.rgba(palette.surface), stage.rgba(palette.ink), 6)
    stage.text(cx + 32, cy + 34, "BRUTAL", "black", max(20, int(62 * scale)), stage.rgba(palette.ink))
    stage.rrect(cx + 32, cy + ch - 74, 160, 44, 22, stage.rgba(palette.primary), stage.rgba(palette.ink), 4)
    stage.text(cx + 112, cy + ch - 52, "MOTION", "bold", 15, stage.rgba(palette.ink), tracking=1, anchor="center", valign="middle")


@_drawer("chalk")
def _chalk(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    stage.rect(0, 0, W, 28, stage.rgba("#0C241C", 110))
    stage.rect(0, H - 34, W, 34, stage.rgba("#0C241C", 100))
    for x, y in ((48, 60), (180, 340), (640, 48), (680, 220), (300, 40)):
        stage.ellipse(x, y, 3, 3, stage.rgba(palette.spot("dust"), 100))
    drawn = 1 - _mix(style, "stroke_draw", tri)
    stage.arc(64, 78, 210, 210, -90, -90 + 360 * drawn, stage.rgba(palette.ink), 8)
    stage.line(320, 250, 320 + 280 * drawn, 248, stage.rgba(palette.primary), 7)
    ink = stage.rgba(palette.ink, int(255 * _mix(style, "word_opacity", _lag(tri, 0.28))))
    stage.text(330, 150, "explain", "chalk", 54, ink)
    dust = 0.35 + 0.65 * abs(math.sin(phase * math.tau))
    stage.ellipse(560, 210, 7, 7, stage.rgba(palette.spot("dust"), int(150 * dust)))


@_drawer("isometric")
def _isometric(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    stage.ellipse(200, 286, 320, 40, stage.rgba(palette.ink, 28))
    specs = ((250, 168, palette.primary), (385, 128, palette.accent), (310, 214, palette.spot("sand")))
    bob = math.sin(phase * math.tau) * 4
    for index, (cx, cy, color) in enumerate(specs):
        y_off = _mix(style, "block_y", _lag(tri, index * 0.18))
        extra = bob if index == 0 else 0
        _cube(stage, cx, cy + y_off + extra, color)
    stage.rrect(48, 42, 92, 34, 12, stage.rgba(palette.surface))
    stage.text(94, 59, "API", "bold", 16, stage.rgba(palette.ink), anchor="center", valign="middle")


@_drawer("signal")
def _signal(stage: Stage, style: Style, tri: float, phase: float) -> None:
    palette = style.palette
    stage.rect(0, 0, W, H, stage.rgba(palette.background))
    for x in range(70, 660, 40):
        stage.line(x, 78, x, 300, stage.rgba(palette.spot("grid")), 1)
    for y in range(78, 301, 44):
        stage.line(70, y, 650, y, stage.rgba(palette.spot("grid")), 1)
    bars = ((80, palette.secondary), (130, palette.secondary), (100, palette.primary), (170, palette.accent))
    for index, (height, color) in enumerate(bars):
        grown = _mix(style, "bar_grow", _lag(tri, index * 0.08))
        stage.rect(100 + index * 64, 286 - height * grown, 34, height * grown, stage.rgba(color))
    points = [(390, 250), (450, 190), (510, 210), (570, 120), (640, 150)]
    stage.polyline(points, 1 - _mix(style, "line_draw", tri), stage.rgba(palette.primary), 3)
    shown = round(32 * _mix(style, "count_up", tri))
    stage.text(78, 36, f"{shown}%", "din", 40, stage.rgba(palette.ink))
    stage.text(210, 52, "ACTIVATION", "mono", 14, stage.rgba(palette.text_dim))
