#!/usr/bin/env python3
"""Builds guide/index.json from the chapters' YAML frontmatter.

Run it after editing any chapter's frontmatter or headings:
    python3 guide/_build_index.py

Screen element ids live in guide/img/index.json, written by
guide/img/_generate_screens.py. These two files are the whole machine-readable
surface of the guide.
"""
import json, pathlib, re, sys

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

GUIDE = pathlib.Path(__file__).resolve().parent
screens = json.loads((GUIDE / "img/index.json").read_text())["screens"]

chapters, problems = {}, []
for md in sorted(GUIDE.glob("[0-9]*.md")):
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        problems.append(f"{md.name}: no frontmatter")
        continue
    fm = yaml.safe_load(text.split("---\n", 2)[1])
    sc = fm.get("screen")
    sc = sc if isinstance(sc, list) else ([sc] if sc else [])
    for s in sc:
        if s not in screens:
            problems.append(f"{md.name}: unknown screen {s}")
        elif screens[s]["chapter"] != fm["id"]:
            problems.append(f"{md.name}: {s} is filed under {screens[s]['chapter']}")
    if fm["id"] != md.stem:
        problems.append(f"{md.name}: id is {fm['id']}")

    chapters[fm["id"]] = {
        "title": fm["title"],
        "file": md.name,
        "html": md.stem + ".html",
        "url": fm.get("url"),
        "screens": sc,
        "two_fa": fm.get("two_fa"),
        "keywords": fm.get("keywords", []),
        "related": fm.get("related", []),
        "sections": re.findall(r"^## (.+)$", text, re.M),
    }

for cid, c in chapters.items():
    for r in c["related"]:
        if r not in chapters:
            problems.append(f"{cid}: related -> {r} does not exist")

(GUIDE / "index.json").write_text(json.dumps({
    "guide": "ScenarioBot user guide",
    "site": "https://liorg.github.io/scenariobot-guide",
    "note": "One entry per chapter. Element-level ids are in img/index.json.",
    "chapters": chapters,
}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print(f"index.json: {len(chapters)} chapters, "
      f"{sum(len(c['keywords']) for c in chapters.values())} keywords, "
      f"{sum(len(c['sections']) for c in chapters.values())} sections")
if problems:
    print("PROBLEMS:"); [print(" ", p) for p in problems]; sys.exit(1)
