"""Turn a shape line (TAXONOMY.md §6) into a Mermaid flowchart.

  →          next step
  (a ⟲ b)    a, then b; back to a until b passes
  each X: a  a, done for every X (drawn as a box labelled "each X")
  a | b      alternative paths after a routing step
  🛑 type    a human checkpoint (drawn red)
"""
import re


def split_top(text, sep):
    """Split on sep, ignoring separators inside parentheses."""
    parts, depth, buf, i = [], 0, "", 0
    while i < len(text):
        ch = text[i]
        depth += ch == "("
        depth -= ch == ")"
        if depth == 0 and text.startswith(sep, i):
            parts.append(buf.strip())
            buf, i = "", i + len(sep)
            continue
        buf += ch
        i += 1
    parts.append(buf.strip())
    return [p for p in parts if p]


def unwrap(text):
    """Drop one pair of parentheses that wraps the whole text."""
    if text.startswith("(") and text.endswith(")") and split_top(text[1:-1], "⟲") and _matched(text):
        return text[1:-1].strip()
    return text


def _matched(text):
    depth = 0
    for i, ch in enumerate(text):
        depth += ch == "("
        depth -= ch == ")"
        if depth == 0 and i < len(text) - 1:
            return False
    return True


def label(text):
    text = text.replace('"', "#quot;")
    return text if len(text) <= 60 else text[:57].rstrip() + "…"


class Graph:
    def __init__(self):
        # edges go after all nodes and boxes: an edge written inside a box pulls its nodes into it
        self.lines, self.edges, self.n = [], [], 0

    def next_id(self, prefix="n"):
        self.n += 1
        return f"{prefix}{self.n}"

    def node(self, text):
        nid = self.next_id()
        if "🛑" in text:
            self.lines.append(f'  {nid}{{{{"{label(text)}"}}}}:::stop')
        else:
            self.lines.append(f'  {nid}["{label(text)}"]')
        return nid

    def edge(self, a, b):
        self.edges.append(f"  {a} --> {b}")

    def back(self, a, b):
        self.edges.append(f"  {a} -.->|repeat| {b}")


def build(g, text, prev):
    """Add the steps in text after the nodes in prev; return the last nodes."""
    for seg in split_top(text, "→"):
        seg = unwrap(seg)
        loop = split_top(seg, "⟲")
        if len(loop) > 1:
            first = None
            for part in loop:
                before = g.n
                prev = build(g, unwrap(part), prev)
                first = first or f"n{before + 1}"
            for end in prev:
                g.back(end, first)
            continue
        each = re.match(r"^(each [^:()]+):\s*(.+)$", seg)
        if each:
            g.lines.append(f'  subgraph {g.next_id("s")}["{label(each.group(1))}"]')
            prev = build(g, each.group(2), prev)
            g.lines.append("  end")
            continue
        options = split_top(seg, "|")
        if len(options) > 1:
            outs = []
            for option in options:
                outs += build(g, option, prev)
            prev = outs
            continue
        nid = g.node(seg)
        for p in prev:
            g.edge(p, nid)
        prev = [nid]
    return prev


def to_mermaid(shape):
    g = Graph()
    build(g, shape, [])
    return "\n".join(["flowchart TD", *g.lines, *g.edges, "  classDef stop fill:#fde2e1,stroke:#b42318,color:#7a1610"])


def to_route(shape):
    """Flatten a shape line into the marks of a route strip: one per top-level step.

    Each mark is {"k": kind, "t": text}, kind being step, loop (a ⟲ group), each (done for
    every item), alt (a routing fork) or stop (a 🛑 checkpoint, with "cp" set to its type).
    """
    marks = []
    for seg in split_top(shape, "→"):
        text = unwrap(seg)
        cp = re.search(r"🛑 ([a-z-]+)", text)
        if cp:
            marks.append({"k": "stop", "t": text.replace("🛑", "").strip(), "cp": cp.group(1)})
        elif re.match(r"^each [^:()]+:", text):
            marks.append({"k": "each", "t": text})
        elif len(split_top(text, "⟲")) > 1:
            marks.append({"k": "loop", "t": text})
        elif len(split_top(text, "|")) > 1:
            marks.append({"k": "alt", "t": text})
        else:
            marks.append({"k": "step", "t": text})
    return marks
