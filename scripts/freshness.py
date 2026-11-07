"""Report workflows that are due for re-checking, and source links that no longer work.

Usage:
  python scripts/freshness.py                  stale entries only (no network)
  python scripts/freshness.py --links          also check every source and public-run link
  python scripts/freshness.py --as-of 2027-06  age entries against another month

Prints a Markdown report. The monthly freshness workflow posts it as an issue.
An entry is due when its `last_verified` month is STALE_AFTER months old or more.
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date

from catalog import ROOT, read_front_matter, species_files

STALE_AFTER = 6
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")
# Many sites refuse scripted requests; these codes mean "couldn't check", not "gone".
BLOCKED = {401, 403, 405, 406, 429, 451, 999}
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
        except Exception as e:  # DNS, TLS, timeout
            if method == "HEAD":
                continue
            return url, type(e).__name__
    return url, "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--links", action="store_true")
    ap.add_argument("--as-of", help="YYYY-MM (default: this month)")
    args = ap.parse_args()
    today = date.today()
    as_of = tuple(map(int, args.as_of.split("-"))) if args.as_of else (today.year, today.month)

    stale, urls = [], {}
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

    if args.links:
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(check, sorted(urls)))
        broken = [(u, s) for u, s in results if not (isinstance(s, int) and (s < 400 or s in BLOCKED))]
        blocked = [(u, s) for u, s in results if isinstance(s, int) and s in BLOCKED]
        out += [f"## Broken links ({len(broken)} of {len(results)})", ""]
        if broken:
            out += ["| Link | Result | Used by |", "|---|---|---|"]
            out += [f"| {u} | {s} | {', '.join(sorted(urls[u]))} |" for u, s in broken]
        else:
            out.append("None.")
        out += ["", f"{len(blocked)} links refused the automated check (403, 429 and similar) and need a look by hand only if a reader reports them.", ""]

    print("\n".join(out))


if __name__ == "__main__":
    main()
