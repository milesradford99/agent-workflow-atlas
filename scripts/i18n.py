"""Simplified Chinese translations of workflow entries.

Each workflow folder holds a README.zh-CN.md next to its README.md. It translates the
whole entry except the sources: name, summary, deliverable, shape line, the intro,
the steps and the public-run descriptions. i18n/TRANSLATING.md is the style guide.

The file records `source_hash`, a hash of the English README it was translated from.
When the English changes, the hash no longer matches and the translation is "behind":
validate.py warns, the freshness report lists it, and the Chinese page says so.
A missing translation, or one whose structure doesn't match the English (steps,
checkpoints, citations, links, quoted numbers, shape), is an error.

Usage:
  python scripts/i18n.py status               list missing, behind and broken translations
  python scripts/i18n.py check AWF-0001 ...   check these translations, print every problem
  python scripts/i18n.py stamp AWF-0001 ...   record the current English hash (after translating)
  python scripts/i18n.py scaffold AWF-0001    write a README.zh-CN.md to translate, with source_hash: TODO
"""
import hashlib
import re
import sys
from pathlib import Path

from catalog import ROOT, read_front_matter, species_files
from shapes import to_route

ZH_NAME = "README.zh-CN.md"
# 🛑 checkpoint labels in steps: English `🛑 **Review**` becomes `🛑 **审阅**`
CP_ZH = {"plan": "计划", "action": "操作", "review": "审阅", "sample": "抽检", "sign-off": "签发", "handoff": "接手"}
H_STEPS, H_RUNS = "## 步骤", "## 公开实例"
FIELDS = ("id", "name", "summary", "deliverable", "shape", "source_hash")
DIAGRAM_RE = re.compile(r"\n*<!-- shape diagram:.*?<!-- end shape diagram -->\n*", re.S)
CITE_RE = re.compile(r"\[\[(\d+)\]\]\(#sources\)")
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")
QUOTE_RE = re.compile(r'"([^"\n]+)"')
NUM_RE = re.compile(r"(?<![\w.])\d[\d,.]*%?")


def english_hash(readme):
    """Hash of the English README, ignoring the generated diagram."""
    text = DIAGRAM_RE.sub("\n\n", Path(readme).read_text())
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def body(text):
    return text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text[4:] else text


def section(text, heading):
    m = re.search(rf"^{re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def intro(text):
    """Everything between the title and the first ## heading, minus what the page draws itself:
    the badge line (place, autonomy, status), the shape and kit lines, and the diagram."""
    m = re.search(r"^# .*?\n(.*?)(?=^## |\Z)", DIAGRAM_RE.sub("\n\n", text), re.M | re.S)
    lines = (m.group(1) if m else "").strip().split("\n")
    lines = [ln for ln in lines if not ln.startswith(("**Shape:**", "**Agent kit:**", "**Traits:**", "**路线：**"))]
    if lines and lines[0].startswith("`"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def parts(readme):
    """The pieces of an English README that a translation must mirror."""
    text = body(readme.read_text())
    return {"intro": intro(text), "steps": section(text, "## Steps"), "runs": section(text, "## Public runs")}


def zh_parts(path):
    text = body(path.read_text())
    return {"intro": intro(text), "steps": section(text, H_STEPS), "runs": section(text, H_RUNS)}


def shape_marks(shape):
    route = to_route(shape)
    return [m["k"] for m in route], [m.get("cp") for m in route if m["k"] == "stop"]


def count_ops(shape):
    return {op: shape.count(op) for op in ("→", "⟲", "|", "🛑")}


def problems(readme, fm, allow_todo=False):
    """Errors for one workflow's translation, plus whether it is behind the English.

    allow_todo checks the structure of a file still marked `source_hash: TODO`."""
    zh_path = readme.parent / ZH_NAME
    if not zh_path.is_file():
        return [f"missing {ZH_NAME}"], False
    zfm, problem = read_front_matter(zh_path)
    if problem:
        return [f"{ZH_NAME}: {problem}"], False
    errs = []
    for key in FIELDS:
        if not str(zfm.get(key) or "").strip():
            errs.append(f"{ZH_NAME}: `{key}` is empty")
    if zfm.get("id") != fm["id"]:
        errs.append(f"{ZH_NAME}: id `{zfm.get('id')}` should be `{fm['id']}`")
    if str(zfm.get("source_hash")) == "TODO" and not allow_todo:
        errs.append(f"{ZH_NAME}: not translated yet (source_hash: TODO)")
    if len(str(zfm.get("summary") or "")) > 120:
        errs.append(f"{ZH_NAME}: summary is longer than 120 characters")
    if errs:
        return errs, False

    # shape: same steps, kinds, checkpoints and operators as the English
    en_kinds, en_cps = shape_marks(fm["shape"])
    zh_kinds, zh_cps = shape_marks(str(zfm["shape"]))
    if en_cps != zh_cps:
        errs.append(f"{ZH_NAME}: shape checkpoints {zh_cps} should be {en_cps} (keep `🛑 <type>` in English)")
    elif en_kinds != zh_kinds:
        errs.append(f"{ZH_NAME}: shape steps {zh_kinds} don't line up with the English {en_kinds}")
    if count_ops(fm["shape"]) != count_ops(str(zfm["shape"])):
        errs.append(f"{ZH_NAME}: shape uses {count_ops(str(zfm['shape']))} symbols, the English {count_ops(fm['shape'])}")

    en, zh = parts(readme), zh_parts(zh_path)
    if en["steps"] and not zh["steps"]:
        errs.append(f"{ZH_NAME}: needs a `{H_STEPS}` section")
    if en["runs"] and not zh["runs"]:
        errs.append(f"{ZH_NAME}: needs a `{H_RUNS}` section")
    n_en = len(re.findall(r"^\d+\. ", en["steps"], re.M))
    n_zh = len(re.findall(r"^\d+\. ", zh["steps"], re.M))
    if n_en != n_zh:
        errs.append(f"{ZH_NAME}: {n_zh} numbered steps, the English has {n_en}")
    for cp, word in CP_ZH.items():
        a, b = en["steps"].count(f"🛑 **{cp.capitalize()}"), zh["steps"].count(f"🛑 **{word}")
        if a != b:
            errs.append(f"{ZH_NAME}: {b}× `🛑 **{word}**` in steps, the English has {a}× `🛑 **{cp.capitalize()}**`")
    n_en = len(re.findall(r"^- \[", en["runs"], re.M))
    n_zh = len(re.findall(r"^- \[", zh["runs"], re.M))
    if n_en != n_zh:
        errs.append(f"{ZH_NAME}: {n_zh} public runs, the English has {n_en}")

    # still English? (a scaffold matches the English structure trivially)
    for key, label in (("steps", H_STEPS), ("intro", "intro")):
        text = re.sub(r"`[^`]*`|\[[^\]]*\]\([^)]*\)|https?://\S+", "", zh[key])
        letters = re.findall(r"[A-Za-z\u4e00-\u9fff]", text)
        cjk = sum(1 for ch in letters if ch >= "\u4e00")
        if letters and cjk / len(letters) < 0.3:
            errs.append(f"{ZH_NAME}: the {label} section is still mostly English")
    en_all, zh_all = "\n".join(en.values()), "\n".join(zh.values())
    missing = sorted(set(CITE_RE.findall(en_all)) - set(CITE_RE.findall(zh_all)), key=int)
    if missing:
        errs.append(f"{ZH_NAME}: citations missing: " + ", ".join(f"[[{n}]]" for n in missing))
    zh_urls = set(URL_RE.findall(zh_all))
    for url in sorted(set(URL_RE.findall(en_all))):
        if url not in zh_urls:
            errs.append(f"{ZH_NAME}: link missing: {url}")
    for q in QUOTE_RE.findall(en["runs"]):
        if len(q) >= 3 and q not in zh["runs"]:
            errs.append(f'{ZH_NAME}: public-run quote must stay verbatim: "{q[:60]}"')
    zh_nums = set(NUM_RE.findall(zh_all))
    norm = lambda nums: {n.rstrip(".,%") for n in nums} - {""}  # "40 percent" may become 40%
    lost = sorted(norm(NUM_RE.findall(en["intro"] + en["steps"])) - norm(zh_nums))
    if lost:
        errs.append(f"{ZH_NAME}: numbers missing from intro or steps (keep Arabic numerals): {', '.join(lost[:8])}")
    behind = str(zfm.get("source_hash")) != english_hash(readme)
    return errs, behind


def load(readme):
    """The translation as the site needs it, or None. Until `source_hash` is set (not TODO),
    only the name and summary are used: the rest of a scaffold is still English."""
    zh_path = readme.parent / ZH_NAME
    if not zh_path.is_file():
        return None
    zfm, problem = read_front_matter(zh_path)
    if problem:
        return None
    p = zh_parts(zh_path)
    translated = str(zfm.get("source_hash")) != "TODO"
    return {"translated": translated,
        "name": str(zfm.get("name") or ""), "summary": str(zfm.get("summary") or ""),
        "deliverable": str(zfm.get("deliverable") or ""), "shape": str(zfm.get("shape") or ""),
        "intro": p["intro"], "steps": p["steps"], "runs": p["runs"],
        "behind": str(zfm.get("source_hash")) != english_hash(readme),
    }


def by_id():
    out = {}
    for readme in species_files():
        fm, problem = read_front_matter(readme)
        if not problem:
            out[fm["id"]] = (readme, fm)
    return out


def scaffold(readme, fm):
    """A file to translate: the English text in the right places, hash left as TODO."""
    en = parts(readme)
    steps = en["steps"]
    for cp, word in CP_ZH.items():
        steps = steps.replace(f"🛑 **{cp.capitalize()}**", f"🛑 **{word}**")
    q = lambda s: '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'
    lines = ["---", f"id: {fm['id']}", f"name: {fm['name']}", f"summary: {q(fm['summary'])}",
             f"deliverable: {fm['deliverable']}", f"shape: {q(fm['shape'])}", "source_hash: TODO", "---", "",
             f"# {fm['name']}", "", en["intro"], "", H_STEPS, "", steps]
    if en["runs"]:
        lines += ["", H_RUNS, "", en["runs"]]
    return "\n".join(lines) + "\n"


def main(argv):
    if not argv or argv[0] not in ("status", "check", "stamp", "scaffold"):
        print(__doc__)
        return 2
    cmd, ids = argv[0], argv[1:]
    known = by_id()
    for i in ids:
        if i not in known:
            print(f"unknown id {i}")
            return 2
    if cmd == "status":
        missing, behind, broken = [], [], []
        for i, (readme, fm) in sorted(known.items()):
            errs, late = problems(readme, fm)
            if errs and errs[0].startswith("missing"):
                missing.append(i)
            elif errs:
                broken.append((i, errs))
            elif late:
                behind.append(i)
        print(f"{len(known)} workflows: {len(known) - len(missing) - len(broken) - len(behind)} up to date, "
              f"{len(behind)} behind the English, {len(broken)} with problems, {len(missing)} missing")
        for i in behind:
            print(f"  behind: {i}")
        for i, errs in broken:
            print(f"  problems: {i}: {errs[0]}" + (f" (+{len(errs) - 1} more)" if len(errs) > 1 else ""))
        if missing:
            print("  missing: " + " ".join(missing))
        return 1 if missing or broken else 0
    rc = 0
    for i in ids:
        readme, fm = known[i]
        zh_path = readme.parent / ZH_NAME
        if cmd == "scaffold":
            if zh_path.exists():
                print(f"{i}: {zh_path.relative_to(ROOT)} already exists")
                rc = 1
                continue
            zh_path.write_text(scaffold(readme, fm))
            print(f"{i}: wrote {zh_path.relative_to(ROOT)}")
        elif cmd == "check":
            errs, late = problems(readme, fm, allow_todo=True)
            todo = zh_path.is_file() and "\nsource_hash: TODO\n" in zh_path.read_text()
            late = late and not todo
            if todo and not errs:
                errs = [f"{ZH_NAME}: structure OK; run `stamp {i}` once the text is translated"]
            print(f"{i}: " + ("OK" + (" (behind the English)" if late else "") if not errs else f"{len(errs)} problem(s)"))
            for e in errs:
                print(f"  - {e}")
            rc |= bool(errs)
        elif cmd == "stamp":
            if not zh_path.is_file():
                print(f"{i}: no {ZH_NAME}")
                rc = 1
                continue
            text = zh_path.read_text()
            new = re.sub(r"^source_hash: .*$", f"source_hash: {english_hash(readme)}", text, count=1, flags=re.M)
            zh_path.write_text(new)
            errs, _ = problems(readme, fm)
            print(f"{i}: stamped" + ("" if not errs else f", but {len(errs)} problem(s):"))
            for e in errs:
                print(f"  - {e}")
            rc |= bool(errs)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
