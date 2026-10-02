import json, glob, os, collections, re, math, gzip, pickle, gc

CULTURES = ['islamic', 'christian', 'hindu']
TOTAL_TARGET = 19000

CORE = {
 'islamic': set('PK SA AE EG MY ID BD TR IR IQ KW QA BH OM JO LB SY DZ MA TN LY NG SD YE PS AF KZ UZ AZ BN MV GM SN ML NE TD SO DJ KM MR BF GN SL TG BJ CI AL BA XK MK KG TJ TM'.split()),
 'christian': set('US GB CA IE DE FR IT ES PL NL SE NO DK FI PT AT BE CH GR RU UA RO HU CZ SK HR RS BG LT LV EE AU NZ PH MX BR AR CO CL PE VE EC GT CU DO PR ZA GH KE TZ UG ZM ZW CM ET NG AO MZ MG RW BI LS SZ NA BW'.split()),
 'hindu': set('IN NP MU SG MY AE KW QA BH OM SA GB US CA AU NZ ZA TT FJ GY SR ID BD LK MM KE TZ UG YT RE GP MQ'.split()),
}

print('loading ...', flush=True)
ND = pickle.load(gzip.open('/workspace/data/fn.pkl.gz', 'rb'))
SCORE = {}
for c in CULTURES:
    core = CORE[c]; tbl = {}
    for k, v in ND.items():
        rk = v.get('rank')
        if not rk: continue
        rel = [r for cc, r in rk.items() if cc in core]
        best_rel = min(rel) if rel else None
        best_all = min(rk.values()); n_all = len(rk)
        s = 0.0
        if best_rel is not None:
            s += 70.0 * (1.0 - min(1.0, math.log10(max(best_rel, 1)) / 3.0))
        else:
            s += 25.0 * (1.0 - min(1.0, math.log10(max(best_all, 1)) / 3.0))
        s += min(n_all, 25) * 1.2
        tbl[k.lower()] = round(s, 2)
    SCORE[c] = tbl
del ND; gc.collect()
print('score tables ready', flush=True)

def norm_name(n): return re.sub(r'[^a-z0-9]', '', str(n).lower())

def cluster_key(n):
    s = re.sub(r'[^a-z]', '', str(n).lower())
    s = re.sub(r'(.)\1+', r'\1', s)
    s = re.sub(r'(ah|eh)$', 'a', s)
    s = re.sub(r'(ee|ie)$', 'i', s)
    s = re.sub(r'(oo|ou)$', 'u', s)
    s = re.sub(r'y$', 'i', s)
    s = re.sub(r'h$', '', s)
    return s

# force-keep the 100 source records that already have upgraded counterparts
FORCE = set()
for f in glob.glob('upgrading/names_upgraded/islamic/*.json'):
    try:
        d = json.load(open(f))
        FORCE.add(norm_name(d['data'].get('name')))
    except Exception:
        pass
print('force-keep (upgraded sources):', len(FORCE), flush=True)

stage = {}
for c in CULTURES:
    tbl = SCORE[c]
    recs = []; removed = []
    for f in sorted(glob.glob('upgrading/names/%s/*.json' % c)):
        b = os.path.basename(f)
        if b.startswith('_'):
            removed.append((f, b, 'invalid', 'non-record index file')); continue
        try: d = json.load(open(f))
        except Exception:
            removed.append((f, b, 'invalid', 'unparseable JSON')); continue
        if not isinstance(d, dict) or not isinstance(d.get('data'), dict):
            removed.append((f, b, 'invalid', 'not a name record')); continue
        dd = d['data']
        nm = str(dd.get('name') or '').strip(); sl = str(dd.get('slug') or '').strip()
        if not nm or not re.fullmatch(r'[a-z0-9_-]+', sl):
            removed.append((f, b, 'invalid', 'malformed slug or empty name')); continue
        nn = norm_name(nm)
        recs.append((f, b, nm, nn, tbl.get(nn, 0.0), len(json.dumps(dd))))

    # duplicates
    bynorm = collections.defaultdict(list)
    for t in recs: bynorm[t[3]].append(t)
    s1 = []
    for k, grp in bynorm.items():
        if len(grp) == 1: s1.append(grp[0]); continue
        grp.sort(key=lambda t: (-t[4], -t[5])); s1.append(grp[0])
        for t in grp[1:]:
            removed.append((t[0], t[1], 'duplicate', 'duplicate of %s' % grp[0][2]))

    # clusters: ONLY merge when at least one form is NOT independently attested
    byclu = collections.defaultdict(list)
    for t in s1: byclu[cluster_key(t[2])].append(t)
    s2 = []
    for k, grp in byclu.items():
        if len(grp) == 1: s2.append(grp[0]); continue
        attested = [t for t in grp if t[4] > 0]
        if len(attested) > 1:
            s2.extend(grp)          # distinct real names -> keep all
            continue
        grp.sort(key=lambda t: (-t[4], -t[5])); s2.append(grp[0])
        for t in grp[1:]:
            removed.append((t[0], t[1], 'cluster', 'transliteration variant of %s' % grp[0][2]))

    s2.sort(key=lambda t: (-t[4], t[2]))
    stage[c] = (s2, removed)
    print('  %s: pool after dedup/cluster = %d (attested %d)' % (
        c, len(s2), sum(1 for t in s2 if t[4] > 0)), flush=True)

# allocate 19000 across the ATTESTED pools, proportionally
att = {c: sum(1 for t in stage[c][0] if t[4] > 0) for c in CULTURES}
tot_att = sum(att.values())
alloc = {c: min(att[c], int(round(TOTAL_TARGET * att[c] / tot_att))) for c in CULTURES}
print('attested pools:', att, '| alloc:', alloc, '| sum', sum(alloc.values()), flush=True)

report = {}; all_removed = []; all_kept = []
for c in CULTURES:
    s2, removed = stage[c]
    keep_n = alloc[c]
    kept = s2[:keep_n]
    for t in s2[keep_n:]:
        why = ('absent from real name-frequency dataset' if t[4] == 0
               else 'below fame cut-off (%.1f)' % t[4])
        removed.append((t[0], t[1], 'not-famous', why))
    # force-keep upgraded sources
    keptn = {t[3] for t in kept}
    for t in s2[keep_n:]:
        if t[3] in FORCE and t[3] not in keptn:
            kept.append(t); keptn.add(t[3])
            removed = [r for r in removed if r[0] != t[0]]
    reasons = collections.Counter(r[2] for r in removed)
    report[c] = {'total': len(glob.glob('upgrading/names/%s/*.json' % c)),
                 'kept': len(kept), 'removed': len(removed), 'reasons': dict(reasons),
                 'attested_pool': att[c],
                 'kept_attested': sum(1 for t in kept if t[4] > 0),
                 'cutoff': min((t[4] for t in kept), default=None)}
    all_removed += [(c, r[0], r[1], r[2], r[3]) for r in removed]
    all_kept += [(c, t[0], t[1], t[4]) for t in kept]

print(json.dumps(report, indent=2))
print('TOTAL kept:', len(all_kept), '| removed:', len(all_removed))
json.dump([{'culture': c, 'path': p, 'file': b, 'reason': r, 'detail': d}
           for c, p, b, r, d in all_removed], open('/workspace/removed.json', 'w'), indent=1)
json.dump([{'culture': c, 'path': p, 'file': b, 'fame': s} for c, p, b, s in all_kept],
          open('/workspace/kept.json', 'w'), indent=1)
open('/workspace/remove_paths.txt', 'w').write('\n'.join(p for c, p, b, r, d in all_removed))
print('wrote manifests')
