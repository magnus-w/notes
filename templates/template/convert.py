#!/usr/bin/env python3
"""
Convert a markdown file to a self-contained HTML document.

Usage:
  python3 template/convert.py notes/MyNote.md
  python3 template/convert.py notes/MyNote.md output/MyNote.html

Frontmatter (optional YAML block at the top of the markdown file):
  ---
  title: Document Title
  subtitle: A short description or ingress
  from: Magnus Westerberg
  date: 2026-06-18
  ---

If 'title' is missing from frontmatter, the first # heading is used.
If 'date' is missing, today's date is used.
"""

import sys
import re
import subprocess
from datetime import date
from pathlib import Path


TEMPLATE = Path(__file__).parent / "template.html"


def parse_frontmatter(text):
    """Return (meta dict, body without frontmatter)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip().lower()] = val.strip()
    return meta, body


def extract_h1(text):
    """Return (title, body with h1 removed) or (None, body)."""
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        body = text[: m.start()] + text[m.end():]
        return title, body.lstrip("\n")
    return None, text


def md_to_html(text):
    """Convert markdown to an HTML fragment using pandoc."""
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html", "--no-highlight"],
        input=text,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def convert(src_path, dst_path=None):
    src = Path(src_path)
    if not src.exists():
        sys.exit(f"Error: file not found: {src}")

    dst = Path(dst_path) if dst_path else src.with_suffix(".html")

    raw = src.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)

    title = meta.get("title", "")
    if not title:
        title, body = extract_h1(body)
        title = title or src.stem

    subtitle = meta.get("subtitle", meta.get("description", ""))
    sender   = meta.get("from", meta.get("author", ""))
    doc_date = meta.get("date", date.today().isoformat())

    content = md_to_html(body)

    template = TEMPLATE.read_text(encoding="utf-8")
    html = (template
        .replace("{{title}}",    title)
        .replace("{{subtitle}}", subtitle)
        .replace("{{from}}",     sender)
        .replace("{{date}}",     str(doc_date))
        .replace("{{content}}",  content)
    )

    dst.write_text(html, encoding="utf-8")
    print(f"✓ {dst}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
