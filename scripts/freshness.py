"""Report workflows that are due for re-checking, and source links that no longer work.

Usage:
  python scripts/freshness.py                  stale entries only (no network)
  python scripts/freshness.py --links          also check every source and public-run link
  python scripts/freshness.py --as-of 2027-06  age entries against another month

Prints a Markdown report. The monthly freshness workflow posts it as an issue.
It also lists Chinese translations (README.zh-CN.md) that are behind the English.
Links are split into dead (404, 410, unknown domain), couldn't reach (timeouts and
other errors, often bot blocking) and refused (403, 429).
An entry is due when its `last_verified` month is STALE_AFTER months old or more.
"""
import argparse
import re
import socket
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date

import i18n
from catalog import ROOT, read_front_matter, species_files

STALE_AFTER = 6
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")
# Only these mean the page is gone: the server says so, or the domain no longer exists.
DEAD = {404, 410, "DNS"}
# Many sites refuse scripted requests; these codes mean "couldn't check", not "gone".
BLOCKED = {401, 403, 405, 406, 429, 451, 999}
# Anything else that fails (timeouts, dropped connections, TLS errors, 5xx) is "couldn't reach":
# often a site that is slow or rejects data-centre traffic, so it is listed apart and not called broken.
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; agent-workflow-atlas-freshness/1.0)"}


def months_old(verified, as_of):
    y, m = map(int, str(verified).split("-"))
    return (as_of[0] - y) * 12 + (as_of[1] - m)


def check(url):
    """Try the link as written, then without trailing punctuation that may end a sentence."""
    first = fetch(url)
    trimmed = url.rstrip(".,;:")
    if trimmed != url and not (isinstance(first[1], int) and first[1] < 400):
        return url, fetch(trimmed)[1]
    return first


def fetch(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 404, 405, 501):
                continue
            return url, e.code
        except Exception as e:  # DNS, TLS, timeout, dropped connection
            if method == "HEAD":
                continue
            reason = getattr(e, "reason", None)
            if isinstance(reason, socket.gaierror):
                return url, "DNS"
            return url, type(reason).__name__ if isinstance(reason, BaseException) else type(e).__name__
    return url, "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--links", action="store_true")
    ap.add_argument("--as-of", help="YYYY-MM (default: this month)")
    args = ap.parse_args()
    today = date.today()
    as_of = tuple(map(int, args.as_of.split("-"))) if args.as_of else (today.year, today.month)

    stale, urls, zh_behind = [], {}, []
    for path in species_files():
        fm, problem = read_front_matter(path)
        if problem:
            sys.exit(f"{path.relative_to(ROOT)}: {problem} (run scripts/validate.py)")
        if fm["status"] in ("merged", "retired"):
            continue
        rel = path.parent.relative_to(ROOT).as_posix()
        age = months_old(fm["last_verified"], as_of)
        if age >= STALE_AFTER:
            stale.append((age, fm["id"], fm["name"], rel, fm["last_verified"]))
        zh_errors, late = i18n.problems(path, fm)
        if zh_errors or late:
            zh_behind.append((fm["id"], fm["name"], rel, "missing or broken" if zh_errors else "behind the English"))
        for url in URL_RE.findall(path.read_text()):
            urls.setdefault(url, set()).add(fm["id"])

    month = f"{as_of[0]}-{as_of[1]:02d}"
    out = [f"# Freshness report, {month}", ""]
    out += [f"## Due for re-checking ({len(stale)})", "",
            f"Entries last verified {STALE_AFTER} or more months ago. To re-check one, follow MAINTAINING.md.", ""]
    if stale:
        out += ["| ID | Workflow | Last verified |", "|---|---|---|"]
        out += [f"| {i} | [{n}]({p}/) | {v} |" for _, i, n, p, v in sorted(stale, reverse=True)]
    else:
        out.append("None.")
    out.append("")
    out += [f"## Chinese translation to update ({len(zh_behind)})", "",
            "README.zh-CN.md no longer matches the English README. Update it and run `python scripts/i18n.py stamp <ID>` (i18n/TRANSLATING.md).", ""]
    if zh_behind:
        out += ["| ID | Workflow | State |", "|---|---|---|"] + [f"| {i} | [{n}]({p}/) | {s} |" for i, n, p, s in zh_behind]
    else:
        out.append("None.")
    out.append("")

    if args.links:
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(check, sorted(urls)))
        ok = lambda s: isinstance(s, int) and s < 400
        dead = [(u, s) for u, s in results if s in DEAD]
        blocked = [(u, s) for u, s in results if s in BLOCKED]
        unreachable = [(u, s) for u, s in results if not ok(s) and s not in DEAD and s not in BLOCKED]
        table = lambda rows: ["| Link | Result | Used by |", "|---|---|---|"] + [f"| {u} | {s} | {', '.join(sorted(urls[u]))} |" for u, s in rows]
        out += [f"## Dead links ({len(dead)} of {len(results)})", "",
                "Pages that return 404 or 410, or whose domain no longer resolves. Replace each with an archived copy or a newer source.", ""]
        out += table(dead) if dead else ["None."]
        out += ["", f"## Couldn't reach ({len(unreachable)})", "",
                "Timeouts, dropped connections and server errors from the checker. These are usually slow sites or sites that block automated traffic; check one by hand only if it shows up here several months in a row.", ""]
        if unreachable:
            out += ["<details><summary>Show links</summary>", ""] + table(unreachable) + ["", "</details>"]
        else:
            out.append("None.")
        out += ["", f"{len(blocked)} more links refused the automated check (403, 429 and similar) and need a look by hand only if a reader reports them.", ""]

    print("\n".join(out))


if __name__ == "__main__":
    main()
