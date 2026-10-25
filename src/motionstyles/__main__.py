"""Command line for the motion-graphic style libraries."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from motionstyles import catalog, get_style


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="motionstyles", description="Inspect and export motion-graphic styles.")
    sub = parser.add_subparsers(dest="command", required=True)

    listing = sub.add_parser("list", help="List every style library")
    listing.add_argument("--json", action="store_true")

    show = sub.add_parser("show", help="Print a style.md spec")
    show.add_argument("style")

    export = sub.add_parser("export", help="Write one style as md, json, css, or ts")
    export.add_argument("style")
    export.add_argument("--format", choices=("md", "json", "css", "ts"), default="md")
    export.add_argument("-o", "--output", help="File to write. Prints to stdout when omitted.")

    export_all = sub.add_parser("export-all", help="Write a style.md for every library")
    export_all.add_argument("directory")

    previews = sub.add_parser("previews", help="Render a looping GIF study for every style")
    previews.add_argument("directory")
    previews.add_argument("--frames", type=int, default=36)

    gallery = sub.add_parser("gallery", help="Write the animated HTML gallery")
    gallery.add_argument("-o", "--output", default="docs/gallery.html")

    skills = sub.add_parser("skills", help="Regenerate agent skills from the libraries")
    skills.add_argument("-o", "--output", default=".cursor/skills")

    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            return _list(args.json)
        if args.command == "show":
            sys.stdout.write(get_style(args.style).to_style_md())
            return 0
        if args.command == "export":
            return _export(get_style(args.style), args.format, args.output)
        if args.command == "export-all":
            return _export_all(args.directory)
        if args.command == "previews":
            from motionstyle_core.preview import render_all

            for path in render_all(args.directory, frames=args.frames):
                print(path)
            return 0
        if args.command == "gallery":
            from motionstyle_core.gallery import write_gallery

            print(write_gallery(catalog(), args.output))
            return 0
        if args.command == "skills":
            from motionstyle_core.skills import write_skills

            for path in write_skills(catalog(), args.output):
                print(path)
            return 0
    except KeyError as exc:
        print(exc, file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1
    return 2


def _list(as_json: bool) -> int:
    styles = catalog()
    if as_json:
        payload = [
            {"id": style.id, "name": style.name, "library": style.library, "tagline": style.tagline, "bestFor": list(style.best_for)}
            for style in styles
        ]
        print(json.dumps(payload, indent=2))
        return 0
    for style in styles:
        print(f"{style.id:<14} {style.name:<22} {style.library:<26} {style.tagline}")
    return 0


def _export(style, fmt: str, output: str | None) -> int:
    rendered = {
        "md": style.to_style_md(),
        "json": style.to_json(),
        "css": style.to_css(),
        "ts": style.to_theme_ts(),
    }[fmt]
    if output:
        Path(output).write_text(rendered, encoding="utf-8")
        print(output)
    else:
        sys.stdout.write(rendered)
    return 0


def _export_all(directory: str) -> int:
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    for style in catalog():
        path = root / f"{style.id}.md"
        path.write_text(style.to_style_md(), encoding="utf-8")
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
