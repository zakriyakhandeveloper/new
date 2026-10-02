# -*- coding: utf-8 -*-
"""Patch pass 2: restore the Aabad reference's field TYPES.

The reference defines culture, emotional_traits, hidden_personality_traits and
popularity_by_region as LISTS. Patch pass 1 wrote three of them as plain strings
and culture as a string; this restores list typing while keeping the same
explicit, evidence-honest content.

canonical_url is left as "" because that is exactly what the reference record
contains (both top-level and inside seo).
"""
import json
import pathlib

ROOT = pathlib.Path("/workspace/upgrade_v2/upgrading/names_upgraded/islamic")

CULTURE_BY_ORIGIN = {
    "Arabic": ["Arab"],
    "Persian": ["Persian"],
    "Sanskrit": ["Indian"],
    "Hebrew": ["Jewish"],
    "Greek": ["Greek"],
    "Turkish": ["Turkish"],
}


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return v
    s = str(v).strip()
    return [s] if s else []


def main():
    empties = []
    changed = 0
    for p in sorted(ROOT.glob("*.json")):
        obj = json.loads(p.read_text(encoding="utf-8"))
        d = obj["data"]
        ch = False

        # 1. list-typed fields written as strings by patch pass 1
        for k in ("emotional_traits", "hidden_personality_traits", "popularity_by_region"):
            if isinstance(d.get(k), str):
                d[k] = as_list(d[k])
                ch = True

        # 2. culture must be a list; derive from origin when absent
        if not isinstance(d.get("culture"), list):
            d["culture"] = as_list(d.get("culture"))
            ch = True
        if not d["culture"]:
            origin = (d.get("origin") or "").split("/")[0].strip()
            d["culture"] = CULTURE_BY_ORIGIN.get(origin) or ([origin] if origin else [])
            empties.append((p.stem, origin, d["culture"]))
            ch = True

        if ch:
            p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                         encoding="utf-8")
            changed += 1

    print("patched:", changed)
    print("culture filled from origin:", empties)


if __name__ == "__main__":
    main()
