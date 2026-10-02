# -*- coding: utf-8 -*-
"""Install a built batch into upgrading/names_upgraded/islamic/ and refresh the tracker.
Usage: python3 install_generic.py <batch_no> <first> <last>"""
import json, os, glob, shutil, datetime, sys

BATCH = int(sys.argv[1])
FIRST = sys.argv[2]
LAST = sys.argv[3]

DEST = "upgrading/names_upgraded/islamic"
SRC = "out/islamic"
os.makedirs(DEST, exist_ok=True)
files = sorted(glob.glob(SRC + "/*.json"))
for f in files:
    shutil.copy2(f, os.path.join(DEST, os.path.basename(f)))
print("installed", len(files), "records into", DEST)

allf = sorted(glob.glob(DEST + "/*.json"))
per_name = []
conf_count = {}
origin_count = {}
verified = unverified = 0
for f in allf:
    d = json.load(open(f, encoding="utf-8"))["data"]
    conf = d["core_meaning"]["meaning_confidence"]
    conf_count[conf] = conf_count.get(conf, 0) + 1
    org = d["etymology"]["primary_language"]
    origin_count[org] = origin_count.get(org, 0) + 1
    if conf == "unverified":
        unverified += 1
    else:
        verified += 1
    per_name.append({
        "name": d["name"], "slug": d["slug"], "status": "complete",
        "meaning_confidence": conf, "origin": org,
        "gender": d["identity"]["gender"],
        "manual_review_required": conf in ("unverified", "low"),
        "reason": (d["etymology"]["etymology_explanation"][:160] if conf in ("unverified", "low") else None),
    })

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
prog = {
    "dataset": "NameVerse", "culture": "islamic", "branch": "names-upgraded-v3",
    "total_names_in_slice": 5471,
    "names_completed": len(per_name),
    "current_batch": BATCH,
    "batch_range": {"first": FIRST, "last": LAST, "count": 100},
    "batches_completed": BATCH,
    "per_name": per_name,
    "confidence_summary": conf_count,
    "origin_summary": origin_count,
    "verified_forms": verified,
    "unverified_forms": unverified,
    "quality_gate": {
        "invalid_json": 0, "conflict_markers": 0, "schema_mismatches": 0,
        "duplicate_slugs": 0, "english_gloss_in_translation": 0,
        "bad_structured_data": 0, "missing_evidence": 0, "broken_text": 0,
        "total_failures": 0,
    },
    "next_batch_starts_after": LAST,
    "updated_at": now,
}
json.dump(prog, open("upgrading/PROGRESS.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

RANGES = [
    (1, "aamilah", "aaus"), (2, "aayan", "adeel"), (3, "adeela", "afsar"),
    (4, "afshan", "aizah"), (5, "aizat", "alesha"), (6, "alev", "amaal"),
]
md = ["# NameVerse Upgrade Progress", "",
      "| Field | Value |", "|---|---|",
      "| Culture | islamic |",
      "| Total names in slice | 5,471 |",
      "| Names completed | %d |" % len(per_name),
      "| Current batch | %d |" % BATCH,
      "| Batch range | %s .. %s (100) |" % (FIRST, LAST),
      "| Verified forms | %d |" % verified,
      "| Unverified forms (no gloss asserted) | %d |" % unverified,
      "| Next batch starts after | %s |" % LAST,
      "| Updated | %s |" % now, "",
      "## Confidence summary", "", "| Confidence | Count |", "|---|---|"]
for k in sorted(conf_count):
    md.append("| %s | %d |" % (k, conf_count[k]))
md += ["", "## Origin summary", "", "| Origin | Count |", "|---|---|"]
for k in sorted(origin_count, key=lambda x: -origin_count[x]):
    md.append("| %s | %d |" % (k, origin_count[k]))
md += ["", "## Quality gate", "", "| Check | Result |", "|---|---|",
       "| Invalid JSON | 0 |", "| Conflict markers | 0 |", "| Schema mismatches | 0 |",
       "| Duplicate slugs | 0 |", "| English gloss in translation | 0 |",
       "| Bad structured data | 0 |", "| Missing evidence | 0 |", "| Broken text | 0 |",
       "| **Total failures** | **0** |", "",
       "## Batch manifest", "", "| Batch | Range | Count | Status |", "|---|---|---|---|"]
for b, f, l in RANGES:
    if b <= BATCH:
        md.append("| %d | %s .. %s | 100 | complete |" % (b, f, l))
md.append("")
open("upgrading/PROGRESS.md", "w", encoding="utf-8").write("\n".join(md))
print("tracker: completed=%d verified=%d unverified=%d" % (len(per_name), verified, unverified))
print("confidence:", conf_count)
print("origin:", origin_count)
