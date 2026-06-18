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

TOC_TOGGLE = """\
<input type="checkbox" id="toc-cb">
<label for="toc-cb" id="toc-toggle" role="button" tabindex="0" aria-label="Visa innehållsförteckning">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
    <line x1="2" y1="4" x2="14" y2="4"/>
    <line x1="2" y1="8" x2="14" y2="8"/>
    <line x1="2" y1="12" x2="14" y2="12"/>
  </svg>
</label>"""


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


def build_toc(content_html):
    """
    Parse h2/h3 from pandoc HTML output and return (toc_toggle, toc_nav).
    Returns ('', '') if fewer than 2 headings found.
    """
    headings = re.findall(
        r'<h([23])[^>]+id="([^"]+)"[^>]*>(.*?)</h\1>',
        content_html,
        re.DOTALL,
    )
    if len(headings) < 2:
        return '', ''

    items = []
    for level, hid, raw_text in headings:
        text = re.sub(r'<[^>]+>', '', raw_text).strip()
        cls  = 'toc-h2' if level == '2' else 'toc-h3'
        items.append(f'    <li class="{cls}"><a href="#{hid}">{text}</a></li>')

    toc_nav = (
        '  <nav id="toc" aria-label="Innehållsförteckning">\n'
        '    <p class="toc-label">Innehåll</p>\n'
        '    <ul id="toc-list">\n'
        + '\n'.join(items) + '\n'
        '    </ul>\n'
        '  </nav>'
    )
    return TOC_TOGGLE, toc_nav


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
    toc_toggle, toc_nav = build_toc(content)

    template = TEMPLATE.read_text(encoding="utf-8")
    html = (template
        .replace("{{title}}",      title)
        .replace("{{subtitle}}",   subtitle)
        .replace("{{from}}",       sender)
        .replace("{{date}}",       str(doc_date))
        .replace("{{content}}",    content)
        .replace("{{toc_toggle}}", toc_toggle)
        .replace("{{toc_nav}}",    toc_nav)
    )

    dst.write_text(html, encoding="utf-8")
    print(f"✓ {dst}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
