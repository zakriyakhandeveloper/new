# -*- coding: utf-8 -*-
"""Build batch 11 (asimah..aurangzeb) using the existing nv_build renderer with curated11 data."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curated11, nv_build

nv_build.CUR = curated11.CUR
nv_build.GLOSSES = curated11.GLOSSES

rows = json.load(open("work/batch11_src.json", encoding="utf-8"))
out = "out/islamic"
os.makedirs(out, exist_ok=True)
missing = []
for r in rows:
    n = r["name"]
    if n not in curated11.CUR:
        missing.append(n); continue
    rec = nv_build.build(n, r)
    with open(os.path.join(out, n + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)
print("built", len(rows) - len(missing), "of", len(rows))
if missing:
    print("MISSING FROM CURATED:", missing)
