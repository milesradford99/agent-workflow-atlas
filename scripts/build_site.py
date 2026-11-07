"""Build the browsable catalog: one self-contained HTML page with every workflow in it.

Usage:
  python scripts/build_site.py                      write site/index.html
  python scripts/build_site.py --out DIR            write DIR/index.html
  python scripts/build_site.py --repo-url URL       link each entry to its file at URL/blob/main/...

The page needs no server: open site/index.html in a browser. Alongside it go one
static page per workflow (w/<ID>/), catalog.json and catalog.csv, and with --site-url
a sitemap. The Pages workflow publishes all of it.
"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

from catalog import ROOT, load_taxonomy, read_front_matter, species_files
import site_pages
from shapes import to_mermaid

TEMPLATE = Path(__file__).with_name("site_template.html")
DIAGRAM_RE = re.compile(r"\n*<!-- shape diagram:.*?<!-- end shape diagram -->\n*", re.S)


def section(body, title):
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


def intro(body):
    """Everything between the title line and the first ## heading, minus the generated diagram."""
    body = DIAGRAM_RE.sub("\n\n", body)
    m = re.search(r"^# .*?\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    lines = (m.group(1) if m else "").strip().split("\n")
    # the first line repeats the place, autonomy and status, which the page shows as badges
    return "\n".join(lines[1:]).strip() if lines and lines[0].startswith("`") else "\n".join(lines).strip()


def repo_url():
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return ""
    url = re.sub(r"^git@github\.com:", "https://github.com/", url)
    return re.sub(r"\.git$", "", url) if url.startswith("https://") else ""


def records(tax):
    out = []
    for path in species_files():
        fm, problem = read_front_matter(path)
        if problem:
            raise SystemExit(f"{path.relative_to(ROOT)}: {problem} (run scripts/validate.py)")
        text = path.read_text()
        body = text.split("\n---\n", 1)[1]
        runs = section(body, "Public runs")
        grade = re.search(r"\*\*(Strong|Partial|Weak|None found)\*\*", runs)
        kingdom = tax["kingdoms"].get(fm["kingdom"], {})
        phylum = kingdom.get("phyla", {}).get(fm["phylum"], {})
        tags = fm.get("tags") or {}
        out.append({
            "id": fm["id"], "name": fm["name"],
            "kingdom": fm["kingdom"], "kingdomName": kingdom.get("name", ""),
            "phylum": fm["phylum"], "phylumName": phylum.get("name", ""),
            "class": fm["class"], "deliverable": fm["deliverable"], "shape": fm["shape"],
            "autonomy": fm["autonomy"], "checkpoints": fm["checkpoints"], "patterns": fm["patterns"],
            "variants": fm.get("variants") or [], "evidence": fm["evidence"], "status": fm["status"],
            "risk": tags.get("risk", ""), "region": tags.get("region") or [],
            "lastVerified": str(fm["last_verified"]),
            "coverage": grade.group(1) if grade else "",
            "runs": len(re.findall(r"^- \[", runs, re.M)),
            "path": path.parent.relative_to(ROOT).as_posix(),
            "unplaced": path.parent.parent.name == "unplaced",
            "kit": (path.parent / "variants" / "claude-code.md").is_file(),
            "mermaid": to_mermaid(fm["shape"]),
            "intro": intro(body),
            "steps": section(body, "Steps"),
            "publicRuns": runs,
            "sources": section(body, "Sources"),
        })
    return sorted(out, key=lambda w: w["id"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "site"))
    ap.add_argument("--repo-url", default=None)
    ap.add_argument("--site-url", default="", help="published base URL, for canonical links, previews and the sitemap")
    args = ap.parse_args()
    tax = load_taxonomy()
    data = {
        "repo": args.repo_url if args.repo_url is not None else repo_url(),
        "taxonomy": {k: {"name": v["name"], "phyla": {p: {"name": ph["name"], "classes": ph["classes"]} for p, ph in v["phyla"].items()}}
                     for k, v in tax["kingdoms"].items()},
        "workflows": records(tax),
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = TEMPLATE.read_text().replace("/*__DATA__*/null", blob)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html)
    site_url = args.site_url.rstrip("/")
    site_pages.write_all(out, data, site_url)
    shutil.copyfile(ROOT / "docs" / "images" / "og.png", out / "og.png")
    print(f"Wrote {out}/: index.html, {len(data['workflows'])} workflow pages, catalog.json, catalog.csv")


if __name__ == "__main__":
    main()
