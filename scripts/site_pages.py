"""Static outputs for the catalog site: one page per workflow, data exports and a sitemap.

The interactive page (site_template.html) is for browsing. These files are for linking,
sharing and search engines: each workflow gets a plain HTML page at w/<ID>/ with its own
title, description and preview image, and the whole catalog is downloadable as JSON and CSV.
"""
import csv
import html
import io
import json
import re

CSV_FIELDS = ["id", "name", "kingdom", "kingdomName", "phylum", "phylumName", "class", "deliverable",
              "autonomy", "checkpoints", "patterns", "variants", "evidence", "coverage", "runs", "risk",
              "region", "status", "lastVerified", "kit", "shape", "url", "source"]


def esc(s):
    return html.escape(str(s), quote=True)


def inline(text, link):
    """Markdown inline: code, citations, links, bold, italic, bare URLs."""
    parts, last = [], 0
    for m in re.finditer(r"`([^`]+)`|\[\[(\d+)\]\]\(#sources\)|\[([^\]]+)\]\(([^)\s]+)\)|\*\*([^*]+)\*\*|(?<![\w*])\*([^*\n]+)\*|(https?://[^\s<)]+)", text):
        parts.append(esc(text[last:m.start()]))
        code, cite, label, url, bold, ital, bare = m.groups()
        if code is not None:
            parts.append(f"<code>{esc(code)}</code>")
        elif cite is not None:
            parts.append(f'<sup><a href="#src-{cite}">[{cite}]</a></sup>')
        elif label is not None:
            parts.append(f'<a href="{esc(link(url))}">{inline(label, link)}</a>')
        elif bold is not None:
            parts.append(f"<strong>{inline(bold, link)}</strong>")
        elif ital is not None:
            parts.append(f"<em>{inline(ital, link)}</em>")
        else:
            parts.append(f'<a href="{esc(bare)}">{esc(bare)}</a>')
        last = m.end()
    parts.append(esc(text[last:]))
    return "".join(parts)


def markdown(text, link, sources=False):
    """Block Markdown: paragraphs and flat numbered or bulleted lists."""
    out, kind = [], None
    for line in text.split("\n"):
        line = line.rstrip()
        ol, ul = re.match(r"^(\d+)\.\s+(.*)$", line), re.match(r"^[-*]\s+(.*)$", line)
        if ol or ul:
            tag = "ol" if ol else "ul"
            if kind != tag:
                if kind:
                    out.append(f"</{kind}>")
                out.append(f"<{tag}>")
                kind = tag
            attrs = f' value="{ol[1]}"' + (f' id="src-{ol[1]}"' if sources else "") if ol else ""
            out.append(f"<li{attrs}>{inline(ol[2] if ol else ul[1], link)}</li>")
            continue
        if kind:
            out.append(f"</{kind}>")
            kind = None
        if line.strip():
            out.append(f"<p>{inline(line, link)}</p>")
    if kind:
        out.append(f"</{kind}>")
    return "\n".join(out)


def resolver(repo, path):
    """Turn a link written inside a workflow README into an absolute or site-relative URL."""
    def link(url):
        if re.match(r"^(https?:|#|mailto:)", url):
            return url
        stack = []
        for part in f"{path}/{url}".split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        target = "/".join(stack)
        return f"{repo}/blob/main/{target}" if repo else f"../../../{target}"
    return link


def description(w):
    first = re.sub(r"\s+", " ", re.sub(r"\[\[\d+\]\]\(#sources\)|\*\*|`", "", w["steps"].split("\n")[0] if w["steps"] else ""))
    first = re.sub(r"^\d+\.\s*", "", first)
    text = f"{w['name']}: how professionals in {w['phylumName'].lower()} run this agent workflow, step by step, with human checkpoints and sources. {first}"
    return text if len(text) <= 300 else text[:297].rstrip() + "…"


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<style>
:root {{ --bg:#f7f6f2; --panel:#fff; --ink:#1d2433; --muted:#5b6475; --line:#e3e1d9; --accent:#2f5bd3; --chip:#eef0f5; --stop-bg:#fde2e1; --stop-ink:#8a1c13; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#12151c; --panel:#1a1f29; --ink:#e7eaf0; --muted:#a2abbb; --line:#2b3240; --accent:#7c9cff; --chip:#252c39; --stop-bg:#4a1f1c; --stop-ink:#ffc9c3; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","PingFang SC","Microsoft YaHei",sans-serif; }}
a {{ color:var(--accent); }}
header {{ background:var(--panel); border-bottom:1px solid var(--line); padding:12px 20px; display:flex; gap:16px; align-items:center; flex-wrap:wrap; }}
header a.brand {{ font-weight:700; color:var(--ink); text-decoration:none; margin-right:auto; }}
main {{ max-width:880px; margin:0 auto; padding:24px 20px 60px; }}
.place {{ color:var(--muted); font-size:14px; }}
h1 {{ margin:4px 0 12px; font-size:30px; line-height:1.2; }}
h2 {{ font-size:14px; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); margin:30px 0 8px; }}
.badges {{ display:flex; flex-wrap:wrap; gap:6px; }}
.badge {{ font-size:13px; padding:2px 9px; border-radius:6px; background:var(--chip); }}
.badge.stop {{ background:var(--stop-bg); color:var(--stop-ink); }}
.shape {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:13.5px; background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:12px 14px; }}
.diagram {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:12px; overflow:auto; margin-top:10px; }}
code {{ background:var(--chip); padding:1px 5px; border-radius:4px; font-size:14px; }}
li {{ margin:5px 0; }}
.cta {{ display:inline-block; margin-top:6px; padding:8px 14px; border-radius:8px; background:var(--accent); color:#fff; text-decoration:none; }}
footer {{ color:var(--muted); font-size:13px; text-align:center; padding:24px; }}
</style>
</head>
<body>
<header><a class="brand" href="../../">Agent Workflow Atlas</a><a href="../../#{id}">Open in the catalog</a><a href="{source}">Source file</a></header>
<main>
<div class="place">{id} · {place}</div>
<h1>{name}</h1>
<div class="badges">{badges}</div>
<h2>Shape</h2>
<div class="shape">{shape}</div>
<pre class="mermaid diagram">{mermaid}</pre>
{kit}
{intro}
<h2>Steps</h2>
{steps}
<h2>Public runs</h2>
{runs}
<h2 id="sources">Sources</h2>
{sources}
<p class="place">Last verified {verified}. Spotted something outdated? <a href="{issues}">Report it</a>.</p>
</main>
<footer>Agent Workflow Atlas · content CC BY 4.0 · <a href="../../catalog.json">catalog.json</a> · <a href="../../catalog.csv">catalog.csv</a></footer>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
mermaid.initialize({{ startOnLoad: true, securityLevel: "strict", theme: matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "default" }});
</script>
</body>
</html>
"""


def page(w, repo, site_url):
    link = resolver(repo, w["path"])
    canonical = f"{site_url}/w/{w['id']}/" if site_url else f"w/{w['id']}/"
    badges = [f'<span class="badge">Public runs: {esc(w["coverage"] or "not graded")}</span>',
              f'<span class="badge">{esc(w["autonomy"])}</span>',
              f'<span class="badge">evidence {esc(w["evidence"])}</span>',
              f'<span class="badge">{esc(w["status"])}</span>']
    badges += [f'<span class="badge stop">🛑 {esc(c)}</span>' for c in w["checkpoints"]]
    kit = ""
    if w["kit"]:
        kit = f'<p><a class="cta" href="{esc(link("variants/claude-code.md"))}">Run it: Claude Code kit</a></p>'
    return PAGE.format(
        title=esc(f"{w['name']} · Agent Workflow Atlas"),
        desc=esc(description(w)),
        canonical=esc(canonical),
        image=esc(f"{site_url}/og.png" if site_url else "../../og.png"),
        id=esc(w["id"]),
        place=esc(f"{w['kingdomName']} › {w['phylumName']} › {w['class']}" + (" (unplaced)" if w["unplaced"] else "")),
        name=esc(w["name"]),
        badges="".join(badges),
        shape=esc(w["shape"]),
        mermaid=esc(w["mermaid"]),
        kit=kit,
        intro=markdown(w["intro"], link),
        steps=markdown(w["steps"], link),
        runs=markdown(w["publicRuns"], link),
        sources=markdown(w["sources"], link, sources=True),
        verified=esc(w["lastVerified"]),
        source=esc(f"{repo}/blob/main/{w['path']}/README.md" if repo else f"../../../{w['path']}/README.md"),
        issues=esc(f"{repo}/issues/new?template=correction.yml" if repo else "#"),
    )


def export_rows(workflows, repo, site_url):
    rows = []
    for w in workflows:
        row = {k: w.get(k) for k in CSV_FIELDS if k in w}
        row["url"] = f"{site_url}/w/{w['id']}/" if site_url else f"w/{w['id']}/"
        row["source"] = f"{repo}/blob/main/{w['path']}/README.md" if repo else w["path"] + "/README.md"
        rows.append(row)
    return rows


def to_csv(rows):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_FIELDS, extrasaction="ignore")
    writer.writeheader()
    for r in rows:
        writer.writerow({k: "; ".join(v) if isinstance(v, list) else v for k, v in r.items()})
    return buf.getvalue()


def write_all(out, data, site_url):
    repo, workflows = data["repo"], data["workflows"]
    for w in workflows:
        d = out / "w" / w["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(w, repo, site_url))
    export = [dict(w, **r) for w, r in zip(workflows, export_rows(workflows, repo, site_url))]
    for w in export:
        w.pop("mermaid", None)
    (out / "catalog.json").write_text(json.dumps({"taxonomy": data["taxonomy"], "workflows": export}, ensure_ascii=False, indent=1))
    (out / "catalog.csv").write_text(to_csv(export))
    if site_url:
        urls = [f"{site_url}/"] + [f"{site_url}/w/{w['id']}/" for w in workflows]
        (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                         + "".join(f"  <url><loc>{esc(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
        (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n")
