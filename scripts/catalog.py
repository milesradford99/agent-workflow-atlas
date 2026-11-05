"""Shared loading for validate.py and build_index.py."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / "workflows"


def load_taxonomy():
    return yaml.safe_load((ROOT / "taxonomy.yaml").read_text())


def read_front_matter(path):
    """Return (front matter dict, error string or None)."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return None, "missing front matter (file must start with ---)"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "front matter is not closed with ---"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as e:
        return None, f"front matter is not valid YAML: {e}"
    if not isinstance(data, dict):
        return None, "front matter must be a mapping"
    return data, None


def species_files():
    """Every species README: workflows/<K>/<P>/<C>/<slug>/README.md and workflows/unplaced/<slug>/README.md."""
    placed = sorted(WORKFLOWS.glob("*/*/*/*/README.md"))
    unplaced = sorted((WORKFLOWS / "unplaced").glob("*/README.md"))
    return [p for p in placed if p.parts[-5] != "unplaced"] + unplaced
