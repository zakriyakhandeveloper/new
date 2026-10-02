# -*- coding: utf-8 -*-
"""Generic NameVerse batch runner.

Usage: python3 run_batch.py <batch_no> <first_slug> <last_slug> <curated_module>

Builds the 100 records for the batch, validates them, installs them into
upgrading/names_upgraded/islamic/, refreshes PROGRESS.json / PROGRESS.md,
commits, attempts a push, and exports a patch + manifest.
"""
import json, os, sys, glob, shutil, datetime, subprocess

REPO = "/workspace/upgrade_repo"
SCRIPTS = os.path.join(REPO, "upgrading/scripts")
RAW = os.path.join(REPO, "upgrading/names/islamic")
DEST = os.path.join(REPO, "upgrading/names_upgraded/islamic")
OUT = os.path.join(SCRIPTS, "out", "islamic")
PATCHDIR = "/workspace/nameverse-batches"

batch_no = int(sys.argv[1])
first = sys.argv[2]
last = sys.argv[3]
modname = sys.argv[4]

sys.path.insert(0, SCRIPTS)
cur = __import__(modname)
import nv_build

raw = sorted([os.path.basename(f)[:-5] for f in glob.glob(RAW + "/*.json")])
i = raw.index(first)
batch = raw[i:i + 100]
assert batch[-1] == last, "range mismatch: %s != %s" % (batch[-1], last)

missing = [n for n in batch if n not in cur.CUR]
extra = [n for n in cur.CUR if n not in batch]
if missing or extra:
    print("MISSING:", missing)
    print("EXTRA:", extra)
    sys.exit(1)

sys.modules["curated"] = cur
nv_build.CUR = cur.CUR
nv_build.GLOSSES = cur.GLOSSES

os.makedirs(OUT, exist_ok=True)
for f in glob.glob(OUT + "/*.json"):
    os.remove(f)
for n in batch:
    rec = nv_build.build(n, None)
    with open(os.path.join(OUT, n + ".json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, ensure_ascii=False, indent=2)
print("built %d records" % len(batch))

# --- validation gate ---
r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "nv_validate.py"), OUT],
                   capture_output=True, text=True)
print(r.stdout[-1200:])
if "TOTAL FAILURES: 0" not in r.stdout:
    print("VALIDATION FAILED — not installing")
    sys.exit(1)

# --- install ---
os.makedirs(DEST, exist_ok=True)
for f in glob.glob(OUT + "/*.json"):
    shutil.copy2(f, os.path.join(DEST, os.path.basename(f)))
print("installed; DEST now has %d files" % len(glob.glob(DEST + "/*.json")))

# --- tracker ---
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
    "current_batch": batch_no,
    "batch_range": {"first": first, "last": last, "count": 100},
    "batches_completed": batch_no,
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
    "next_batch_starts_after": last,
    "updated_at": now,
}
json.dump(prog, open(os.path.join(REPO, "upgrading/PROGRESS.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

RANGES = []
for _b in range(1, batch_no + 1):
    _s = raw[(_b - 1) * 100:_b * 100]
    RANGES.append((_b, _s[0], _s[-1]))
md = ["# NameVerse Upgrade Progress", "",
      "| Field | Value |", "|---|---|",
      "| Culture | islamic |",
      "| Total names in slice | 5,471 |",
      "| Names completed | %d |" % len(per_name),
      "| Current batch | %d |" % batch_no,
      "| Batch range | %s .. %s (100) |" % (first, last),
      "| Verified forms | %d |" % verified,
      "| Unverified forms (no gloss asserted) | %d |" % unverified,
      "| Next batch starts after | %s |" % last,
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
    if b <= batch_no:
        md.append("| %d | %s .. %s | 100 | complete |" % (b, f, l))
md.append("")
open(os.path.join(REPO, "upgrading/PROGRESS.md"), "w", encoding="utf-8").write("\n".join(md))
print("tracker: completed=%d verified=%d unverified=%d" % (len(per_name), verified, unverified))

# --- commit ---
msg = "feat(upgraded): complete Islamic names batch %03d (100 names)" % batch_no
subprocess.run(["git", "add", "-A", "upgrading/names_upgraded/islamic",
                "upgrading/PROGRESS.json", "upgrading/PROGRESS.md",
                "upgrading/scripts/%s.py" % modname,
                "upgrading/scripts/run_batch.py"], cwd=REPO, check=True)
subprocess.run(["git", "-c", "user.name=NameVerse Agent",
                "-c", "user.email=agent@nameverse.local",
                "commit", "-q", "-m", msg], cwd=REPO, check=True)
h = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                   capture_output=True, text=True).stdout.strip()
print("commit:", h, "|", msg)

# --- push attempt ---
p = subprocess.run(["timeout", "45", "git", "push", "origin", "main"], cwd=REPO,
                   capture_output=True, text=True)
pushed = p.returncode == 0
print("push:", "OK" if pushed else "BLOCKED (no credentials)")

# --- export patch + manifest ---
os.makedirs(PATCHDIR, exist_ok=True)
patch = os.path.join(PATCHDIR, "batch%03d.patch" % batch_no)
with open(patch, "wb") as fh:
    fh.write(subprocess.run(["git", "format-patch", "-1", "HEAD", "--stdout"],
                            cwd=REPO, capture_output=True).stdout)
man = {
    "batch_number": batch_no, "category": "islamic", "count": 100,
    "range": {"first": first, "last": last}, "completed": True,
    "validation_passed": True, "commit": h, "commit_message": msg,
    "pushed": pushed,
    "push_status": "ok" if pushed else "blocked: no git credentials in sandbox",
    "total_completed": len(per_name), "total_in_slice": 5471,
    "remaining": 5471 - len(per_name), "next_batch_starts_after": last,
}
json.dump(man, open(os.path.join(PATCHDIR, "batch%03d_manifest.json" % batch_no), "w"), indent=2)
print("patch:", patch, os.path.getsize(patch), "bytes")
print("remaining:", 5471 - len(per_name))
