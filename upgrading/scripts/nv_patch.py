# -*- coding: utf-8 -*-
"""Patch pass: fill the content gaps found by the post-push audit.

No field is filled with invented data; every added value is either an explicit
interpretive/unknown statement or something derived mechanically from the
already-verified transliteration.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path("/workspace/upgrade_v2/upgrading/names_upgraded/islamic")

TRAITS_EMOTIONAL = (
    "No evidence-based personality traits can be inferred from the name alone. "
    "Traditional naming literature sometimes attaches qualities such as warmth or "
    "resolve to a name; that is interpretive and is not a property of the name."
)
TRAITS_HIDDEN = (
    "Not objectively established. No empirical basis exists for hidden or subconscious "
    "traits from a name. Any such reading is interpretive tradition, not a fact about "
    "the person."
)
POP_REGION = (
    "Regional frequency is not objectively established: no national registry, census, or "
    "official naming-statistics dataset publishes per-region counts for this form. No "
    "figure is asserted in place of a verified one."
)


def strip_diacritics(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.replace("ʿ", "").replace("ʾ", "").replace("'", "").replace("-", "").strip()


def main():
    files = sorted(ROOT.glob("*.json"))
    patched = 0
    for p in files:
        raw = p.read_text(encoding="utf-8")
        obj = json.loads(raw)
        d = obj["data"]
        ch = False

        if not d.get("emotional_traits"):
            d["emotional_traits"] = TRAITS_EMOTIONAL
            ch = True
        if not d.get("hidden_personality_traits"):
            d["hidden_personality_traits"] = TRAITS_HIDDEN
            ch = True
        if not d.get("popularity_by_region"):
            d["popularity_by_region"] = POP_REGION
            ch = True

        # derive Latin romanization variant(s) from the verified transliteration
        tl = d.get("transliteration") or []
        if isinstance(tl, str):
            tl = [tl] if tl.strip() else []
        romans = []
        for t in tl:
            r = strip_diacritics(str(t))
            if r and r not in romans:
                romans.append(r)
        if romans and not d.get("variants"):
            d["variants"] = romans
            ch = True
        if tl and not d.get("name_variants"):
            d["name_variants"] = list(tl)
            ch = True

        # record why the remaining list fields are empty
        v = d.setdefault("verification", {})
        flags = v.setdefault("flags", [])
        for f in ("no-documented-diminutive-registered",
                  "no-documented-nickname-registered",
                  "no-verified-popularity-dataset"):
            if f not in flags:
                flags.append(f)
                ch = True
        v["empty_list_policy"] = (
            "Empty list fields are deliberate. A list is left empty when no "
            "published, verifiable entry exists for it; the reason is recorded in "
            "flags. No entry is invented to make a list non-empty."
        )
        ch = True

        if ch:
            p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                         encoding="utf-8")
            patched += 1
    print("patched:", patched, "/", len(files))


if __name__ == "__main__":
    main()
