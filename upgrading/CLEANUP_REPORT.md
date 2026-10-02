# NameVerse Dataset Cleanup Report

**Generated:** 2026-10-02T03:08:22Z  
**Source commit:** `ccdd7fa852bf14fac1e9f29ff7030206d9d0d5c4`  
**Archive branch:** `names-full-backup` (`ccdd7fa852bf14fac1e9f29ff7030206d9d0d5c4`)

> The full original 37,716-record set is preserved on `names-full-backup`. Nothing was permanently lost. Restore with `git checkout names-full-backup -- upgrading/names/`.

## Result

| Culture | Before | After | Removed |
|---|---:|---:|---:|
| islamic | 14411 | 5471 | 8940 |
| christian | 12894 | 7685 | 5209 |
| hindu | 10411 | 5885 | 4526 |
| **Total** | **37716** | **19041** | **18675** |

Target was ~19,000; achieved **19041**.

## Removal reasons

| Reason | Count | Meaning |
|---|---:|---|
| not-famous | 16677 | Absent from the real name-frequency dataset, or below the per-culture fame cut-off |
| cluster | 1850 | Trivial transliteration variant of another record (only when at most one form is independently attested) |
| invalid | 111 | Malformed slug, empty name, unparseable JSON, or non-record index file |
| duplicate | 37 | Same normalized name appearing more than once |

### Per culture

**islamic** — removed 8940:
- not-famous: 7579
- cluster: 1328
- duplicate: 30
- invalid: 3
- kept and present in the frequency dataset: 5430
- kept but not in the dataset (retained for other reasons): 41

**christian** — removed 5209:
- not-famous: 4879
- cluster: 307
- invalid: 16
- duplicate: 7
- kept and present in the frequency dataset: 7685
- kept but not in the dataset (retained for other reasons): 0

**hindu** — removed 4526:
- not-famous: 4219
- cluster: 215
- invalid: 92
- kept and present in the frequency dataset: 5885
- kept but not in the dataset (retained for other reasons): 0

## Method

Fame was measured with **philipperemy/name-dataset v3** — per-country given-name rank tables for 727,556 names derived from public national name statistics. Each culture was scored against a curated set of countries where that naming tradition is dominant.

```
fame = 70*(1 - log10(best_rank_in_culture_countries)/3)
     + 25*(1 - log10(best_rank_anywhere)/3)
     + 1.2*min(countries_present, 25)
```

**Duplicates** — same normalized name, keep the highest-fame record.

**Clusters** — trivial transliteration variants (doubled letters, `ah/eh`, `ee/ie`, `oo/ou`, `y/i`, trailing `h`) are merged *only* when at most one form is independently attested. Distinct attested names are never merged.

**Force-keep** — the 100 source records that already have upgraded counterparts under `upgrading/names_upgraded/islamic/` are always retained.

## Important caveat

The source records' own `popularity_score`, `celebrity_usage`, `historical_references` and `name_in_real_life` fields were found to be **fabricated** and were not used as evidence:

- obscure `Arqamun` scored 61 while `Ahmed` scored 54
- celebrity lists contained empty strings (`Mazyaan: ["",""]`) and `"Not known"` (`Sharvikus`)
- `Elvika` listed `Ramakrishna Paramahamsa` — a different name entirely

This is a **fame/frequency-based reduction**, not a linguistic verification of each name's meaning or origin. The frequency dataset is not exhaustive for South Asian and Muslim naming traditions, so some genuinely used names may have been removed. They remain recoverable from `names-full-backup`.

## Manifests

- `upgrading/CLEANUP_REPORT.json` — full removal manifest (18675 entries) and kept manifest (19041 entries)