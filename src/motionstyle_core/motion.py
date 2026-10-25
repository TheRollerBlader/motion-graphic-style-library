"""Sample style clips. Easing matches the CSS exported with each style."""

from __future__ import annotations

import re

from motionstyle_core.model import Clip

_BEZIER = re.compile(
    r"^cubic-bezier\(\s*([-+0-9.]+)\s*,\s*([-+0-9.]+)\s*,\s*([-+0-9.]+)\s*,\s*([-+0-9.]+)\s*\)$"
)

# Named eases and their CSS cubic-bezier equivalents. y may leave 0..1 so
# ease-out-back can overshoot, the same way a CSS timing function does.
EASES: dict[str, str] = {
    "linear": "linear",
    "ease-out": "cubic-bezier(0.16, 1, 0.3, 1)",
    "ease-in-out": "cubic-bezier(0.65, 0, 0.35, 1)",
    "ease-out-back": "cubic-bezier(0.34, 1.56, 0.64, 1)",
}


def css_ease(ease: str) -> str:
    """Return a CSS timing-function for a clip ease name."""
    if ease == "linear":
        return "linear"
    if ease in EASES and ease != "linear":
        return EASES[ease]
    if _BEZIER.match(ease):
        return ease
    raise ValueError(f"Unsupported ease {ease!r}. Use linear, ease-out, ease-in-out, ease-out-back, or cubic-bezier().")


def apply_ease(ease: str, t: float) -> float:
    """Map linear time t (0..1) through a timing function."""
    t = min(1.0, max(0.0, t))
    if ease == "linear":
        return t
    spec = EASES.get(ease, ease)
    match = _BEZIER.match(spec)
    if not match:
        raise ValueError(f"Unsupported ease {ease!r}.")
    x1, y1, x2, y2 = (float(v) for v in match.groups())
    return _bezier_y(t, x1, y1, x2, y2)


def pose(clip: Clip, amount: float) -> float:
    """Sample a clip at a 0..1 mix of its full duration. 0 is the first pose, 1 is the last."""
    amount = min(1.0, max(0.0, amount))
    return sample_clip(clip, amount * clip.duration_s)


def sample_clip(clip: Clip, seconds: float) -> float:
    """Value of a clip at `seconds` from its start.

    Keyframe `t` is normalized 0..1 across the clip. Easing is applied inside
    each keyframe span, which is how CSS applies a timing function between
    keyframes. Time before the clip returns the first value. Time after the
    clip holds the last value.
    """
    keys = clip.keyframes
    if seconds <= 0:
        return keys[0].value
    if seconds >= clip.duration_s:
        return keys[-1].value
    u = seconds / clip.duration_s
    for start, end in zip(keys, keys[1:]):
        if u <= end.t or end is keys[-1]:
            span = end.t - start.t
            local = 0.0 if span == 0 else (u - start.t) / span
            local = min(1.0, max(0.0, local))
            eased = apply_ease(clip.ease, local)
            return start.value + (end.value - start.value) * eased
    return keys[-1].value


def _bezier_y(x: float, x1: float, y1: float, x2: float, y2: float) -> float:
    """Solve CSS cubic-bezier for y at time fraction x."""

    def bx(t: float) -> float:
        return 3 * (1 - t) ** 2 * t * x1 + 3 * (1 - t) * t**2 * x2 + t**3

    def by(t: float) -> float:
        return 3 * (1 - t) ** 2 * t * y1 + 3 * (1 - t) * t**2 * y2 + t**3

    def dx(t: float) -> float:
        return 3 * (1 - t) ** 2 * x1 + 6 * (1 - t) * t * (x2 - x1) + 3 * t**2 * (1 - x2)

    t = x
    for _ in range(10):
        slope = dx(t)
        if abs(slope) < 1e-6:
            break
        t = min(1.0, max(0.0, t - (bx(t) - x) / slope))
    return by(t)
