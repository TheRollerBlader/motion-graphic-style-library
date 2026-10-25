"""A single-file CSS gallery. Each tile loops the style's signature move."""

from __future__ import annotations

from pathlib import Path

from motionstyle_core.model import Style

# Inner markup uses {token} placeholders filled from the palette. CSS braces stay as-is.
_STAGES: dict[str, tuple[str, str]] = {
    "swiss": (
        """
        <i class="red"></i>
        <i class="index">01 / 08</i>
        <b>SWISS</b>
        <i class="rule"></i>
        """,
        """
        .s-swiss { background: {background}; color: {ink}; }
        .s-swiss .red { position:absolute; inset:0 auto 0 0; width:34%; background:{primary}; transform-origin:left; animation: wipe 2.8s cubic-bezier(.77,0,.18,1) infinite; }
        .s-swiss .index { position:absolute; left:6%; top:12%; color:{background}; font-size:12px; letter-spacing:.14em; z-index:1; }
        .s-swiss b { position:absolute; left:42%; top:36%; font-size:34px; letter-spacing:.04em; white-space:nowrap; }
        .s-swiss .rule { position:absolute; left:48%; top:68%; width:18%; height:2px; background:{ink}; transform-origin:left; animation: wipe 2.8s linear infinite; }
        """,
    ),
    "kinetic": (
        """
        <small>MAKE IT</small>
        <b>SLAM</b>
        <i class="bar"></i>
        """,
        """
        .s-kinetic { background:{background}; color:{ink}; }
        .s-kinetic small { position:absolute; top:16%; left:0; right:0; text-align:center; letter-spacing:.4em; color:{text_dim}; font-size:12px; }
        .s-kinetic b { position:absolute; inset:0; display:grid; place-items:center; font-size:64px; animation: slam 1.6s cubic-bezier(.34,1.56,.64,1) infinite; }
        .s-kinetic .bar { position:absolute; left:28%; right:28%; bottom:22%; height:8px; background:{primary}; transform-origin:left; animation: wipe 1.6s ease-out infinite; }
        """,
    ),
    "glass": (
        """
        <i class="a"></i><i class="b"></i><i class="c"></i><i class="card"><b>Soft glass</b><small>FROSTED PANEL</small></i>
        """,
        """
        .s-glass { background:{background}; }
        .s-glass .a, .s-glass .b, .s-glass .c { position:absolute; border-radius:50%; filter:blur(8px); }
        .s-glass .a { width:55%; height:70%; left:-8%; top:-20%; background:{glow}; animation: drift 6s ease-in-out infinite; }
        .s-glass .b { width:48%; height:60%; right:-6%; bottom:-10%; background:{accent}; animation: drift 7s ease-in-out infinite reverse; }
        .s-glass .c { width:36%; height:46%; left:30%; bottom:-8%; background:{primary}; animation: drift 5.5s ease-in-out infinite; }
        .s-glass .card { position:absolute; left:16%; right:16%; top:22%; bottom:22%; border-radius:18px; border:1px solid rgba(255,255,255,.35); background:rgba(244,247,255,.16); backdrop-filter:blur(10px); display:grid; place-items:center; align-content:center; color:{ink}; animation: float 3.2s ease-in-out infinite; }
        .s-glass b { font-size:28px; font-weight:560; }
        .s-glass small { letter-spacing:.18em; color:{text_dim}; font-size:10px; }
        """,
    ),
    "brutalist": (
        """
        <i class="card"><b>BRUTAL</b><em>MOTION</em></i>
        """,
        """
        .s-brutalist { background:{background}; }
        .s-brutalist .card { position:absolute; left:14%; right:14%; top:22%; bottom:22%; background:{surface}; color:{ink}; border:4px solid {ink}; border-radius:18px; box-shadow:8px 8px 0 {ink}; display:flex; flex-direction:column; justify-content:space-between; padding:8% 8%; animation: pop 1.8s cubic-bezier(.34,1.56,.64,1) infinite; }
        .s-brutalist b { font-size:32px; letter-spacing:.04em; }
        .s-brutalist em { align-self:flex-start; font-style:normal; font-size:12px; letter-spacing:.12em; background:{primary}; border:3px solid {ink}; border-radius:999px; padding:6px 12px; box-shadow:4px 4px 0 {ink}; }
        """,
    ),
    "chalk": (
        """
        <svg viewBox="0 0 320 180" class="board"><circle cx="78" cy="90" r="46" fill="none" stroke="{ink}" stroke-width="4" class="draw"/><line x1="150" y1="108" x2="270" y2="108" stroke="{primary}" stroke-width="4" class="draw"/></svg>
        <b>explain</b>
        """,
        """
        .s-chalk { background:{background}; color:{ink}; }
        .s-chalk svg { position:absolute; inset:0; width:100%; height:100%; }
        .s-chalk .draw { stroke-dasharray: 300; stroke-dashoffset:300; animation: draw 2.8s ease-in-out infinite; }
        .s-chalk b { position:absolute; left:46%; top:28%; font-family:"Chalkduster","Bradley Hand",cursive; font-size:32px; font-weight:400; animation: fade 2.8s ease-out infinite; }
        """,
    ),
    "isometric": (
        """
        <i class="cube c1"></i><i class="cube c2"></i><i class="cube c3"></i><small>API</small>
        """,
        """
        .s-isometric { background:{background}; }
        .s-isometric .cube { position:absolute; width:42px; height:42px; transform:rotate(45deg) skew(-12deg,-12deg); }
        .s-isometric .c1 { left:28%; top:42%; background:{primary}; animation: drop 2.4s ease-out infinite; }
        .s-isometric .c2 { left:46%; top:30%; background:{accent}; animation: drop 2.4s ease-out .15s infinite; }
        .s-isometric .c3 { left:40%; top:52%; background:{sand}; animation: drop 2.4s ease-out .3s infinite; }
        .s-isometric small { position:absolute; left:8%; top:12%; background:{surface}; color:{ink}; border-radius:10px; padding:4px 10px; font-size:12px; }
        """,
    ),
    "signal": (
        """
        <b class="num">32%</b>
        <i class="bars"><span></span><span></span><span></span><span></span></i>
        <svg viewBox="0 0 120 60" class="line"><polyline points="0,40 30,28 55,34 85,12 120,20" fill="none" stroke="{primary}" stroke-width="2" class="draw"/></svg>
        """,
        """
        .s-signal { background:{background}; color:{ink}; }
        .s-signal .num { position:absolute; left:8%; top:10%; font-size:28px; font-variant-numeric:tabular-nums; }
        .s-signal .bars { position:absolute; left:8%; bottom:18%; display:flex; align-items:flex-end; gap:8px; height:46%; }
        .s-signal .bars span { width:16px; background:{secondary}; transform-origin:bottom; animation: grow 2s ease-out infinite; }
        .s-signal .bars span:nth-child(1){ height:46%; }
        .s-signal .bars span:nth-child(2){ height:70%; animation-delay:.08s; }
        .s-signal .bars span:nth-child(3){ height:58%; background:{primary}; animation-delay:.16s; }
        .s-signal .bars span:nth-child(4){ height:90%; background:{accent}; animation-delay:.24s; }
        .s-signal .line { position:absolute; right:6%; bottom:16%; width:42%; }
        .s-signal .draw { stroke-dasharray:180; stroke-dashoffset:180; animation: draw 2.2s ease-in-out infinite; }
        """,
    ),
    "papercut": (
        """
        <i class="s1"></i><i class="s2"></i><i class="s3"><b>Story</b></i><i class="tab"></i>
        """,
        """
        .s-papercut { background:{background}; }
        .s-papercut i { position:absolute; border-radius:16px; box-shadow:0 12px 18px rgba(80,50,30,.18); }
        .s-papercut .s1 { left:14%; right:18%; top:30%; bottom:16%; background:{secondary}; animation: sheet 2.6s ease-out infinite; }
        .s-papercut .s2 { left:20%; right:14%; top:22%; bottom:20%; background:{sheet_pink}; animation: sheet 2.6s ease-out .12s infinite; }
        .s-papercut .s3 { left:24%; right:20%; top:14%; bottom:26%; background:{surface}; color:{ink}; display:grid; place-items:center; animation: sheet 2.6s ease-out .24s infinite; }
        .s-papercut .tab { left:16%; top:20%; width:16%; height:14%; background:{primary}; animation: sheet 2.6s ease-out .08s infinite; }
        .s-papercut b { font-family:Georgia,serif; font-size:32px; }
        """,
    ),
    "neon": (
        """
        <i class="floor"></i>
        <b>NEON</b>
        """,
        """
        .s-neon { background:{background}; }
        .s-neon .floor { position:absolute; left:0; right:0; top:62%; height:1px; background:{accent}; box-shadow:0 0 12px {accent}; }
        .s-neon b { position:absolute; inset:0; display:grid; place-items:center; font-size:52px; letter-spacing:.16em; color:{primary}; text-shadow:0 0 12px {primary}, 0 0 28px {primary}; animation: flicker 2.4s linear infinite; }
        """,
    ),
    "documentary": (
        """
        <i class="still"></i>
        <i class="lower">Field notes</i>
        """,
        """
        .s-documentary { background:{background}; overflow:hidden; }
        .s-documentary .still { position:absolute; left:-4%; right:-4%; top:0; height:72%; background:linear-gradient({primary}, {primary} 42%, {secondary} 43%, {background_raised}); animation: ken 8s linear infinite alternate; }
        .s-documentary .lower { position:absolute; left:0; bottom:14%; background:{primary}; color:{background}; font-family:Georgia,serif; padding:8px 18px; animation: rise 2.4s ease-out infinite; }
        """,
    ),
    "playful": (
        """
        <i class="d1"></i><i class="d2"></i><i class="d3"></i><b>Hello</b>
        """,
        """
        .s-playful { background:{background}; color:{ink}; }
        .s-playful i { position:absolute; border-radius:50%; animation: hop 1.6s cubic-bezier(.34,1.56,.64,1) infinite; }
        .s-playful .d1 { width:54px; height:54px; left:16%; top:32%; background:{primary}; }
        .s-playful .d2 { width:78px; height:78px; left:40%; top:24%; background:{secondary}; animation-delay:.12s; }
        .s-playful .d3 { width:48px; height:48px; right:16%; top:36%; background:{accent}; animation-delay:.24s; }
        .s-playful b { position:absolute; left:0; right:0; bottom:14%; text-align:center; font-size:28px; }
        """,
    ),
    "blueprint": (
        """
        <small>A-01</small>
        <svg viewBox="0 0 320 180"><rect x="36" y="28" width="248" height="110" fill="none" stroke="{primary}" stroke-width="1.5" class="draw"/></svg>
        <em>490</em>
        """,
        """
        .s-blueprint { background:{background}; color:{ink}; background-image:linear-gradient({primary}22 1px, transparent 1px), linear-gradient(90deg, {primary}22 1px, transparent 1px); background-size:16px 16px; }
        .s-blueprint svg { position:absolute; inset:0; width:100%; height:100%; }
        .s-blueprint .draw { stroke-dasharray:720; stroke-dashoffset:720; animation: draw 2.8s ease-in-out infinite; }
        .s-blueprint small { position:absolute; left:6%; top:8%; letter-spacing:.14em; font-size:12px; }
        .s-blueprint em { position:absolute; left:0; right:0; bottom:8%; text-align:center; color:{secondary}; font-style:normal; font-size:12px; letter-spacing:.12em; }
        """,
    ),
    "gradient": (
        """
        <i class="a"></i><i class="b"></i><i class="c"></i><b>Flow</b>
        """,
        """
        .s-gradient { background:{background}; }
        .s-gradient i { position:absolute; border-radius:50%; filter:blur(18px); }
        .s-gradient .a { width:60%; height:80%; left:-10%; top:-20%; background:{violet}; animation: drift 7s ease-in-out infinite; }
        .s-gradient .b { width:50%; height:70%; right:-8%; top:20%; background:{peach}; animation: drift 8s ease-in-out infinite reverse; }
        .s-gradient .c { width:40%; height:50%; left:30%; bottom:-10%; background:{blue}; animation: drift 6s ease-in-out infinite; }
        .s-gradient b { position:absolute; inset:0; display:grid; place-items:center; color:{ink}; font-size:48px; font-weight:500; animation: fade 3s ease-out infinite; }
        """,
    ),
    "comic": (
        """
        <i class="burst">POW</i>
        <i class="bubble">Again!</i>
        """,
        """
        .s-comic { background:{accent}; border:4px solid {ink}; box-sizing:border-box; }
        .s-comic .burst { position:absolute; left:18%; top:28%; width:90px; height:90px; display:grid; place-items:center; background:{primary}; color:{ink}; font-weight:800; clip-path:polygon(50% 0,60% 28%,90% 18%,72% 42%,100% 50%,72% 62%,88% 92%,58% 72%,50% 100%,40% 72%,12% 88%,28% 58%,0 50%,28% 38%,10% 12%,42% 28%); animation: pop 1.3s cubic-bezier(.34,1.56,.64,1) infinite; }
        .s-comic .bubble { position:absolute; right:10%; top:18%; background:{surface}; color:{ink}; border:3px solid {ink}; border-radius:14px; padding:10px 14px; box-shadow:4px 4px 0 {ink}; animation: pop 1.3s cubic-bezier(.34,1.56,.64,1) .12s infinite; }
        """,
    ),
}

_KEYFRAMES = """
@keyframes wipe { 0%,100% { transform: scaleX(0); } 45%,70% { transform: scaleX(1); } }
@keyframes slam { 0%,100% { transform: scale(1.22); } 55%,75% { transform: scale(1); } }
@keyframes float { 0%,100% { transform: translateY(16px); opacity:.2; } 40%,70% { transform: translateY(0); opacity:1; } }
@keyframes drift { 0%,100% { transform: translate3d(0,0,0); } 50% { transform: translate3d(16px,-12px,0); } }
@keyframes pop { 0%,100% { transform: scale(.86); } 50%,70% { transform: scale(1); } }
@keyframes draw { 0%,100% { stroke-dashoffset: 740; } 55%,80% { stroke-dashoffset: 0; } }
@keyframes drop { 0%,100% { transform: rotate(45deg) skew(-12deg,-12deg) translateY(-28px); opacity:0; } 45%,75% { transform: rotate(45deg) skew(-12deg,-12deg) translateY(0); opacity:1; } }
@keyframes grow { 0%,100% { transform: scaleY(0); } 40%,80% { transform: scaleY(1); } }
@keyframes sheet { 0%,100% { transform: translate(-28px, 16px); } 45%,75% { transform: translate(0,0); } }
@keyframes flicker { 0%,100% { opacity:0; } 12%,18% { opacity:1; } 24% { opacity:.2; } 36%,80% { opacity:1; } }
@keyframes ken { 0% { transform: scale(1); } 100% { transform: scale(1.08); } }
@keyframes rise { 0%,100% { transform: translateY(14px); opacity:0; } 30%,80% { transform: translateY(0); opacity:1; } }
@keyframes hop { 0%,100% { transform: translateY(10px) scale(.7,1.05); } 45%,70% { transform: translateY(0) scale(1,1); } }
@keyframes fade { 0%,100% { opacity:0; transform: translateY(8px); } 35%,75% { opacity:1; transform: translateY(0); } }
"""


def _fill(template: str, style: Style) -> str:
    values = {
        "background": style.palette.background,
        "background_raised": style.palette.background_raised,
        "surface": style.palette.surface,
        "ink": style.palette.ink,
        "text": style.palette.text,
        "text_dim": style.palette.text_dim,
        "primary": style.palette.primary,
        "secondary": style.palette.secondary,
        "accent": style.palette.accent,
    }
    for name, value in style.palette.spots:
        values[name] = value
    rendered = template
    for name in sorted(values, key=len, reverse=True):
        rendered = rendered.replace("{" + name + "}", values[name])
    return rendered


def render_gallery(styles: tuple[Style, ...]) -> str:
    by_id = {style.id: style for style in styles}
    missing = [style_id for style_id in by_id if style_id not in _STAGES]
    if missing:
        raise KeyError(f"Gallery is missing an animation for: {', '.join(missing)}")
    cards = []
    css = [_KEYFRAMES]
    for style in styles:
        inner, extra = _STAGES[style.id]
        cards.append(
            f"""<article class="card">
  <div class="stage s-{style.id}">{_fill(inner, style)}</div>
  <h2>{style.name}</h2>
  <p>{style.tagline}</p>
  <code>{style.library}</code>
</article>"""
        )
        css.append(_fill(extra, style))
    card_html = "\n".join(cards)
    css_html = "\n".join(css)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Motion style studies</title>
  <style>
    :root {{ color-scheme: dark; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; background:#101014; color:#f4f1ea; font-family: Helvetica, Arial, sans-serif; }}
    header {{ padding: 56px 6vw 8px; max-width: 1100px; }}
    h1 {{ font-weight: 560; letter-spacing: -0.03em; font-size: clamp(32px, 5vw, 56px); margin: 0 0 8px; }}
    header p {{ max-width: 62ch; color: #c8c2b6; line-height: 1.5; }}
    .grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 22px; padding: 28px 6vw 72px; }}
    .card h2 {{ margin: 10px 0 0; font-size: 16px; font-weight: 650; }}
    .card p {{ margin: 4px 0; color: #b7b1a6; font-size: 14px; }}
    code {{ color: #8d887e; font-size: 12px; }}
    .stage {{ position:relative; aspect-ratio: 16/9; overflow:hidden; border-radius: 12px; }}
    .stage b, .stage small, .stage em {{ font-weight: 800; }}
    {css_html}
    @media (prefers-reduced-motion: reduce) {{
      .stage, .stage * {{ animation: none !important; }}
    }}
  </style>
</head>
<body>
  <header>
    <p>Motion graphic style library</p>
    <h1>Fourteen studies, looping.</h1>
    <p>Each tile is the signature move of one Python style library. The settled pose is what you get with reduced motion. Open a style's spec in <code>catalog/</code> for the tokens an agent should follow.</p>
  </header>
  <main class="grid">
    {card_html}
  </main>
</body>
</html>
"""


def write_gallery(styles: tuple[Style, ...], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_gallery(styles), encoding="utf-8")
    return target
