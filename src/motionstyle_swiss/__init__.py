"""Editorial Swiss. International Typographic Style, set in motion."""

from motionstyle_core import clip, font, make_style

STYLE = make_style(
    id="swiss",
    name="Editorial Swiss",
    tagline="A grid, a grotesque, and one red. Type does the explaining.",
    best_for=("strategy explainers", "essays", "product positioning", "serious software"),
    aliases=("swiss style", "international typographic style", "helvetica grid", "editorial print", "bauhaus grid"),
    palette=dict(
        background="#F3F0E8",
        background_raised="#E7E2D6",
        surface="#F7F4EC",
        ink="#111111",
        text="#111111",
        text_dim="#5E594F",
        primary="#E10600",
        primary_light="#FF3B30",
        primary_dark="#9E0500",
        secondary="#111111",
        accent="#E10600",
        danger="#E10600",
        ok="#1F6B4A",
        info="#1D4E89",
    ),
    display=font("Helvetica Neue, Helvetica, Arial, sans-serif", 700, 0.04, "upper", 0.9),
    body=font("Helvetica Neue, Helvetica, Arial, sans-serif", 500, 0.01, "none", 1.35),
    mono=font("SF Mono, ui-monospace, Menlo, Consolas, monospace", 500, 0.08, "upper", 1.2),
    shape=dict(radius_px=0, border_px=1, border_color="#111111", shadow="none", blur_px=0, notes="Corners are square. Rules are 1px. Red is never a large fill except a single signal block."),
    motion_character="Mechanical and exact. Elements wipe, crop, and settle their tracking. They arrive and stop. Nothing bounces, blurs, or overshoots.",
    clips=(
        clip("wipe_x", 0.55, "cubic-bezier(0.77, 0, 0.18, 1)", "scaleX", ((0, 0), (1, 1)), "Transform origin is the left edge. Use for rules, red blocks, and masks."),
        clip("tracking_settle", 0.7, "cubic-bezier(0.22, 1, 0.36, 1)", "letterSpacing", ((0, 0.22), (1, 0.04)), "Display words tighten into the grid. Do not fade them in from nothing."),
        clip("rise_mask", 0.5, "cubic-bezier(0.22, 1, 0.36, 1)", "y", ((0, 28), (1, 0)), "Reveal through a crop. The type moves up and the mask stays put."),
        clip("idle_rule", 3.2, "linear", "x", ((0, 0), (1, 64)), "A 1px rule travels one column, then loops. Type does not bob."),
    ),
    stagger_s=0.06,
    idle="One hairline travels a single column and loops. Everything else holds.",
    chrome=(
        "12 columns, 64px outer margin, 24px gutter on the 1920 canvas. Every edge lands on a column.",
        "The signal red appears once per frame: a square, a rule, or a single word.",
        "A mono index sits in the top safe margin, like 01 / 08. No pills, badges, or icons.",
        "Body copy is flush left, ragged right, never justified and never centered under a huge title.",
    ),
    primitives=(
        "GridFrame: column lines in ink at low contrast, shown only when the beat is about structure.",
        "IndexMark: mono index plus a 10px red square.",
        "DisplayCrop: an oversized uppercase line revealed by rise_mask or wipe_x.",
        "Hairline: a 1px ink rule driven by wipe_x.",
    ),
    caption="Bottom margin, one line, flush left. A red square marks the current clause. The rest of the sentence is text_dim. No capsule behind the words.",
    dos=(
        "Align type and rules to the same column edges.",
        "Reveal type with a wipe, a crop, or a tracking settle.",
        "Leave more paper empty than you fill.",
    ),
    donts=(
        "Do not round corners, add drop shadows, gradients, or glow.",
        "Do not bounce, overshoot, or ease with a spring.",
        "Do not use more than two type sizes in one frame.",
        "Do not center a paragraph.",
    ),
    agent_rules=(
        "A radius other than 0 is wrong for this style.",
        "A second red element means the frame is shouting. Remove one.",
        "Prefer a wipe or a crop over a fade.",
    ),
)
