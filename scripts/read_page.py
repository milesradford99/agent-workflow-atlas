"""Print a public web page as plain text, for reading an entry's sources where a fetch tool is not available.

Usage: python scripts/read_page.py URL [max_chars]
"""
import html, re, subprocess, sys
url = sys.argv[1]; limit = int(sys.argv[2]) if len(sys.argv) > 2 else 12000
r = subprocess.run(["curl", "-sSL", "-m", "40", "-w", "\n__HTTP__%{http_code}", url], capture_output=True)
raw = r.stdout.decode("utf-8", "replace")
body, _, code = raw.rpartition("\n__HTTP__")
if r.returncode or not code.startswith("2"):
    sys.exit(f"FAILED: http {code or '-'} (site refused or unreachable); note it and carry on")
body = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", body)
body = re.sub(r"(?i)<(br|/p|/div|/li|/h\d|/tr)\s*/?>", "\n", body)
text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", body))
text = re.sub(r"[ \t\r\f\v]+", " ", text); text = re.sub(r"\n\s*\n+", "\n", text).strip()
print(f"[http {code}, {len(text)} chars]"); print(text[:limit])
