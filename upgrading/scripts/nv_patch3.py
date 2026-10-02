# -*- coding: utf-8 -*-
"""Patch pass 3: remove script-form conflation in the in_persian block.

The post-push audit found that on all 54 Arabic-origin records the in_persian
block presented a DIFFERENT letter form from the in_arabic original
(e.g. aamir: arabic عامر but persian امیر), while the in_urdu and in_pashto
blocks correctly carried the Arabic lexical item. Presenting a different
lexical word under a language label is exactly the conflation the NameVerse
spec prohibits (cf. آباد vs عابد).

Fix: where the origin is Arabic and a distinct Persian form was asserted without
support, carry the same Arabic lexical item and say so in the language note.
No new lexical claim is introduced; an unsupported substitution is removed.
"""
import json
import pathlib

ROOT = pathlib.Path("/workspace/upgrade_v2/upgrading/names_upgraded/islamic")

NOTE = ("Persian uses the Arabic-derived script. No separate Persian lexical form is "
        "asserted for this name; the Arabic form is carried over, as it is borrowed "
        "into Persian usage rather than re-lexicalised.")


def main():
    fixed = 0
    for p in sorted(ROOT.glob("*.json")):
        obj = json.loads(p.read_text(encoding="utf-8"))
        d = obj["data"]
        origin = (d.get("origin") or "")
        if not origin.startswith("Arabic"):
            continue
        ar = (d.get("in_arabic") or {}).get("name", "")
        pe = d.get("in_persian")
        if not isinstance(pe, dict) or not ar or ar.startswith("Not"):
            continue
        if pe.get("name") == ar:
            continue

        old = pe.get("name", "")
        pe["name"] = ar
        lm = pe.get("long_meaning", "")
        if old and lm.startswith(old):
            lm = ar + lm[len(old):]
        pe["long_meaning"] = lm
        pe["language_note"] = NOTE
        fixed += 1
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")
    print("persian conflation fixed:", fixed)


if __name__ == "__main__":
    main()
