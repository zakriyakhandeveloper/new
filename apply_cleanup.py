import json, os, collections, datetime

removed = json.load(open('/workspace/removed.json'))
kept = json.load(open('/workspace/kept.json'))

CULT = ['islamic', 'christian', 'hindu']
BEFORE = {'islamic': 14411, 'christian': 12894, 'hindu': 10411}

# ---- apply deletions ----
deleted = 0
for r in removed:
    p = r['path']
    if os.path.exists(p):
        os.remove(p)
        deleted += 1
print('deleted files:', deleted)

# ---- verify ----
after = {}
for c in CULT:
    after[c] = len([f for f in os.listdir('upgrading/names/%s' % c) if f.endswith('.json')])
print('after counts:', after, '| total', sum(after.values()))

# ---- build report ----
reasons = collections.Counter(r['reason'] for r in removed)
by_culture_reason = collections.defaultdict(collections.Counter)
for r in removed:
    by_culture_reason[r['culture']][r['reason']] += 1

kept_by_culture = collections.Counter(k['culture'] for k in kept)
attested = collections.Counter(k['culture'] for k in kept if k['fame'] > 0)

report = {
    "cleanup": "NameVerse name-dataset reduction",
    "generated_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
    "source_commit": "ccdd7fa852bf14fac1e9f29ff7030206d9d0d5c4",
    "archive": {
        "branch": "names-full-backup",
        "sha": "ccdd7fa852bf14fac1e9f29ff7030206d9d0d5c4",
        "note": "Full original 37,716-record set is preserved on this branch. Nothing is permanently lost.",
        "restore_command": "git checkout names-full-backup -- upgrading/names/"
    },
    "methodology": {
        "fame_signal": "philipperemy/name-dataset v3 (first_names.pkl.gz) - per-country given-name rank tables for 727,556 names, derived from public national name statistics.",
        "fame_score": "70*(1 - log10(best_rank_in_culture_countries)/3) + 25*(1 - log10(best_rank_anywhere)/3) + 1.2*min(countries_present,25)",
        "culture_country_sets": "Each culture scored against a curated set of countries where that naming tradition is dominant.",
        "duplicate_rule": "Same normalized name (lowercase, alphanumerics only) -> keep the single highest-fame record.",
        "cluster_rule": "Trivial transliteration variants (doubled letters, ah/eh, ee/ie, oo/ou, y/i, trailing h) are merged ONLY when at most one form is independently attested in the frequency dataset. Distinct attested names are never merged.",
        "not_famous_rule": "Records absent from the frequency dataset, or below the per-culture fame cut-off, are removed.",
        "force_keep": "The 100 source records that already have upgraded counterparts under upgrading/names_upgraded/islamic/ are always retained.",
        "limitations": [
            "The frequency dataset covers ~727k names but is not exhaustive for South Asian and Muslim naming traditions; some genuinely used names may be absent and were therefore removed.",
            "The source records' own popularity_score, celebrity_usage, historical_references and name_in_real_life fields were found to be fabricated (e.g. obscure 'Arqamun' scored 61 while 'Ahmed' scored 54; celebrity lists contained empty strings and 'Not known') and were NOT used as evidence.",
            "This is a fame/frequency-based reduction, not a linguistic verification of each name's meaning or origin."
        ]
    },
    "summary": {
        "before_total": sum(BEFORE.values()),
        "after_total": sum(after.values()),
        "removed_total": len(removed),
        "target": 19000,
        "per_culture": {
            c: {
                "before": BEFORE[c],
                "after": after[c],
                "removed": BEFORE[c] - after[c],
                "reasons": dict(by_culture_reason[c]),
                "kept_attested_in_frequency_dataset": attested[c],
                "kept_not_in_dataset": kept_by_culture[c] - attested[c]
            } for c in CULT
        },
        "reason_totals": dict(reasons)
    },
    "removal_manifest": [
        {"name": r['file'][:-5], "culture": r['culture'], "reason": r['reason'], "detail": r['detail']}
        for r in sorted(removed, key=lambda x: (x['culture'], x['file']))
    ],
    "kept_manifest": [
        {"name": k['file'][:-5], "culture": k['culture'], "fame_score": k['fame']}
        for k in sorted(kept, key=lambda x: (x['culture'], -x['fame'], x['file']))
    ]
}

json.dump(report, open('upgrading/CLEANUP_REPORT.json', 'w'), indent=1, ensure_ascii=False)
print('wrote CLEANUP_REPORT.json')

# ---- markdown ----
L = []
L.append('# NameVerse Dataset Cleanup Report\n')
L.append('**Generated:** %s  ' % report['generated_at'])
L.append('**Source commit:** `%s`  ' % report['source_commit'])
L.append('**Archive branch:** `names-full-backup` (`%s`)\n' % report['archive']['sha'])
L.append('> The full original 37,716-record set is preserved on `names-full-backup`. '
         'Nothing was permanently lost. Restore with `git checkout names-full-backup -- upgrading/names/`.\n')
L.append('## Result\n')
L.append('| Culture | Before | After | Removed |')
L.append('|---|---:|---:|---:|')
for c in CULT:
    L.append('| %s | %d | %d | %d |' % (c, BEFORE[c], after[c], BEFORE[c] - after[c]))
L.append('| **Total** | **%d** | **%d** | **%d** |\n' % (sum(BEFORE.values()), sum(after.values()), len(removed)))
L.append('Target was ~19,000; achieved **%d**.\n' % sum(after.values()))
L.append('## Removal reasons\n')
L.append('| Reason | Count | Meaning |')
L.append('|---|---:|---|')
desc = {
 'invalid': 'Malformed slug, empty name, unparseable JSON, or non-record index file',
 'duplicate': 'Same normalized name appearing more than once',
 'cluster': 'Trivial transliteration variant of another record (only when at most one form is independently attested)',
 'not-famous': 'Absent from the real name-frequency dataset, or below the per-culture fame cut-off',
}
for r, n in reasons.most_common():
    L.append('| %s | %d | %s |' % (r, n, desc.get(r, '')))
L.append('')
L.append('### Per culture\n')
for c in CULT:
    L.append('**%s** — removed %d:' % (c, BEFORE[c] - after[c]))
    for r, n in by_culture_reason[c].most_common():
        L.append('- %s: %d' % (r, n))
    L.append('- kept and present in the frequency dataset: %d' % attested[c])
    L.append('- kept but not in the dataset (retained for other reasons): %d\n' % (kept_by_culture[c] - attested[c]))
L.append('## Method\n')
L.append('Fame was measured with **philipperemy/name-dataset v3** — per-country given-name rank tables for '
         '727,556 names derived from public national name statistics. Each culture was scored against a curated '
         'set of countries where that naming tradition is dominant.\n')
L.append('```')
L.append('fame = 70*(1 - log10(best_rank_in_culture_countries)/3)')
L.append('     + 25*(1 - log10(best_rank_anywhere)/3)')
L.append('     + 1.2*min(countries_present, 25)')
L.append('```\n')
L.append('**Duplicates** — same normalized name, keep the highest-fame record.\n')
L.append('**Clusters** — trivial transliteration variants (doubled letters, `ah/eh`, `ee/ie`, `oo/ou`, `y/i`, '
         'trailing `h`) are merged *only* when at most one form is independently attested. Distinct attested '
         'names are never merged.\n')
L.append('**Force-keep** — the 100 source records that already have upgraded counterparts under '
         '`upgrading/names_upgraded/islamic/` are always retained.\n')
L.append('## Important caveat\n')
L.append('The source records\' own `popularity_score`, `celebrity_usage`, `historical_references` and '
         '`name_in_real_life` fields were found to be **fabricated** and were not used as evidence:\n')
L.append('- obscure `Arqamun` scored 61 while `Ahmed` scored 54')
L.append('- celebrity lists contained empty strings (`Mazyaan: ["",""]`) and `"Not known"` (`Sharvikus`)')
L.append('- `Elvika` listed `Ramakrishna Paramahamsa` — a different name entirely\n')
L.append('This is a **fame/frequency-based reduction**, not a linguistic verification of each name\'s meaning '
         'or origin. The frequency dataset is not exhaustive for South Asian and Muslim naming traditions, so '
         'some genuinely used names may have been removed. They remain recoverable from `names-full-backup`.\n')
L.append('## Manifests\n')
L.append('- `upgrading/CLEANUP_REPORT.json` — full removal manifest (%d entries) and kept manifest (%d entries)'
         % (len(removed), len(kept)))
open('upgrading/CLEANUP_REPORT.md', 'w').write('\n'.join(L))
print('wrote CLEANUP_REPORT.md')
