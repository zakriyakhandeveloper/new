import json, glob, os, collections, re

CULTURES = ['islamic', 'christian', 'hindu']
TARGET = {'islamic': 7300, 'christian': 6500, 'hindu': 5200}
MINKEYS = {'gender', 'language', 'meaning', 'name', 'origin', 'religion',
           'similar_sounding_names', 'slug'}


def nonempty(v):
    if v is None:
        return False
    if isinstance(v, str):
        return v.strip() not in ('', 'Unknown', 'N/A', 'None', 'unknown')
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


def norm_name(n):
    return re.sub(r'[^a-z0-9]', '', str(n).lower())


def cluster_key(n):
    s = re.sub(r'[^a-z]', '', str(n).lower())
    s = re.sub(r'(.)\1+', r'\1', s)
    s = re.sub(r'(ah|eh)$', 'a', s)
    s = re.sub(r'(ee|ie)$', 'i', s)
    s = re.sub(r'(oo|ou)$', 'u', s)
    s = re.sub(r'y$', 'i', s)
    s = re.sub(r'h$', '', s)
    return s


def fame(dd):
    sc = float(dd.get('popularity_score') or 0)
    if nonempty(dd.get('celebrity_usage')):
        sc += 20
    if nonempty(dd.get('historical_references')):
        sc += 12
    if nonempty(dd.get('name_in_real_life')):
        sc += 8
    pbr = dd.get('popularity_by_region')
    if isinstance(pbr, list) and pbr:
        sc += min(len(pbr), 5) * 2
    o = dd.get('origin')
    if nonempty(o) and str(o).strip().lower() != 'unknown':
        sc += 6
    if nonempty(dd.get('category')):
        sc += 4
    lm = dd.get('long_meaning')
    if isinstance(lm, str) and len(lm) > 250:
        sc += 4
    if nonempty(dd.get('seo')):
        sc += 3
    return sc


report = {}
all_removed = []
all_kept = []

for c in CULTURES:
    files = sorted(glob.glob('upgrading/names/%s/*.json' % c))
    recs = []
    removed = []
    for f in files:
        b = os.path.basename(f)
        if b.startswith('_'):
            removed.append((f, b, 'invalid', 'non-record index file'))
            continue
        try:
            d = json.load(open(f))
        except Exception:
            removed.append((f, b, 'invalid', 'unparseable JSON'))
            continue
        if not isinstance(d, dict) or not isinstance(d.get('data'), dict):
            removed.append((f, b, 'invalid', 'not a name record'))
            continue
        dd = d['data']
        nm = str(dd.get('name') or '').strip()
        sl = str(dd.get('slug') or '').strip()
        if not nm or not re.fullmatch(r'[a-z0-9_-]+', sl):
            removed.append((f, b, 'invalid', 'malformed slug or empty name'))
            continue
        if set(dd.keys()) == MINKEYS:
            removed.append((f, b, 'stub', 'stub record: minimal 8-field schema, no content'))
            continue
        recs.append((f, b, dd))

    # --- duplicates: same normalized name, keep the richest ---
    bynorm = collections.defaultdict(list)
    for f, b, dd in recs:
        bynorm[norm_name(dd.get('name'))].append((f, b, dd))
    survivors = []
    for k, grp in bynorm.items():
        if len(grp) == 1:
            survivors.append(grp[0])
            continue
        grp.sort(key=lambda t: (-fame(t[2]), -len(json.dumps(t[2]))))
        survivors.append(grp[0])
        for f, b, dd in grp[1:]:
            removed.append((f, b, 'duplicate',
                            'duplicate of %s (same normalized name)' % grp[0][2].get('name')))

    # --- clusters: trivial transliteration variants, keep the richest ---
    byclu = collections.defaultdict(list)
    for f, b, dd in survivors:
        byclu[cluster_key(dd.get('name'))].append((f, b, dd))
    survivors2 = []
    for k, grp in byclu.items():
        if len(grp) == 1:
            survivors2.append(grp[0])
            continue
        grp.sort(key=lambda t: (-fame(t[2]), -len(json.dumps(t[2]))))
        survivors2.append(grp[0])
        for f, b, dd in grp[1:]:
            removed.append((f, b, 'cluster',
                            'transliteration variant of %s' % grp[0][2].get('name')))

    # --- fame ranking: keep top TARGET ---
    survivors2.sort(key=lambda t: (-fame(t[2]), str(t[2].get('name'))))
    keep_n = min(TARGET[c], len(survivors2))
    kept = survivors2[:keep_n]
    for f, b, dd in survivors2[keep_n:]:
        removed.append((f, b, 'not-famous',
                        'below fame cut-off (score %.0f)' % fame(dd)))

    reasons = collections.Counter(r[2] for r in removed)
    report[c] = {
        'total': len(files),
        'kept': len(kept),
        'removed': len(removed),
        'reasons': dict(reasons),
        'cutoff_score': fame(kept[-1][2]) if kept else None,
    }
    all_removed += [(c, r[0], r[1], r[2], r[3]) for r in removed]
    all_kept += [(c, f, b) for f, b, dd in kept]

print(json.dumps(report, indent=2))
print('TOTAL kept:', len(all_kept), '| removed:', len(all_removed))

with open('/workspace/removed.json', 'w') as fh:
    json.dump([{'culture': c, 'path': p, 'file': b, 'reason': r, 'detail': d}
               for c, p, b, r, d in all_removed], fh, indent=1)
with open('/workspace/kept.json', 'w') as fh:
    json.dump([{'culture': c, 'path': p, 'file': b} for c, p, b in all_kept], fh, indent=1)
with open('/workspace/remove_paths.txt', 'w') as fh:
    fh.write('\n'.join(p for c, p, b, r, d in all_removed))
print('wrote /workspace/removed.json, /workspace/kept.json, /workspace/remove_paths.txt')
