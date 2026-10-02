# -*- coding: utf-8 -*-
"""Build batch 10 (arsala..asima) using the existing nv_build renderer with curated10 data."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curated10, nv_build

nv_build.CUR = curated10.CUR
nv_build.GLOSSES = curated10.GLOSSES

rows = json.load(open("work/batch10_src.json", encoding="utf-8"))
out = "out/islamic"
os.makedirs(out, exist_ok=True)
missing = []
for r in rows:
    n = r["name"]
    if n not in curated10.CUR:
        missing.append(n); continue
    rec = nv_build.build(n, r)
    with open(os.path.join(out, n + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)
print("built", len(rows) - len(missing), "of", len(rows))
if missing:
    print("MISSING FROM CURATED:", missing)
