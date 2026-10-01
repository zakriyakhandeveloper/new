# -*- coding: utf-8 -*-
"""NameVerse final audit / validator for an upgraded slice."""
import json
import pathlib
import sys
from collections import Counter

REQ = ["name", "slug", "language", "gender", "gender_notes", "origin", "religion", "category",
       "culture", "short_meaning", "long_meaning", "spiritual_meaning", "emotional_traits",
       "hidden_personality_traits", "etymology", "root", "language_root", "root_letters",
       "syllables", "name_length", "transliteration", "lucky_number", "lucky_day", "lucky_colors",
       "lucky_stone", "ruling_planet", "life_path_number", "numerology_meaning", "in_arabic",
       "in_urdu", "in_hindi", "in_pashto", "in_persian", "in_english", "pronunciation",
       "name_variants", "variants", "diminutives", "nicknames", "related_names",
       "similar_sounding_names", "notable_people", "celebrity_usage", "popularity_score",
       "popularity_by_region", "cultural_impact", "spiritual_significance", "spiritual_symbolism",
       "islamic_reference", "historical_references", "modern_usage", "name_in_real_life",
       "social_tags", "monetization", "user_engagement", "social_optimization", "accessibility",
       "seo", "seo_title", "meta_description", "keywords", "canonical_url", "intro_paragraph",
       "structured_data", "structured_data_faq", "structured_data_breadcrumb", "advanced_seo",
       "confidence", "data_quality", "created_at", "updated_at", "tier1_verified",
       "tier2_explanatory", "tier3_interpretive", "verification", "nameverse"]

TRANSLATIONS = ["in_arabic", "in_urdu", "in_hindi", "in_pashto", "in_persian", "in_english"]

FABRICATED_PATTERNS = [
    "Historical records show that", "carried significant weight in that era",
    "has been a source of inspiration throughout their life", "brings blessings",
    "very popular in", "well-regarded in",
]

MARKERS = ("<<<<<<<", ">>>>>>>", "|||||||", "=======")


def audit(directory):
    files = sorted(pathlib.Path(directory).rglob("*.json"))
    bad_json, missing, markers, thin, flagged = [], [], [], [], []
    confs, faqs, fab = Counter(), [], []
    for p in files:
        raw = p.read_text(encoding="utf-8")
        for m in MARKERS:
            if raw.count(m):
                markers.append((str(p), m))
                break
        try:
            d = json.loads(raw)
        except Exception as e:
            bad_json.append((str(p), str(e)[:80]))
            continue
        data = d.get("data", d)
        miss = [k for k in REQ if k not in data]
        if miss:
            missing.append((str(p), miss))
        for k in TRANSLATIONS:
            blk = data.get(k)
            if not isinstance(blk, dict) or not blk.get("name") or not blk.get("meaning"):
                missing.append((str(p), [k]))
        seo = data.get("seo") or {}
        faqs.append(len(seo.get("faq") or []))
        if len(seo.get("faq") or []) < 15:
            thin.append((str(p), len(seo.get("faq") or [])))
        confs[data.get("confidence", {}).get("meaning", "?")] += 1
        blob = json.dumps(data, ensure_ascii=False)
        for pat in FABRICATED_PATTERNS:
            if pat in blob:
                fab.append((str(p), pat))
        if data.get("data_quality", {}).get("authenticity_flags"):
            flagged.append(str(p))
    print(f"directory        : {directory}")
    print(f"json files       : {len(files)}")
    print(f"invalid JSON     : {len(bad_json)}")
    print(f"files w/ markers : {len(markers)}")
    print(f"missing fields   : {len(missing)}")
    print(f"faq < 15         : {len(thin)}")
    print(f"fabrication hits : {len(fab)}")
    print(f"meaning conf     : {dict(confs)}")
    if faqs:
        print(f"faq count        : min {min(faqs)} / max {max(faqs)}")
    for label, coll in (("INVALID", bad_json), ("MARKER", markers), ("MISSING", missing),
                        ("THIN-FAQ", thin), ("FABRICATED", fab)):
        for item in coll[:8]:
            print(f"  {label}: {item}")
    return not (bad_json or markers or missing or fab)


if __name__ == "__main__":
    ok = audit(sys.argv[1] if len(sys.argv) > 1 else "/workspace/nv/out/islamic")
    print("RESULT:", "PASS" if ok else "FAIL")
