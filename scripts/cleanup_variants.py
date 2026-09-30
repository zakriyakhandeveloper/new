#!/usr/bin/env python3
"""Trim variant clusters and repair similar_sounding_names for a baby-name dataset.

This script is intentionally conservative and only edits:
  1) name_variations on kept records when extra variant pages are removed
  2) similar_sounding_names links after cluster trimming

No other fields, names, slugs, genders, or text are changed.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple

MAX_PER_CLUSTER = 3
STOPWORDS = {"the", "a", "an", "of", "and", "or", "who", "one", "is", "to", "in", "with", "for"}
DATASET_CONFIG = {
    "christian": {
        "source_dir": "upgrading/names/christian",
        "backup": "christian.backup.json",
        "route_prefix": "/names/christian",
    },
    "hindu": {
        "source_dir": "upgrading/names/hindu",
        "backup": "hindu.backup.json",
        "route_prefix": "/names/hindu",
    },
}


def write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def load_source_entries(source_dir: Path) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    for child in sorted(source_dir.glob("*.json")):
        if child.name.startswith("_"):
            continue
        try:
            with child.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            nested = data.get("data")
            if isinstance(nested, dict):
                entries.append(dict(nested))
                continue
            if isinstance(nested, list):
                for item in nested:
                    if isinstance(item, dict):
                        entries.append(dict(item))
                continue
            if "slug" in data:
                entries.append(dict(data))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    entries.append(dict(item))
    return entries


def load_dataset(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, list):
        return [dict(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        nested = data.get("data")
        if isinstance(nested, list):
            return [dict(item) for item in nested if isinstance(item, dict)]
        if isinstance(nested, dict):
            return [dict(nested)]
        if "slug" in data or any(k in data for k in ("name", "gender", "short_meaning")):
            return [dict(data)]
    raise ValueError(f"Unsupported dataset format in {path}")


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
    text = str(value).strip().lower()
    text = text.replace("(female)", "female").replace("(male)", "male")
    if "/" in text or " or " in text:
        return "u"
    letters = re.sub(r"[^a-z]", "", text)
    if letters in {"female", "girl", "feminine"}:
        return "f"
    if letters in {"male", "masculine", "boy"}:
        return "m"
    if letters in {"unisex", "neutral"}:
        return "u"
    return "u"


def genders_compatible(a: str, b: str) -> bool:
    return a == "u" or b == "u" or a == b


def spelling_key(name: Any) -> str:
    s = str(name or "").strip().lower()
    s = re.sub(r"[^a-z]", "", s)
    if len(s) < 3:
        return ""
    s = re.sub(r"(.)\1+", r"\1", s)
    replacements = [
        ("kh", "k"), ("gh", "g"), ("sh", "s"), ("ch", "c"), ("th", "t"),
        ("dh", "d"), ("zh", "z"), ("ph", "f"), ("q", "k"), ("w", "v"),
        ("oo", "u"), ("ou", "u"), ("ee", "i"), ("ea", "i"), ("ie", "i"),
        ("y", "i"), ("j", "z"), ("c", "k"), ("e", "i"), ("o", "u"),
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
    return {word for word in words if word not in STOPWORDS and len(word) > 1}


def share_meaning(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
    left = meaningful_words(a.get("short_meaning"))
    right = meaningful_words(b.get("short_meaning"))
    return bool(left and right and (left & right))


def feature_score(name: str) -> int:
    lowered = name.lower()
    score = 0
    if not re.search(r"[aeiou]{2,}", lowered):
        score += 1
    if "'" not in name:
        score += 1
    return score


def cluster_rank(entry: Dict[str, Any]) -> Tuple[float, int, int, str, str]:
    name = name_of(entry)
    popularity = float(entry.get("popularity_score") or 0.0)
    return (
        -popularity,
        -feature_score(name),
        -len(name),
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


def build_clusters(entries: List[Dict[str, Any]]) -> List[List[int]]:
    duplicate_slugs = {slug for slug, count in Counter(slug_of(entry) for entry in entries if slug_of(entry)).items() if count > 1}
    parent = list(range(len(entries)))
    rank = [0] * len(entries)

    buckets: Dict[str, List[int]] = defaultdict(list)
    for idx, entry in enumerate(entries):
        slug = slug_of(entry)
        if slug in duplicate_slugs:
            continue
        name = entry.get("name")
        short = entry.get("short_meaning")
        key = spelling_key(name)
        if not name or not short or not key:
            continue
        buckets[key].append(idx)

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return
        if rank[left_root] < rank[right_root]:
            parent[left_root] = right_root
        elif rank[left_root] > rank[right_root]:
            parent[right_root] = left_root
        else:
            parent[right_root] = left_root
            rank[left_root] += 1

    for bucket_indices in buckets.values():
        for i in range(len(bucket_indices)):
            left_idx = bucket_indices[i]
            left_entry = entries[left_idx]
            for j in range(i + 1, len(bucket_indices)):
                right_idx = bucket_indices[j]
                right_entry = entries[right_idx]
                if not left_entry.get("name") or not right_entry.get("name"):
                    continue
                if not left_entry.get("short_meaning") or not right_entry.get("short_meaning"):
                    continue
                if not share_meaning(left_entry, right_entry):
                    continue
                if not genders_compatible(parse_gender(left_entry.get("gender")), parse_gender(right_entry.get("gender"))):
                    continue
                union(left_idx, right_idx)

    groups: Dict[int, List[int]] = defaultdict(list)
    for idx in range(len(entries)):
        groups[find(idx)].append(idx)
    return [cluster for cluster in groups.values() if cluster]


def cluster_trimmed_entries(entries: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, str]]:
    clusters = build_clusters(entries)
    kept: List[Dict[str, Any]] = []
    removed: List[Dict[str, Any]] = []
    redirect_map: Dict[str, str] = {}
    cluster_member_indexes = {idx for cluster in clusters for idx in cluster}

    for idx, entry in enumerate(entries):
        if idx not in cluster_member_indexes:
            kept.append(dict(entry))

    for cluster in clusters:
        cluster_entries = [entries[idx] for idx in cluster]
        if len(cluster_entries) <= MAX_PER_CLUSTER:
            for entry in cluster_entries:
                kept.append(dict(entry))
            continue

        ranked = sorted(cluster_entries, key=cluster_rank)
        keepers = ranked[:MAX_PER_CLUSTER]
        for entry in keepers:
            kept.append(dict(entry))
        redirect_target = slug_of(keepers[0])
        for entry in ranked[MAX_PER_CLUSTER:]:
            removed_slug = slug_of(entry)
            removed_name = name_of(entry) or removed_slug
            removed.append({
                "removed_slug": removed_slug,
                "removed_name": removed_name,
                "redirect_to_slug": redirect_target,
                "cluster_size": len(cluster_entries),
            })
            redirect_map[removed_slug] = redirect_target

    final_kept: List[Dict[str, Any]] = []
    seen: Set[str] = set()
    for entry in kept:
        slug = slug_of(entry)
        if slug and slug in seen:
            continue
        if slug:
            seen.add(slug)
        final_kept.append(dict(entry))

    for item in removed:
        target_slug = item["redirect_to_slug"]
        target_entry = next((entry for entry in final_kept if slug_of(entry) == target_slug), None)
        if target_entry is None:
            continue
        existing = target_entry.get("name_variations") or []
        if not isinstance(existing, list):
            existing = []
        additions = dedupe_preserve_order(existing)
        removed_name = str(item.get("removed_name") or "").strip()
        if removed_name and removed_name.lower() not in {entry_name.lower() for entry_name in additions}:
            additions.append(removed_name)
        target_entry["name_variations"] = additions

    final_kept = sorted(final_kept, key=lambda entry: next((idx for idx, original in enumerate(entries) if slug_of(original) == slug_of(entry)), len(entries)))
    return final_kept, removed, redirect_map


def find_filler_lists(entries: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Counter[str] = Counter()
    for entry in entries:
        values = entry.get("similar_sounding_names") or []
        if not isinstance(values, list):
            continue
        for value in values:
            if isinstance(value, str):
                cleaned = value.strip()
                if cleaned:
                    counts[cleaned] += 1
    return {value: count for value, count in counts.items() if count >= 5}


def remap_similar_sounding_names(entries: List[Dict[str, Any]], redirect_map: Dict[str, str], valid_slugs: Set[str]) -> None:
    for entry in entries:
        value = entry.get("similar_sounding_names")
        if not isinstance(value, list):
            entry["similar_sounding_names"] = []
            continue

        rebuilt: List[str] = []
        seen: Set[str] = set()
        for raw in value:
            if not isinstance(raw, str):
                continue
            item = raw.strip()
            if not item:
                continue
            mapped = redirect_map.get(item, item)
            if mapped not in valid_slugs:
                continue
            if mapped == slug_of(entry):
                continue
            lowered = mapped.lower()
            if lowered in seen:
                continue
            seen.add(lowered)
            rebuilt.append(mapped)
        entry["similar_sounding_names"] = rebuilt


def validate(entries_before: List[Dict[str, Any]], entries_after: List[Dict[str, Any]], removed: List[Dict[str, Any]], valid_slugs: Set[str]) -> Tuple[bool, Dict[str, int]]:
    counts = {
        "before": len(entries_before),
        "after": len(entries_after),
        "removed": len(removed),
    }
    largest_cluster = max((len(cluster) for cluster in build_clusters(entries_after)), default=0)
    dangling = 0
    for entry in entries_after:
        for link in entry.get("similar_sounding_names") or []:
            if link not in valid_slugs:
                dangling += 1

    redirect_targets = {item["removed_slug"]: item["redirect_to_slug"] for item in removed}
    for removed_slug, target in redirect_targets.items():
        if target == removed_slug:
            print(f"FAIL: redirect target is itself removed: {removed_slug} -> {target}")
        if target in redirect_targets:
            print(f"FAIL: redirect target is also removed: {target}")

    non_variant_changes = 0
    before_by_slug = {slug_of(entry): entry for entry in entries_before}
    for entry in entries_after:
        original = before_by_slug.get(slug_of(entry))
        if original is None:
            continue
        for key, value in original.items():
            if key in {"name_variations", "similar_sounding_names"}:
                continue
            if entry.get(key) != value:
                non_variant_changes += 1
                break

    ok = largest_cluster <= MAX_PER_CLUSTER and dangling == 0 and non_variant_changes == 0
    counts.update({
        "largest_cluster": largest_cluster,
        "dangling_links": dangling,
        "non_variant_field_changes": non_variant_changes,
        "valid": 1 if ok else 0,
    })
    return ok, counts


def print_examples(before_entries: List[Dict[str, Any]], after_entries: List[Dict[str, Any]]) -> None:
    print("\nRandom cluster examples (15):")
    clusters = build_clusters(before_entries)
    sample_clusters = random.sample(clusters, min(15, len(clusters))) if clusters else []
    for cluster in sample_clusters:
        before_slugs = [slug_of(before_entries[idx]) for idx in cluster]
        after_slugs = [slug_of(entry) for entry in after_entries if slug_of(entry) in before_slugs]
        print({"before": before_slugs, "after": after_slugs})

    print("\nRandom similar_sounding_names examples (10):")
    sample_entries = random.sample(after_entries, min(10, len(after_entries))) if after_entries else []
    for entry in sample_entries:
        before_entry = next(
            (item for item in before_entries if slug_of(item) == slug_of(entry)),
            None,
        )
        print({
            "slug": slug_of(entry),
            "before": (before_entry or {}).get("similar_sounding_names", []),
            "after": entry.get("similar_sounding_names", []),
        })


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Trim variant clusters and repair similar_sounding_names for a baby-name dataset.")
    parser.add_argument("--dataset", choices=["christian", "hindu"], required=True, help="Dataset family to clean up.")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run output only (default).")
    parser.add_argument("--apply", action="store_true", help="Write the cleaned dataset back to disk.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = DATASET_CONFIG[args.dataset]
    repo_root = Path(__file__).resolve().parents[1]
    source_dir = (repo_root / config["source_dir"]).resolve()
    backup_path = (repo_root / config["backup"]).resolve()

    if not source_dir.exists():
        print(f"Missing dataset directory: {source_dir}", file=sys.stderr)
        return 2

    if not backup_path.exists():
        entries = load_source_entries(source_dir)
        write_json(backup_path, entries)
        print(f"Backup created: {backup_path} ({len(entries)} entries)")

    original = load_dataset(backup_path)
    cleaned, removed, redirect_map = cluster_trimmed_entries(original)
    valid_slugs = {slug_of(entry) for entry in cleaned}
    remap_similar_sounding_names(cleaned, redirect_map, valid_slugs)

    ok, counts = validate(original, cleaned, removed, valid_slugs)
    filler_report = find_filler_lists(cleaned)
    print(f"\nDataset: {args.dataset}")
    print(f"Entries before: {counts['before']}")
    print(f"Entries after: {counts['after']}")
    print(f"Removed entries: {counts['removed']}")
    print(f"Largest cluster size after cleanup: {counts.get('largest_cluster', 0)}")
    print(f"Dangling similar_sounding_names entries: {counts.get('dangling_links', 0)}")
    print(f"Entries with non-variant field changes: {counts.get('non_variant_field_changes', 0)}")
    print(f"Filler-list report: {filler_report if filler_report else 'none detected; no filler list cleared'}")
    print("VALIDATION: PASS" if ok else "VALIDATION: FAIL")
    print_examples(original, cleaned)

    if args.apply:
        write_json(backup_path, cleaned)
        print(f"\nApplied cleanup to {backup_path}")
        return 0 if ok else 1

    print("\n--dry-run: no dataset write performed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
