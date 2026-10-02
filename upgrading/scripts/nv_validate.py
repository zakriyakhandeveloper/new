# -*- coding: utf-8 -*-
"""Full batch gate for the NameVerse nested schema. Exit 1 on any failure."""
import json, os, re, sys, glob, unicodedata

REF_ORDER = ["name","slug","identity","core_meaning","etymology","language","origin","religion",
"islamic_naming_context","cultural_context","semantic_field","spiritual_meaning",
"personality_associations","hidden_personality_traits","numerology","lucky_attributes",
"translations","translation_quality","pronunciation","name_variants","historical_context",
"modern_usage","popularity","celebrity_usage","real_world_usage","name_story","faq","seo",
"seo_content","social_tags","content_quality","evidence","provenance","structured_data",
"accessibility","editorial_validation","timestamps"]

SCRIPT = {"urdu": r'[\u0600-\u06FF]', "persian": r'[\u0600-\u06FF]', "pashto": r'[\u0600-\u06FF]',
          "arabic": r'[\u0600-\u06FF]', "hindi": r'[\u0900-\u097F]'}
LATIN_WORD = re.compile(r'[A-Za-z]{3,}')

def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, path + "/" + str(i))
    else:
        yield path, o

def main(d):
    fails = []
    files = sorted(glob.glob(os.path.join(d, "*.json")))
    if not files:
        print("FAIL: no files"); return 1
    seen_slugs = {}
    n_eng_gloss = 0
    n_empty = 0
    n_marker = 0
    n_bad_sd = 0
    n_dup = 0
    n_order = 0
    n_evidence = 0
    n_broken = 0
    for f in files:
        raw = open(f, encoding="utf-8").read()
        for m in ("<<<<<<<", ">>>>>>>", "|||||||", "======="):
            if m in raw:
                n_marker += 1; fails.append("marker %s in %s" % (m, f))
        try:
            rec = json.loads(raw)
        except Exception as e:
            fails.append("invalid JSON %s: %s" % (f, e)); continue
        if rec.get("success") is not True:
            fails.append("success!=true %s" % f)
        data = rec.get("data")
        if not isinstance(data, dict):
            fails.append("no data %s" % f); continue
        # schema order + key set
        keys = list(data.keys())
        if keys != REF_ORDER:
            n_order += 1
            fails.append("schema order/set mismatch %s: %s" % (f, [k for k in keys if k not in REF_ORDER] or "order"))
        # duplicate detection
        s = data.get("slug")
        if s in seen_slugs:
            n_dup += 1; fails.append("duplicate slug %s" % s)
        seen_slugs[s] = f
        # empty-field scan (None/""/[] allowed only where explicitly justified)
        for p, v in walk(data):
            if v is None or v == "" or v == []:
                n_empty += 1
        # translation validation: non-English meaning must be in target script
        for lang, pat in SCRIPT.items():
            blk = data.get("translations", {}).get(lang, {})
            m = blk.get("meaning")
            if m:
                if not re.search(pat, m):
                    n_eng_gloss += 1
                    fails.append("English gloss in %s translation of %s: %r" % (lang, f, m[:40]))
                if LATIN_WORD.search(m) and not re.search(pat, m):
                    n_eng_gloss += 1
        # structured data
        sd = data.get("structured_data", {})
        if sd.get("@type") != "DefinedTerm" or sd.get("@context") != "https://schema.org":
            n_bad_sd += 1; fails.append("bad structured_data %s" % f)
        if not isinstance(sd.get("additionalProperty"), list) or not sd.get("additionalProperty"):
            n_bad_sd += 1; fails.append("bad additionalProperty %s" % f)
        # evidence
        ev = data.get("evidence", {})
        if not isinstance(ev.get("core_claims"), list) or not ev.get("core_claims"):
            n_evidence += 1; fails.append("no core_claims %s" % f)
        # broken text
        for p, v in walk(data):
            if isinstance(v, str):
                if "\ufffd" in v or "\\u" in v or "TODO" in v or "XXX" in v or "lorem" in v.lower():
                    n_broken += 1; fails.append("broken text %s at %s" % (f, p))
        # faq
        if not isinstance(data.get("faq"), list) or len(data["faq"]) < 5:
            fails.append("faq too short %s" % f)
        # seo
        seo = data.get("seo", {})
        for k in ("title","meta_description","h1","focus_keyword","secondary_keywords","search_intents","description_paragraph","editorial_seo_rule"):
            if k not in seo:
                fails.append("seo missing %s in %s" % (k, f))
        if "seo_score" in json.dumps(seo):
            fails.append("arbitrary seo_score present %s" % f)
    print("files: %d" % len(files))
    print("invalid JSON: 0" if not any("invalid JSON" in x for x in fails) else "invalid JSON: SEE FAILS")
    print("conflict markers: %d" % n_marker)
    print("schema order/set mismatches: %d" % n_order)
    print("duplicate slugs: %d" % n_dup)
    print("English-gloss-in-translation fields: %d" % n_eng_gloss)
    print("bad structured_data: %d" % n_bad_sd)
    print("missing evidence: %d" % n_evidence)
    print("broken text: %d" % n_broken)
    print("empty/None/[] leaf values (informational): %d" % n_empty)
    print("TOTAL FAILURES: %d" % len(fails))
    for x in fails[:25]:
        print("  -", x)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "out/islamic"))
