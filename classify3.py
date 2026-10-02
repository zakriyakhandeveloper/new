import json, glob, os, collections, re, math, gzip, pickle, gc

CULTURES = ['islamic', 'christian', 'hindu']
TARGET = {'islamic': 7300, 'christian': 6500, 'hindu': 5200}

CORE = {
 'islamic': set('PK SA AE EG MY ID BD TR IR IQ KW QA BH OM JO LB SY DZ MA TN LY NG SD YE PS AF KZ UZ AZ BN MV GM SN ML NE TD SO DJ KM MR BF GN SL TG BJ CI AL BA XK MK KG TJ TM'.split()),
 'christian': set('US GB CA IE DE FR IT ES PL NL SE NO DK FI PT AT BE CH GR RU UA RO HU CZ SK HR RS BG LT LV EE AU NZ PH MX BR AR CO CL PE VE EC GT CU DO PR ZA GH KE TZ UG ZM ZW CM ET NG AO MZ MG RW BI LS SZ NA BW'.split()),
 'hindu': set('IN NP MU SG MY AE KW QA BH OM SA GB US CA AU NZ ZA TT FJ GY SR ID BD LK MM KE TZ UG YT RE GP MQ'.split()),
}

print('loading ...', flush=True)
ND = pickle.load(gzip.open('/workspace/data/fn.pkl.gz', 'rb'))
print('names:', len(ND), flush=True)

# Build compact per-culture score tables, then free ND
SCORE = {}
for c in CULTURES:
    core = CORE[c]
    tbl = {}
    for k, v in ND.items():
        rk = v.get('rank')
        if not rk:
            continue
        rel = [r for cc, r in rk.items() if cc in core]
        best_rel = min(rel) if rel else None
        best_all = min(rk.values())
        n_all = len(rk)
        s = 0.0
        if best_rel is not None:
            s += 70.0 * (1.0 - min(1.0, math.log10(max(best_rel, 1)) / 3.0))
        else:
            s += 25.0 * (1.0 - min(1.0, math.log10(max(best_all, 1)) / 3.0))
        s += min(n_all, 25) * 1.2
        tbl[k.lower()] = round(s, 2)
    SCORE[c] = tbl
    print('  score table', c, len(tbl), flush=True)
del ND
gc.collect()

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

report = {}
all_removed = []
all_kept = []

for c in CULTURES:
    tbl = SCORE[c]
    files = sorted(glob.glob('upgrading/names/%s/*.json' % c))
    recs = []
    removed = []
    for f in files:
        b = os.path.basename(f)
        if b.startswith('_'):
            removed.append((f, b, 'invalid', 'non-record index file')); continue
        try:
            d = json.load(open(f))
        except Exception:
            removed.append((f, b, 'invalid', 'unparseable JSON')); continue
        if not isinstance(d, dict) or not isinstance(d.get('data'), dict):
            removed.append((f, b, 'invalid', 'not a name record')); continue
        dd = d['data']
        nm = str(dd.get('name') or '').strip()
        sl = str(dd.get('slug') or '').strip()
        if not nm or not re.fullmatch(r'[a-z0-9_-]+', sl):
            removed.append((f, b, 'invalid', 'malformed slug or empty name')); continue
        recs.append((f, b, nm, norm_name(nm), tbl.get(norm_name(nm), 0.0), len(json.dumps(dd))))

    # duplicates
    bynorm = collections.defaultdict(list)
    for t in recs:
        bynorm[t[3]].append(t)
    survivors = []
    for k, grp in bynorm.items():
        if len(grp) == 1:
            survivors.append(grp[0]); continue
        grp.sort(key=lambda t: (-t[4], -t[5]))
        survivors.append(grp[0])
        for t in grp[1:]:
            removed.append((t[0], t[1], 'duplicate', 'duplicate of %s' % grp[0][2]))

    # clusters
    byclu = collections.defaultdict(list)
    for t in survivors:
        byclu[cluster_key(t[2])].append(t)
    survivors2 = []
    for k, grp in byclu.items():
        if len(grp) == 1:
            survivors2.append(grp[0]); continue
        grp.sort(key=lambda t: (-t[4], -t[5]))
        survivors2.append(grp[0])
        for t in grp[1:]:
            removed.append((t[0], t[1], 'cluster', 'transliteration variant of %s' % grp[0][2]))

    survivors2.sort(key=lambda t: (-t[4], t[2]))
    keep_n = min(TARGET[c], len(survivors2))
    kept = survivors2[:keep_n]
    for t in survivors2[keep_n:]:
        removed.append((t[0], t[1], 'not-famous',
                        'absent from real name-frequency dataset / below fame cut-off (%.1f)' % t[4]))

    reasons = collections.Counter(r[2] for r in removed)
    report[c] = {'total': len(files), 'kept': len(kept), 'removed': len(removed),
                 'reasons': dict(reasons),
                 'cutoff': kept[-1][4] if kept else None,
                 'kept_in_dataset': sum(1 for t in kept if t[4] > 0)}
    all_removed += [(c, r[0], r[1], r[2], r[3]) for r in removed]
    all_kept += [(c, t[0], t[1], t[4]) for t in kept]
    print('done', c, flush=True)

print(json.dumps(report, indent=2))
print('TOTAL kept:', len(all_kept), '| removed:', len(all_removed))

json.dump([{'culture': c, 'path': p, 'file': b, 'reason': r, 'detail': d}
           for c, p, b, r, d in all_removed], open('/workspace/removed.json', 'w'), indent=1)
json.dump([{'culture': c, 'path': p, 'file': b, 'fame': s} for c, p, b, s in all_kept],
          open('/workspace/kept.json', 'w'), indent=1)
open('/workspace/remove_paths.txt', 'w').write('\n'.join(p for c, p, b, r, d in all_removed))
print('wrote manifests')
