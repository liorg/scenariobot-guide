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

ACTION_TYPES = {"highlight", "navigate-highlight"}

chapters, actions, problems = {}, {}, []
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
        "actions": [a["id"] for a in fm.get("actions", [])],
    }

    for a in fm.get("actions", []):
        sc, tgt = a["screen"], a["target"]
        if a["type"] not in ACTION_TYPES:
            problems.append(f"{md.name}/{a['id']}: type {a['type']} is not one of {sorted(ACTION_TYPES)}")
        if sc not in screens:
            problems.append(f"{md.name}/{a['id']}: unknown screen {sc}")
        elif tgt not in screens[sc]["elements"]:
            problems.append(f"{md.name}/{a['id']}: {sc} has no element {tgt}")
        if a["id"] in actions:
            problems.append(f"{md.name}/{a['id']}: action id already used in {actions[a['id']]['chapter']}")
        actions[a["id"]] = {
            "description": a["description"],
            "chapter": fm["id"],
            "screen": sc,
            "target": tgt,
            "type": a["type"],
            "url": screens[sc]["url"] if sc in screens else None,
            "element": screens[sc]["elements"][tgt] if sc in screens and tgt in screens[sc]["elements"] else None,
        }

for cid, c in chapters.items():
    for r in c["related"]:
        if r not in chapters:
            problems.append(f"{cid}: related -> {r} does not exist")

(GUIDE / "index.json").write_text(json.dumps({
    "guide": "ScenarioBot user guide",
    "site": "https://liorg.github.io/scenariobot-guide",
    "language": "en",
    "language_note": (
        "This guide is written in English only. The product interface is not — it is "
        "translated into every enabled language and each user picks their own, so a "
        "reader may be looking at a screen in Hebrew, Arabic, Russian, German or "
        "Polish while reading this. Answer in the reader's language; quote UI labels "
        "as they appear here and expect the reader to see the translated wording. "
        "Chapter 22-languages covers how the interface language is chosen, and why "
        "the platform's own messages to a number follow that number's dial code "
        "rather than the reader's language."
    ),
    "note": "One entry per chapter. Element-level ids are in img/index.json.",
    "action_types": {
        "highlight": "The screen's URL contains ids that cannot be typed — "
                     "the user has to already be on it. Point at the element.",
        "navigate-highlight": "Open the screen's url, then point at the element.",
    },
    "chapters": chapters,
    "actions": actions,
}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print(f"index.json: {len(chapters)} chapters, {len(actions)} actions, "
      f"{sum(len(c['keywords']) for c in chapters.values())} keywords, "
      f"{sum(len(c['sections']) for c in chapters.values())} sections")
if problems:
    print("PROBLEMS:"); [print(" ", p) for p in problems]; sys.exit(1)
