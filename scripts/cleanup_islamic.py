#!/usr/bin/env python3
"""Clean up Islamic variant clusters and similar-sounding-name references.

The real data in this repo is a directory of per-name JSON files under
upgrading/names/islamic. The script reads a single backup file created from that
source and performs only the two requested changes: cluster trimming and
similar_sounding_names cleanup.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

MAX_PER_CLUSTER = 3
DEFAULT_ROUTE_PREFIX = "/names/islamic"
STOPWORDS = {"the", "a", "an", "of", "and", "or", "who", "one", "is", "to", "in", "with", "for"}
PLACEHOLDERS = {"", "unknown", "n/a", "na", "none", "null", "nil", "not available", "tbd", "todo"}


def load_dataset(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return [dict(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        if isinstance(data.get("data"), list):
            return [dict(item) for item in data["data"] if isinstance(item, dict)]
        if isinstance(data.get("data"), dict):
            return [dict(data["data"])]
        return [dict(data)]
    raise ValueError(f"Unsupported dataset format: {path}")


def write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def slug_of(entry: Dict[str, Any]) -> str:
    value = entry.get("slug")
    if value is None:
        return ""
    return str(value).strip()


def name_of(entry: Dict[str, Any]) -> str:
    value = entry.get("name")
    if value is None:
        return ""
    return str(value).strip()


def parse_gender(value: Any) -> str:
    if value is None:
        return "u"
    s = str(value).strip().lower()
    s = s.replace("(female)", "female").replace("(male)", "male")
    if "/" in s or " or " in s:
        return "u"
    s = re.sub(r"[^a-z]", "", s)
    if s in {"female", "girl"}:
        return "f"
    if s in {"male", "masculine", "boy"}:
        return "m"
    if s in {"unisex", "neutral"}:
        return "u"
    return "u"


def genders_compatible(a: str, b: str) -> bool:
    if a == "u" or b == "u":
        return True
    return a == b


def spelling_key(name: Any) -> str:
    s = str(name or "").lower()
    s = re.sub(r"[^a-z]", "", s)
    s = re.sub(r"(.)\1+", r"\1", s)
    replacements = [
        ("kh", "k"), ("gh", "g"), ("sh", "s"), ("th", "t"), ("dh", "d"),
        ("zh", "z"), ("ph", "f"), ("q", "k"), ("w", "v"), ("oo", "u"),
        ("ou", "u"), ("ee", "i"), ("ea", "i"), ("ie", "i"), ("y", "i"),
        ("j", "z"), ("c", "k"), ("e", "i"), ("o", "u"),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    for suffix in ("atun", "aat", "at", "un"):
        if s.endswith(suffix):
            s = s[: -len(suffix)]
            break
    if s.endswith("ah"):
        s = s[:-2] + "a"
    elif s.endswith("a"):
        s = s[:-1] + "a"
    if s.endswith("h"):
        s = s[:-1]
    return s


def meaningful_words(value: Any) -> Set[str]:
    if value is None:
        return set()
    words = re.findall(r"[a-z]+", str(value).lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 1}


def share_meaning(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
    left = meaningful_words(a.get("short_meaning"))
    right = meaningful_words(b.get("short_meaning"))
    return bool(left and right and left & right)


def feature_standard_score(name: str) -> int:
    lowered = name.lower()
    score = 0
    if not re.search(r"[aeiou]{2,}", lowered):
        score += 1
    if "'" not in name:
        score += 1
    return score


def placeholder_count(entry: Dict[str, Any]) -> int:
    total = 0
    for key, value in entry.items():
        if key in {"name_variations", "similar_sounding_names"}:
            continue
        if isinstance(value, dict):
            total += placeholder_count(value)
        elif isinstance(value, list):
            if not value:
                total += 1
        elif value is None:
            total += 1
        elif isinstance(value, str) and (value.strip() == "" or value.strip().lower() in PLACEHOLDERS):
            total += 1
    return total


def cluster_rank(entry: Dict[str, Any]) -> tuple:
    name = name_of(entry)
    pop = float(entry.get("popularity_score") or 0.0)
    return (
        -pop,
        -feature_standard_score(name),
        len(name),
        placeholder_count(entry),
        name.lower(),
        slug_of(entry),
    )


def dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    result: List[str] = []
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(text)
    return result


def load_source_entries(source_dir: Path) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    for child in sorted(source_dir.glob("*.json")):
        with child.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        if isinstance(obj, dict):
            if isinstance(obj.get("data"), dict):
                entries.append(dict(obj["data"]))
            else:
                entries.append(dict(obj))
        elif isinstance(obj, list):
            entries.extend(dict(item) for item in obj if isinstance(item, dict))
    return entries


def build_clusters(entries: List[Dict[str, Any]]) -> List[List[int]]:
    dup_slugs = {slug for slug, count in Counter(slug_of(entry) for entry in entries if slug_of(entry)).items() if count > 1}
    parent = list(range(len(entries)))
    rank = [0] * len(entries)

    buckets: Dict[str, List[int]] = defaultdict(list)
    for idx, entry in enumerate(entries):
        if slug_of(entry) in dup_slugs:
            continue
        name = entry.get("name")
        if not name:
            continue
        buckets[spelling_key(name)].append(idx)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1

    for bucket_indices in buckets.values():
        for i in range(len(bucket_indices)):
            left_idx = bucket_indices[i]
            left = entries[left_idx]
            for j in range(i + 1, len(bucket_indices)):
                right_idx = bucket_indices[j]
                right = entries[right_idx]
                if not left.get("name") or not right.get("name"):
                    continue
                if not share_meaning(left, right):
                    continue
                if not genders_compatible(parse_gender(left.get("gender")), parse_gender(right.get("gender"))):
                    continue
                union(left_idx, right_idx)

    groups: Dict[int, List[int]] = defaultdict(list)
    for idx in range(len(entries)):
        groups[find(idx)].append(idx)
    return [cluster for cluster in groups.values() if cluster]


def cluster_trimmed_entries(entries: List[Dict[str, Any]]) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, str]]:
    clusters = build_clusters(entries)
    kept: List[Dict[str, Any]] = []
    removed: List[Dict[str, Any]] = []
    redirect_map: Dict[str, str] = {}
    kept_slugs: Set[str] = set()

    # Keep entries outside any cluster in their original order.
    cluster_member_indexes = {idx for cluster in clusters for idx in cluster}
    for idx, entry in enumerate(entries):
        if idx not in cluster_member_indexes:
            kept.append(dict(entry))
            kept_slugs.add(slug_of(entry))

    for cluster in clusters:
        cluster_entries = [entries[idx] for idx in cluster]
        if len(cluster_entries) <= MAX_PER_CLUSTER:
            for entry in cluster_entries:
                kept.append(dict(entry))
                kept_slugs.add(slug_of(entry))
            continue
        ranked = sorted(cluster_entries, key=cluster_rank)
        keepers = ranked[:MAX_PER_CLUSTER]
        for entry in keepers:
            kept.append(dict(entry))
            kept_slugs.add(slug_of(entry))
        redirect_target = slug_of(keepers[0])
        for entry in ranked[MAX_PER_CLUSTER:]:
            removed_slug = slug_of(entry)
            removed.append({
                "removed_slug": removed_slug,
                "removed_name": name_of(entry) or removed_slug,
                "redirect_to_slug": redirect_target,
                "cluster_size": len(cluster_entries),
            })
            redirect_map[removed_slug] = redirect_target

    final_kept: List[Dict[str, Any]] = []
    seen = set()
    for entry in kept:
        slug = slug_of(entry)
        if slug and slug in seen:
            continue
        seen.add(slug)
        final_kept.append(dict(entry))

    for item in removed:
        redirect_target = item["redirect_to_slug"]
        target_entry = next((entry for entry in final_kept if slug_of(entry) == redirect_target), None)
        if target_entry is None:
            continue
        names = target_entry.get("name_variations") or []
        if not isinstance(names, list):
            names = []
        additions = dedupe_preserve_order(names)
        removed_name = str(item.get("removed_name") or "").strip()
        if removed_name and removed_name.lower() not in {n.lower() for n in additions}:
            additions.append(removed_name)
        target_entry["name_variations"] = dedupe_preserve_order(additions)

    final_kept = sorted(final_kept, key=lambda e: next((idx for idx, orig in enumerate(entries) if slug_of(orig) == slug_of(e)), len(entries)))
    return final_kept, removed, redirect_map


def remap_similar_sounding_names(entries: List[Dict[str, Any]], redirect_map: Dict[str, str], valid_slugs: Set[str]) -> None:
    for entry in entries:
        names = entry.get("similar_sounding_names") or []
        if not isinstance(names, list):
            entry["similar_sounding_names"] = []
            continue
        rebuilt: List[str] = []
        seen: Set[str] = set()
        for raw in names:
            if not isinstance(raw, str):
                continue
            value = raw.strip()
            if not value:
                continue
            mapped = redirect_map.get(value, value)
            if mapped not in valid_slugs:
                continue
            if mapped == slug_of(entry):
                continue
            lower = mapped.lower()
            if lower in seen:
                continue
            seen.add(lower)
            rebuilt.append(mapped)
        entry["similar_sounding_names"] = rebuilt


def validate(entries_before: List[Dict[str, Any]], entries_after: List[Dict[str, Any]], removed: List[Dict[str, Any]], valid_slugs: Set[str]) -> tuple[bool, Dict[str, int]]:
    counts = {
        "before": len(entries_before),
        "after": len(entries_after),
        "removed": len(removed),
    }
    print(f"Entries before: {counts['before']}")
    print(f"Entries after: {counts['after']}")
    print(f"Removed entries: {counts['removed']}")

    largest_cluster = max((len(cluster) for cluster in build_clusters(entries_after)), default=0)
    print(f"Largest cluster size after cleanup: {largest_cluster}")
    dangling = 0
    for entry in entries_after:
        for link in entry.get("similar_sounding_names") or []:
            if link not in valid_slugs:
                dangling += 1
    print(f"Dangling similar_sounding_names entries: {dangling}")

    redirect_targets = {item["removed_slug"]: item["redirect_to_slug"] for item in removed}
    for removed_slug, target in redirect_targets.items():
        occurrences = sum(1 for item in removed if item["removed_slug"] == removed_slug)
        if occurrences != 1:
            print(f"FAIL: removed slug has non-unique redirect: {removed_slug}")
        if target == removed_slug:
            print(f"FAIL: redirect target is itself removed: {removed_slug} -> {target}")
        if target in redirect_targets:
            print(f"FAIL: redirect target is also removed: {target}")
    if any(item["redirect_to_slug"] in redirect_targets for item in removed):
        print("FAIL: redirect target is removed")

    non_variant_changes = 0
    var_changed = 0
    similar_changed = 0
    before_by_slug = {slug_of(entry): entry for entry in entries_before}
    for entry in entries_after:
        slug = slug_of(entry)
        original = before_by_slug.get(slug)
        if original is None:
            continue
        for key, value in original.items():
            if key in {"name_variations", "similar_sounding_names"}:
                continue
            if entry.get(key) != value:
                non_variant_changes += 1
                break
        if entry.get("name_variations") != original.get("name_variations"):
            var_changed += 1
        if entry.get("similar_sounding_names") != original.get("similar_sounding_names"):
            similar_changed += 1

    print(f"Entries with non-variant field changes: {non_variant_changes}")
    print(f"Entries with name_variations changed: {var_changed}")
    print(f"Entries with similar_sounding_names changed: {similar_changed}")

    ok = largest_cluster <= MAX_PER_CLUSTER and dangling == 0 and non_variant_changes == 0
    if ok:
        print("VALIDATION: PASS")
    else:
        print("VALIDATION: FAIL")
    return ok, counts


def print_examples(before_entries: List[Dict[str, Any]], after_entries: List[Dict[str, Any]]) -> None:
    print("\nRandom cluster before/after examples (15):")
    clusters = build_clusters(before_entries)
    sample_clusters = random.sample(clusters, min(15, len(clusters))) if clusters else []
    for cluster in sample_clusters:
        before_slugs = [slug_of(before_entries[idx]) for idx in cluster]
        after_slugs = [slug_of(entry) for entry in after_entries if slug_of(entry) in before_slugs]
        print({"before": before_slugs, "after": after_slugs})

    print("\nRandom similar_sounding_names before/after examples (10):")
    sample_entries = random.sample(after_entries, min(10, len(after_entries))) if after_entries else []
    for entry in sample_entries:
        before_entry = next((item for item in before_entries if slug_of(item) == slug_of(entry)), None)
        print({
            "slug": slug_of(entry),
            "before": (before_entry or {}).get("similar_sounding_names", []),
            "after": entry.get("similar_sounding_names", []),
        })


def main() -> int:
    parser = argparse.ArgumentParser(description="Trim Islamic spelling variant clusters and fix similar_sounding_names links.")
    parser.add_argument("--input", type=Path, default=Path("islamic.backup.json"), help="JSON file with the original dataset backup.")
    parser.add_argument("--source-dir", type=Path, default=Path("upgrading/names/islamic"), help="Directory of Islamic name JSON files if backup is missing.")
    parser.add_argument("--route-prefix", default=DEFAULT_ROUTE_PREFIX, help="Base route prefix used in redirects (default: /names/islamic).")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run by default; use --apply to write the cleaned dataset.")
    parser.add_argument("--apply", action="store_true", help="Write the final cleaned dataset and redirect files.")
    args = parser.parse_args()

    source_dir = args.source_dir.resolve()
    backup_path = args.input.resolve()
    if not backup_path.exists() and source_dir.exists():
        entries = load_source_entries(source_dir)
        write_json(backup_path, entries)
        print(f"Backup created: {backup_path} ({len(entries)} entries)")

    if not backup_path.exists():
        print(f"Missing input dataset: {backup_path}", file=sys.stderr)
        return 2

    original = load_dataset(backup_path)
    if not original:
        print("Dataset is empty.", file=sys.stderr)
        return 2

    cleaned, removed, redirect_map = cluster_trimmed_entries(original)
    valid_slugs = {slug_of(entry) for entry in cleaned}
    remap_similar_sounding_names(cleaned, redirect_map, valid_slugs)

    ok, counts = validate(original, cleaned, removed, valid_slugs)
    print_examples(original, cleaned)

    if not args.apply:
        print("\n--dry-run: no dataset file changes were written.")
        return 0 if ok else 1

    write_json(backup_path, cleaned)
    out_dir = Path("scripts/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "removed_names.json", removed)
    lines = [f"{args.route_prefix}/{item['removed_slug']} {args.route_prefix}/{item['redirect_to_slug']} 301" for item in removed]
    (out_dir / "redirects.txt").write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(f"\nApplied cleanup to {backup_path}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
