# -*- coding: utf-8 -*-
"""Build batch 28 (harisah..helai) using nv_build.build with curated28."""
import json, os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import curated28
import nv_build

R = "/workspace/upgrade_repo/upgrading/names/islamic"
raw = sorted([os.path.basename(f)[:-5] for f in glob.glob(R + "/*.json")])
i = raw.index("harisa")
batch = raw[i+1:i+101]

missing = [n for n in batch if n not in curated28.CUR]
extra = [n for n in curated28.CUR if n not in batch]
print("batch:", len(batch), "curated:", len(curated28.CUR))
print("missing from CUR:", missing)
print("extra in CUR:", extra)
if missing or extra:
    sys.exit(1)

# make nv_build see curated28 as `curated`
sys.modules["curated"] = curated28
nv_build.CUR = curated28.CUR
nv_build.GLOSSES = curated28.GLOSSES

out = os.path.join(HERE, "out", "islamic")
os.makedirs(out, exist_ok=True)
for f in glob.glob(out + "/*.json"):
    os.remove(f)

for n in batch:
    rec = nv_build.build(n, None)
    with open(os.path.join(out, n + ".json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, ensure_ascii=False, indent=2)
print("built", len(batch), "records into", out)
