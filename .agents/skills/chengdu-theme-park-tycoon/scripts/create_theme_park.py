#!/usr/bin/env python3
"""Create a standalone Chengdu low-poly Theme Park Tycoon HTML file."""

from __future__ import annotations

import argparse
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_DIR / "assets" / "theme-park-tycoon.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the bundled Three.js Chengdu Theme Park Tycoon template."
    )
    parser.add_argument(
        "--output",
        "-o",
        default="theme-park-tycoon.html",
        help="Output HTML path. Defaults to theme-park-tycoon.html in the current directory.",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional replacement for the browser title and main HUD heading.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output path if it already exists.",
    )
    return parser.parse_args()


def replace_title(html: str, title: str) -> str:
    old = "春熙路太古里 Theme Park Tycoon"
    return html.replace(f"<title>{old}</title>", f"<title>{title}</title>").replace(
        f"<h1>{old}</h1>", f"<h1>{title}</h1>"
    )


def main() -> int:
    args = parse_args()
    output = Path(args.output).resolve()

    if not TEMPLATE.exists():
        raise SystemExit(f"Template not found: {TEMPLATE}")
    if output.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {output}. Use --force.")

    html = TEMPLATE.read_text(encoding="utf-8")
    if args.title:
        html = replace_title(html, args.title)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8", newline="\n")
    print(f"Created {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
