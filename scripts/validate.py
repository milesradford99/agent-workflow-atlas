"""Check every workflow record against the rules in TAXONOMY.md.

Usage: python scripts/validate.py
Exits 1 and lists every problem if any record breaks a rule.
"""
import re
import sys

from catalog import ROOT, WORKFLOWS, load_taxonomy, read_front_matter, species_files

REQUIRED = [
    "id", "name", "kingdom", "phylum", "class", "deliverable", "shape", "autonomy",
    "checkpoints", "patterns", "variants", "evidence", "status", "reference_example",
    "last_verified",
]
ID_RE = re.compile(r"^AWF-\d{4}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def check_species(path, fm, tax, errors):
    rel = path.relative_to(ROOT)

    def err(msg):
        errors.append(f"{rel}: {msg}")

    missing = [f for f in REQUIRED if f not in fm]
    if missing:
        err(f"missing field(s): {', '.join(missing)}")
        return

    if not ID_RE.match(str(fm["id"])):
        err(f"id `{fm['id']}` must look like AWF-0042")

    slug = path.parent.name
    if not SLUG_RE.match(slug):
        err(f"folder name `{slug}` must be lowercase words joined by hyphens")

    # rule 2: placement matches the folder and taxonomy.yaml
    unplaced = path.parts[-3] == "unplaced"
    if unplaced:
        if fm["status"] == "accepted":
            err("unplaced workflows can't be `accepted`; place them first")
    else:
        k, p, c = path.parts[-5:-2]
        if (fm["kingdom"], fm["phylum"], fm["class"]) != (k, p, c):
            err(f"front matter says {fm['kingdom']}/{fm['phylum']}/{fm['class']} but the folder is {k}/{p}/{c}")
        kingdom = tax["kingdoms"].get(k)
        if kingdom is None:
            err(f"unknown kingdom `{k}`")
        elif p not in kingdom["phyla"]:
            err(f"unknown phylum `{p}` in kingdom {k}")
        elif c not in kingdom["phyla"][p]["classes"]:
            err(f"unknown class `{c}` in {k}/{p} (allowed: {', '.join(kingdom['phyla'][p]['classes'])})")

    # traits use allowed values
    traits = tax["traits"]
    for field in ["autonomy", "evidence", "status"]:
        if fm[field] not in traits[field]:
            err(f"`{field}: {fm[field]}` is not one of {traits[field]}")
    for field in ["checkpoints", "patterns"]:
        if not isinstance(fm[field], list) or not fm[field]:
            err(f"`{field}` must be a non-empty list")
            continue
        for v in fm[field]:
            if v not in traits[field]:
                err(f"`{field}` value `{v}` is not one of {traits[field]}")
    risk = (fm.get("tags") or {}).get("risk")
    if risk is not None and risk not in traits["risk"]:
        err(f"`tags.risk: {risk}` is not one of {traits['risk']}")

    # the shape line and the checkpoint list agree
    in_shape = set(re.findall(r"🛑 ([a-z-]+)", str(fm["shape"])))
    if isinstance(fm["checkpoints"], list) and in_shape != set(fm["checkpoints"]):
        err(f"`checkpoints` {sorted(fm['checkpoints'])} don't match the 🛑 checkpoints in `shape` {sorted(in_shape)}")

    # variants: listed slugs, and any notes file in variants/ is listed
    variants = fm["variants"] or []
    for v in variants:
        if not SLUG_RE.match(str(v)):
            err(f"variant `{v}` must be lowercase words joined by hyphens")
    vdir = path.parent / "variants"
    if vdir.is_dir():
        for f in vdir.glob("*.md"):
            if f.stem not in variants:
                err(f"variants/{f.name} has no matching entry in `variants`")

    # rule 3: accepted needs a reference example; every example has a README
    ref = fm["reference_example"]
    if ref is not None and not (path.parent / ref / "README.md").is_file():
        err(f"reference_example `{ref}` has no README.md")
    if fm["status"] == "accepted" and ref is None:
        err("`accepted` needs a reference_example (rule 3); use `draft` until one exists")
    edir = path.parent / "examples"
    if edir.is_dir():
        for ex in edir.iterdir():
            if ex.is_dir() and not (ex / "README.md").is_file():
                err(f"examples/{ex.name}/ has no README.md")
            if ex.is_dir() and not re.match(r"^\d{4}-\d{2}-[a-z0-9-]+$", ex.name):
                err(f"examples/{ex.name}/ must be named YYYY-MM-short-name")

    # freshness: last_verified is a month, so scripts/freshness.py can age it
    if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", str(fm["last_verified"])):
        err(f"`last_verified: {fm['last_verified']}` must be a month like 2026-11")

    # rule 6: merged points somewhere
    if fm["status"] == "merged" and not fm.get("merged_into"):
        err("`merged` needs `merged_into`")


def main():
    tax = load_taxonomy()
    errors, ids = [], {}
    records = []

    for path in species_files():
        fm, problem = read_front_matter(path)
        if problem:
            errors.append(f"{path.relative_to(ROOT)}: {problem}")
            continue
        check_species(path, fm, tax, errors)
        records.append((path, fm))
        if "id" in fm:
            ids.setdefault(fm["id"], []).append(path.relative_to(ROOT))

    # rule 3: IDs are unique
    for i, paths in ids.items():
        if len(paths) > 1:
            errors.append(f"id {i} is used by {len(paths)} workflows: {', '.join(map(str, paths))}")

    # links between records point at real IDs
    for path, fm in records:
        rel = path.relative_to(ROOT)
        for target in fm.get("inputs_from") or []:
            if target not in ids:
                errors.append(f"{rel}: inputs_from `{target}` is not a known id")
        target = fm.get("merged_into")
        if target and target not in ids:
            errors.append(f"{rel}: merged_into `{target}` is not a known id")

    # stray README files at the wrong depth would be silently skipped otherwise
    for readme in WORKFLOWS.rglob("README.md"):
        depth = len(readme.relative_to(WORKFLOWS).parts)
        is_example = "examples" in readme.parts or "variants" in readme.parts
        if readme.parent in (WORKFLOWS, WORKFLOWS / "unplaced") or is_example:
            continue
        if readme.parts[-3] == "unplaced" or depth == 5:
            continue
        errors.append(f"{readme.relative_to(ROOT)}: workflows go at workflows/<KINGDOM>/<PHYLUM>/<CLASS>/<name>/ or workflows/unplaced/<name>/")

    numbers = [int(i[4:]) for i in ids if ID_RE.match(str(i))]
    next_id = f"AWF-{(max(numbers) + 1 if numbers else 1):04d}"

    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"OK: {len(records)} workflows. Next free id: {next_id}")


if __name__ == "__main__":
    main()
