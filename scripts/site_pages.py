"""Static outputs for the catalog site: one page per workflow in each language, data exports
and a sitemap.

The interactive page (site_template.html) is for browsing. These files are for linking,
sharing and search engines: each workflow gets a plain HTML page at w/<ID>/ (English) and
w/<ID>/zh/ (Simplified Chinese), each with its own title, description and preview image.
"""
import csv
import html
import io
import json
import re

CSV_FIELDS = ["id", "name", "nameZh", "summary", "summaryZh", "kingdom", "phylum", "class", "deliverable",
              "autonomy", "checkpoints", "patterns", "variants", "evidence", "coverage", "runs", "risk",
              "region", "status", "lastVerified", "kit", "shape", "url", "source"]

UI = {
    "en": {
        "home": "All workflows", "open": "Open in the catalog", "source": "Source on GitHub",
        "kit": "Run it with the Claude Code kit", "route": "The route", "steps": "Steps", "runs": "Public runs",
        "sources": "Sources", "diagram": "Full diagram", "verified": "Last checked {v}.", "report": "Report something out of date",
        "note": "", "noteBehind": "", "noteMissing": "", "other": "中文", "otherHref": "zh/", "stops": "{n} human stops", "stop1": "1 human stop",
        "cov": {"Strong": "Strong evidence", "Partial": "Partial evidence", "Weak": "Weak evidence", "None found": "No public run"},
        "auto": {"assist": "Assist: a person reviews each piece", "checkpointed": "Checkpointed: runs freely between fixed approvals", "sampled": "Sampled: runs end to end while people audit samples"},
        "cp": {"plan": "approve the plan", "action": "approve an action", "review": "review the draft", "sample": "check a sample", "sign-off": "sign off", "handoff": "take over a hard case"},
        "pat": {"chain": "Chain", "route": "Router", "parallel": "Parallel", "orch-workers": "Orchestrator and workers", "eval-opt": "Generate and critique", "auto-loop": "Autonomous loop", "role-crew": "Role crew", "computer-use": "Computer use"},
        "ev": {"A": "First-hand write-up", "B": "Vendor material", "C": "Community report"},
        "risk": {"low": "Low", "medium": "Medium", "high": "High (regulated)"},
        "setup": "Inputs and tools", "pattern": "Agent pattern", "evidence": "Sources", "riskLabel": "Risk", "checked": "Last checked",
        "tools": "Tools seen in practice", "theme": "Switch between light and dark",
        "delivers": "Delivers", "autonomy": "Autonomy", "desc": "{name}: a step-by-step AI agent workflow from {field}, with the human checkpoints, tools and sources. {summary}",
        "foot": "Agent Workflow Atlas. Content CC BY 4.0.",
    },
    "zh-CN": {
        "home": "全部工作流", "open": "在目录中打开", "source": "在 GitHub 查看源文件",
        "kit": "用 Claude Code 套件运行", "route": "路线", "steps": "步骤", "runs": "公开实例",
        "sources": "来源", "diagram": "完整流程图", "verified": "最近核对：{v}。", "report": "报告过时内容",
        "note": "来源保留原文标题；公开实例中引号内的原话保留原文，以便与出处逐字对应。",
        "noteBehind": "英文原文在这份译文之后有更新，内容请以英文版为准。", "noteMissing": "本页正文尚未翻译，以下为英文原文。", "other": "English", "otherHref": "../", "stops": "{n} 个人工节点", "stop1": "1 个人工节点",
        "cov": {"Strong": "证据充分", "Partial": "证据部分", "Weak": "证据薄弱", "None found": "暂无公开实例"},
        "auto": {"assist": "辅助：每一步都由人审阅", "checkpointed": "分段：在固定审批点之间自动运行", "sampled": "抽检：端到端运行，人抽查样本"},
        "cp": {"plan": "审批计划", "action": "审批操作", "review": "审阅草稿", "sample": "抽检样本", "sign-off": "签发", "handoff": "人工接手疑难"},
        "pat": {"chain": "链式", "route": "路由", "parallel": "并行", "orch-workers": "编排与子智能体", "eval-opt": "生成与评审", "auto-loop": "自主循环", "role-crew": "角色分工", "computer-use": "操作电脑"},
        "ev": {"A": "第一手记录", "B": "厂商材料", "C": "社区经验"},
        "risk": {"low": "低", "medium": "中", "high": "高（受监管）"},
        "setup": "输入与工具", "pattern": "智能体模式", "evidence": "来源类型", "riskLabel": "风险", "checked": "最近核对",
        "tools": "实践中用到的工具", "theme": "切换浅色或深色",
        "delivers": "交付物", "autonomy": "自主程度", "desc": "{name}：来自{field}的 AI 智能体工作流，逐步写明人工检查点、工具和出处。{summary}",
        "foot": "Agent Workflow Atlas · AI 智能体工作流图谱。内容采用 CC BY 4.0。",
    },
}


def esc(s):
    return html.escape(str(s), quote=True)


OCT = '<span class="oct" role="img" aria-label="human checkpoint"></span>'


def plain(text):
    """Escaped text, with each 🛑 drawn as the checkpoint mark."""
    return re.sub(r"🛑\s*", OCT, esc(text))


def inline(text, link, blank=False):
    """Markdown inline: code, citations, links, bold, italic, bare URLs."""
    ext = ' target="_blank" rel="noopener"' if blank else ""
    parts, last = [], 0
    for m in re.finditer(r"`([^`]+)`|\[\[(\d+)\]\]\(#sources\)|\[([^\]]+)\]\(([^)\s]+)\)|\*\*([^*]+)\*\*|(?<![\w*])\*([^*\n]+)\*|(https?://[^\s<)]+)", text):
        parts.append(plain(text[last:m.start()]))
        code, cite, label, url, bold, ital, bare = m.groups()
        if code is not None:
            parts.append(f"<code>{esc(code)}</code>")
        elif cite is not None:
            parts.append(f'<sup><a href="#src-{cite}">[{cite}]</a></sup>')
        elif label is not None:
            parts.append(f'<a href="{esc(link(url))}"{"" if url.startswith("#") else ext}>{inline(label, link, blank)}</a>')
        elif bold is not None:
            parts.append(f"<strong>{inline(bold, link, blank)}</strong>")
        elif ital is not None:
            parts.append(f"<em>{inline(ital, link, blank)}</em>")
        else:
            parts.append(f'<a href="{esc(bare)}"{ext}>{esc(bare)}</a>')
        last = m.end()
    parts.append(plain(text[last:]))
    return "".join(parts)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def markdown(text, link, sources=False, blank=False, cls=""):
    """Block Markdown: paragraphs, flat numbered or bulleted lists, and simple tables.

    A numbered item that holds a 🛑 gets class "stop", so checkpoints stand out in the steps.
    """
    out, kind = [], None
    lines, i = text.split("\n"), 0

    def close():
        nonlocal kind
        if kind:
            out.append(f"</{kind}>")
            kind = None

    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        if line.startswith("|") and i < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i].strip()):
            close()
            head, rows = cells(line), []
            i += 1
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            out.append('<div class="table"><table><thead><tr>' + "".join(f"<th>{inline(c, link, blank)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c, link, blank)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")
            continue
        ol, ul = re.match(r"^(\d+)\.\s+(.*)$", line), re.match(r"^[-*]\s+(.*)$", line)
        if ol or ul:
            tag = "ol" if ol else "ul"
            if kind != tag:
                close()
                out.append(f"<{tag}>")
                kind = tag
            attrs = ""
            if ol:
                attrs = f' value="{ol[1]}"' + (f' id="src-{ol[1]}"' if sources else "") + (' class="stop"' if "🛑" in ol[2] else "")
            out.append(f"<li{attrs}>{inline(ol[2] if ol else ul[1], link, blank)}</li>")
            continue
        close()
        if line.strip():
            out.append(f"<p>{inline(line, link, blank)}</p>")
    close()
    return f'<div class="prose{" " + cls if cls else ""}">' + "\n".join(out) + "</div>"


def resolver(repo, path, depth):
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
        return f"{repo}/blob/main/{target}" if repo else "../" * depth + "../" + target
    return link


def flow_html(w, ui):
    """The route written out in words: one chip per step, checkpoints in red."""
    items = []
    for m in w["route"]:
        if m["k"] == "stop":
            more = f': {esc(m["t"])}' if m["t"] and m["t"] != m["cp"] else ""
            items.append(f'<li class="stop"><span>{OCT}<span><b>{esc(ui["cp"][m["cp"]])}</b>{more}</span></span></li>')
        else:
            items.append(f'<li class="{m["k"]}"><span>{esc(m["t"])}</span></li>')
    return '<ol class="flow">' + "".join(items) + "</ol>"


BRAND = ('<svg width="30" height="16" viewBox="0 0 30 16" aria-hidden="true"><line x1="2" y1="8" x2="28" y2="8" stroke="var(--route-soft)" stroke-width="2"/>'
         '<circle cx="4" cy="8" r="3" fill="var(--route)"/><path d="M13 3.6h4l2.8 2.8v3.2L17 12.4h-4l-2.8-2.8V6.4z" fill="var(--stop)"/><circle cx="26" cy="8" r="3" fill="var(--route)"/></svg>')
THEME_ICON = '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.25" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.75a6.25 6.25 0 0 1 0 12.5z" fill="currentColor"/></svg>'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;700&display=swap">')
# runs before first paint, so a saved theme never flashes the other one
THEME_BOOT = '<script>try{var t=localStorage.getItem("awa-theme");if(t)document.documentElement.dataset.theme=t}catch(e){}</script>'


PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{href_en}">
<link rel="alternate" hreflang="zh-CN" href="{href_zh}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
{theme_boot}
{fonts}
<style>
{css}
.top {{ border-bottom: 1px solid var(--rule); background: var(--paper); }}
.top-in, main, footer {{ max-width: 840px; margin: 0 auto; padding-left: 22px; padding-right: 22px; }}
.top-in {{ display: flex; gap: 18px; align-items: center; padding-top: 12px; padding-bottom: 12px; flex-wrap: wrap; font-size: 14px; }}
.top-in a {{ color: var(--slate); text-decoration: none; }} .top-in a:hover {{ color: var(--ink); }}
.top-in .brand {{ display: flex; align-items: center; gap: 10px; color: var(--ink); font: 600 16px/1 var(--f-head); letter-spacing: -0.01em; margin-right: auto; }}
main {{ padding-top: 40px; padding-bottom: 70px; }}
main > .crumb {{ margin-bottom: 12px; }}
footer {{ border-top: 1px solid var(--rule); color: var(--slate); font-size: 13.5px; padding-top: 20px; padding-bottom: 30px; }}
</style>
</head>
<body>
<header class="top"><div class="top-in">
<a class="brand" href="{home}">{brand}Agent Workflow Atlas</a>
<a href="{home}">{t_home}</a><a href="{other_href}" hreflang="{other_lang}" lang="{other_lang}">{t_other}</a>
<button class="icon-btn" id="theme" aria-label="{t_theme}" title="{t_theme}">{theme_icon}</button>
</div></header>
<main>
<div class="crumb">{crumb}</div>
<h1 class="d-title">{name}</h1>{alt}
<p class="lede">{summary}</p>
<div class="facts"><span class="grade {grade}">{cov}</span><span class="stops">{oct}{stops}</span></div>
<div class="actions">{kit}<a class="btn" href="{app}">{t_open}</a><a class="btn" href="{source}">{t_source}</a></div>
<section class="d-sec"><h2>{t_route}</h2>
<div class="route-box">{route}</div>
<dl class="meta-grid"><div><dt>{t_delivers}</dt><dd>{deliverable}</dd></div><div><dt>{t_autonomy}</dt><dd>{autonomy}</dd></div><div><dt>{t_pattern}</dt><dd>{pattern}</dd></div><div><dt>{t_evidence}</dt><dd>{evidence}</dd></div><div><dt>{t_risk}</dt><dd>{risk}</dd></div><div><dt>{t_checked}</dt><dd>{checked}</dd></div>{tools}</dl>
</section>
{note}
<div lang="{body_lang}">
{intro}
<section class="d-sec"><h2>{t_steps}</h2>
{steps}</section>
<section class="d-sec"><h2>{t_runs}</h2>
{runs}</section>
</div>
<section class="d-sec"><h2 id="sources">{t_sources}</h2>
<div lang="en">{sources}</div></section>
<section class="d-sec"><h2>{t_diagram}</h2>
<div class="shape-line">{shape}</div>
<pre class="mermaid diagram" style="margin-top:12px">{mermaid}</pre></section>
<p class="crumb" style="margin-top:28px">{verified} <a href="{issues}">{t_report}</a></p>
</main>
<footer>{t_foot} <a href="{json}">catalog.json</a> · <a href="{csv}">catalog.csv</a></footer>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
const root = document.documentElement;
const dark = () => root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
mermaid.initialize({{ startOnLoad: true, securityLevel: "strict", theme: dark() ? "dark" : "neutral" }});
document.getElementById("theme").onclick = () => {{
  root.dataset.theme = dark() ? "light" : "dark";
  try {{ localStorage.setItem("awa-theme", root.dataset.theme); }} catch (e) {{}}
}};
</script>
</body>
</html>
"""


def page(w, data, site_url, css, lang):
    ui, labels, repo = UI[lang], data["labels"], data["repo"]
    zh = lang == "zh-CN"
    depth = 3 if zh else 2  # w/<ID>/ or w/<ID>/zh/
    up = "../" * depth
    link = resolver(repo, w["path"], depth)
    lab = lambda kind, code: labels[kind].get(code, {}).get(lang) or labels[kind].get(code, {}).get("en") or code
    name = w["nameZh"] if zh and w["nameZh"] else w["name"]
    summary = w["summaryZh"] if zh and w["summaryZh"] else w["summary"]
    base = f"{site_url}/w/{w['id']}/" if site_url else ""
    href_en, href_zh = (base, base + "zh/") if site_url else ("../" if zh else "./", "./" if zh else "zh/")
    # the Chinese page reads README.zh-CN.md; without one it falls back to the English text
    tr = w["zh"] if zh and w.get("zh") else None
    pick = lambda key: tr[key] if tr else w[key]
    note = ui["note"] if tr else ui["noteMissing"]
    if tr and tr["behind"]:
        note = ui["noteBehind"] + " " + note
    stops = sum(1 for m in w["route"] if m["k"] == "stop")
    kit = f'<a class="btn primary" href="{esc(link("variants/claude-code.md"))}">{esc(ui["kit"])}</a>' if w["kit"] else ""
    return PAGE.format(
        lang=lang, css=css, theme_boot=THEME_BOOT, fonts=FONTS, brand=BRAND, theme_icon=THEME_ICON, oct=OCT, t_theme=esc(ui["theme"]),
        title=esc(f"{name} · Agent Workflow Atlas"),
        desc=esc(ui["desc"].format(name=name, field=lab("phyla", w["phylum"]), summary=summary)),
        canonical=esc(href_zh if zh else href_en), href_en=esc(href_en), href_zh=esc(href_zh),
        image=esc(f"{site_url}/og.png" if site_url else up + "og.png"),
        home=esc(up + ("?lang=zh-CN" if zh else "")), t_home=esc(ui["home"]),
        other_href=esc(ui["otherHref"]), other_lang="en" if zh else "zh-CN", t_other=esc(ui["other"]),
        crumb=esc(f"{lab('kingdoms', w['kingdom'])} › {lab('phyla', w['phylum'])} › {lab('classes', w['class'])} · {w['id']}"),
        name=esc(name), alt=f'<div class="alt-name" lang="en">{esc(w["name"])}</div>' if zh and w["nameZh"] else "",
        summary=esc(summary), grade="g-" + (w["coverage"] or "").split(" ")[0], cov=esc(ui["cov"].get(w["coverage"], "")),
        stops=esc(ui["stop1"] if stops == 1 else ui["stops"].format(n=stops)), kit=kit,
        app=esc(up + ("?lang=zh-CN" if zh else "") + "#" + w["id"]), t_open=esc(ui["open"]),
        source=esc(f"{repo}/blob/main/{w['path']}/README.md" if repo else up + "../" + w["path"] + "/README.md"), t_source=esc(ui["source"]),
        t_route=esc(ui["route"]), route=flow_html(tr or w, ui),
        t_pattern=esc(ui["pattern"]), pattern=esc(", ".join(ui["pat"].get(p, p) for p in w["patterns"])),
        t_evidence=esc(ui["evidence"]), evidence=esc(ui["ev"].get(w["evidence"], w["evidence"])),
        t_risk=esc(ui["riskLabel"]), risk=esc(ui["risk"].get(w["risk"], w["risk"])),
        t_checked=esc(ui["checked"]), checked=esc(w["lastVerified"]),
        tools=f'<div class="wide"><dt>{esc(ui["tools"])}</dt><dd>{" ".join(f"<code>{esc(v)}</code>" for v in w["variants"])}</dd></div>' if w["variants"] else "",
        t_delivers=esc(ui["delivers"]), deliverable=esc(pick("deliverable")), t_autonomy=esc(ui["autonomy"]), autonomy=esc(ui["auto"][w["autonomy"]]),
        note=f'<p class="note" style="margin-top:28px">{esc(note)}</p>' if note else "", body_lang="zh-CN" if tr else "en",
        t_steps=esc(ui["steps"]), steps=markdown(pick("steps"), link),
        intro=f'<section class="d-sec"><h2>{esc(ui["setup"])}</h2>\n{markdown(pick("intro"), link)}</section>' if pick("intro") else "",
        t_runs=esc(ui["runs"]), runs=markdown(pick("publicRuns"), link, cls="runs"),
        t_sources=esc(ui["sources"]), sources=markdown(w["sources"], link, sources=True, cls="sources"),
        t_diagram=esc(ui["diagram"]), shape=esc(pick("shape")), mermaid=esc(pick("mermaid")),
        verified=esc(ui["verified"].format(v=w["lastVerified"])),
        issues=esc(f"{repo}/issues/new?template=correction.yml" if repo else "#"), t_report=esc(ui["report"]),
        t_foot=esc(ui["foot"]), json=esc(up + "catalog.json"), csv=esc(up + "catalog.csv"),
    )


def export_rows(workflows, repo, site_url):
    rows = []
    for w in workflows:
        row = {k: w[k] for k in CSV_FIELDS if k in w}
        row["url"] = f"{site_url}/w/{w['id']}/" if site_url else f"w/{w['id']}/"
        row["source"] = f"{repo}/blob/main/{w['path']}/README.md" if repo else w["path"] + "/README.md"
        rows.append(row)
    return rows


def to_csv(rows):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_FIELDS)
    writer.writeheader()
    for r in rows:
        writer.writerow({k: "; ".join(map(str, v)) if isinstance(v, list) else v for k, v in r.items()})
    return buf.getvalue()


def write_all(out, data, site_url, css):
    repo, workflows = data["repo"], data["workflows"]
    for w in workflows:
        d = out / "w" / w["id"]
        (d / "zh").mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(w, data, site_url, css, "en"))
        (d / "zh" / "index.html").write_text(page(w, data, site_url, css, "zh-CN"))
    rows = export_rows(workflows, repo, site_url)
    full = [dict({k: v for k, v in w.items() if k not in ("mermaid", "zh")}, zh={k: v for k, v in w["zh"].items() if k != "mermaid"} if w["zh"] else None, url=r["url"], source=r["source"]) for w, r in zip(workflows, rows)]
    (out / "catalog.json").write_text(json.dumps({"taxonomy": data["taxonomy"], "labels": data["labels"], "workflows": full}, ensure_ascii=False, indent=1))
    (out / "catalog.csv").write_text(to_csv(rows))
    if site_url:
        urls = [f"{site_url}/"] + [u for w in workflows for u in (f"{site_url}/w/{w['id']}/", f"{site_url}/w/{w['id']}/zh/")]
        (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                         + "".join(f"  <url><loc>{esc(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
        (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n")
