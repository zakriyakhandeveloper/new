# -*- coding: utf-8 -*-
"""Build batch 24 (ferhat..ghadir) using the existing nv_build renderer."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nv_build, curated24

nv_build.GLOSSES = curated24.GLOSSES
nv_build.CUR = curated24.CUR

SRC = os.path.join(HERE, "..", "names", "islamic")
OUT = os.path.join(HERE, "..", "..", "out", "islamic")
os.makedirs(OUT, exist_ok=True)

names = sorted(curated24.CUR.keys())
for n in names:
    src = os.path.join(SRC, n + ".json")
    row = json.load(open(src, encoding="utf-8")) if os.path.exists(src) else {}
    rec = nv_build.build(n, row)
    json.dump(rec, open(os.path.join(OUT, n + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
print("BUILT", len(names), "->", OUT)
