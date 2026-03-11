#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

REPO_SLUG = "mistbind3u88/blogs"


@dataclass
class WorkItem:
    number: int
    title: str
    url: str
    body: str
    category: str
    when: str


def parse_dt(raw: Optional[str]) -> Optional[datetime]:
    if not raw:
        return None
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def run_gh(args: List[str]) -> list:
    completed = subprocess.run(["gh", *args], capture_output=True)
    if completed.returncode != 0:
        err = completed.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(f"gh command failed: {' '.join(args)}\n{err}")
    out = completed.stdout.decode("utf-8", errors="replace")
    return json.loads(out)


def run_gh_obj(args: List[str]) -> Any:
    completed = subprocess.run(["gh", *args], capture_output=True)
    if completed.returncode != 0:
        err = completed.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(f"gh command failed: {' '.join(args)}\n{err}")
    out = completed.stdout.decode("utf-8", errors="replace")
    return json.loads(out)


def normalize_category(title: str) -> str:
    m = re.match(r"^[a-zA-Z]+\(([^)]+)\)", title)
    if m:
        return m.group(1).lower()
    m = re.match(r"^([a-zA-Z]+):", title)
    if m:
        return m.group(1).lower()
    return "other"


def label_from_date(period_type: str, dt: datetime) -> str:
    if period_type == "monthly":
        return dt.strftime("%Y-%m")
    if period_type == "half-year":
        return f"{dt.year}-H{'1' if dt.month <= 6 else '2'}"
    if period_type == "yearly":
        return str(dt.year)
    raise ValueError(f"Unknown period_type: {period_type}")


def parse_label(period_type: str, label: str) -> Tuple[int, int]:
    if period_type == "monthly":
        m = re.fullmatch(r"(\d{4})-(\d{2})", label)
        if not m:
            raise ValueError(f"Invalid monthly label: {label}")
        y, mo = int(m.group(1)), int(m.group(2))
        if mo < 1 or mo > 12:
            raise ValueError(f"Invalid month label: {label}")
        return y, mo
    if period_type == "half-year":
        m = re.fullmatch(r"(\d{4})-H([12])", label)
        if not m:
            raise ValueError(f"Invalid half-year label: {label}")
        return int(m.group(1)), int(m.group(2))
    if period_type == "yearly":
        m = re.fullmatch(r"(\d{4})", label)
        if not m:
            raise ValueError(f"Invalid yearly label: {label}")
        return int(m.group(1)), 1
    raise ValueError(f"Unknown period_type: {period_type}")


def sort_key(period_type: str, label: str) -> int:
    y, idx = parse_label(period_type, label)
    if period_type == "monthly":
        return y * 12 + idx
    if period_type == "half-year":
        return y * 2 + idx
    return y


def prev_label(period_type: str, label: str) -> str:
    y, idx = parse_label(period_type, label)
    if period_type == "monthly":
        if idx == 1:
            return f"{y - 1}-12"
        return f"{y}-{idx - 1:02d}"
    if period_type == "half-year":
        if idx == 1:
            return f"{y - 1}-H2"
        return f"{y}-H1"
    return str(y - 1)


def pick_items(items: List[Dict[str, Any]], label: str, key: str) -> List[WorkItem]:
    out: List[WorkItem] = []
    for x in items:
        dt = parse_dt(x.get(key))
        if not dt:
            continue
        if x.get("_label") != label:
            continue
        out.append(
            WorkItem(
                number=x["number"],
                title=x.get("title", ""),
                url=x.get("url", ""),
                body=x.get("body", "") or "",
                category=normalize_category(x.get("title", "")),
                when=dt.isoformat(),
            )
        )
    out.sort(key=lambda i: i.when, reverse=True)
    return out


def pick_open_created(items: List[Dict[str, Any]], label: str) -> List[Dict[str, Any]]:
    out = []
    for x in items:
        if x.get("state") != "OPEN":
            continue
        if x.get("_created_label") != label:
            continue
        out.append(
            {
                "number": x["number"],
                "title": x.get("title", ""),
                "url": x.get("url", ""),
                "body": x.get("body", "") or "",
                "createdAt": x.get("createdAt"),
            }
        )
    out.sort(key=lambda i: i["number"])
    return out


def collect_pr_diff_once(merged_prs: List[WorkItem]) -> Dict[str, Any]:
    entries: List[Dict[str, Any]] = []
    incomplete_count = 0

    for pr in merged_prs:
        files = run_gh_obj(
            [
                "api",
                f"repos/{REPO_SLUG}/pulls/{pr.number}/files?per_page=100&page=1",
            ]
        )
        file_entries = []
        with_patch = 0
        without_patch = 0
        missing_patch_files: List[str] = []

        for f in files:
            patch = f.get("patch")
            has_patch = patch is not None
            if has_patch:
                with_patch += 1
            else:
                without_patch += 1
                missing_patch_files.append(f.get("filename"))

            file_entries.append(
                {
                    "filename": f.get("filename"),
                    "status": f.get("status"),
                    "additions": f.get("additions"),
                    "deletions": f.get("deletions"),
                    "changes": f.get("changes"),
                    "has_patch": has_patch,
                    "patch": patch,
                }
            )

        possible_more_files = len(files) >= 100
        reasons: List[str] = []
        if possible_more_files:
            reasons.append("possible_more_files")
        if without_patch > 0:
            reasons.append("some_files_have_no_patch")

        incomplete = len(reasons) > 0
        if incomplete:
            incomplete_count += 1

        entries.append(
            {
                "pr_number": pr.number,
                "pr_title": pr.title,
                "pr_url": pr.url,
                "fetch_mode": "single_request",
                "api_endpoint": f"/repos/{REPO_SLUG}/pulls/{pr.number}/files?per_page=100&page=1",
                "files_returned": len(files),
                "possible_more_files": possible_more_files,
                "patch_coverage": {
                    "with_patch": with_patch,
                    "without_patch": without_patch,
                    "missing_patch_files": missing_patch_files,
                },
                "incomplete": incomplete,
                "incomplete_reasons": reasons,
                "files": file_entries,
            }
        )

    return {
        "fetch_policy": "single_request_per_pr",
        "note": "PRごとに files API を1回だけ取得。取り切れない可能性は各PRの incomplete で判定。",
        "prs_total": len(merged_prs),
        "prs_incomplete": incomplete_count,
        "entries": entries,
    }


def build_period_json(
    period_type: str,
    label: str,
    issues: List[Dict[str, Any]],
    prs: List[Dict[str, Any]],
    include_pr_diff: bool,
) -> Dict[str, Any]:
    prev = prev_label(period_type, label)

    closed_issues = pick_items(issues, label, "closedAt")
    merged_prs = pick_items(prs, label, "mergedAt")
    prev_closed_issues = pick_items(issues, prev, "closedAt")
    prev_merged_prs = pick_items(prs, prev, "mergedAt")

    open_issues = pick_open_created(issues, label)
    open_prs = pick_open_created(prs, label)

    categories: Dict[str, int] = {}
    for item in [*closed_issues, *merged_prs]:
        categories[item.category] = categories.get(item.category, 0) + 1

    sorted_categories = sorted(categories.items(), key=lambda kv: kv[1], reverse=True)

    issues_count = len(closed_issues)
    prs_count = len(merged_prs)
    total_count = issues_count + prs_count

    prev_issues_count = len(prev_closed_issues)
    prev_prs_count = len(prev_merged_prs)
    prev_total_count = prev_issues_count + prev_prs_count

    result: Dict[str, Any] = {
        "period_type": period_type,
        "label": label,
        "compare_to": prev,
        "counts": {
            "issues_closed": issues_count,
            "prs_merged": prs_count,
            "completed_total": total_count,
            "delta": {
                "issues_closed": issues_count - prev_issues_count,
                "prs_merged": prs_count - prev_prs_count,
                "completed_total": total_count - prev_total_count,
            },
        },
        "categories": [
            {"name": name, "count": count} for name, count in sorted_categories
        ],
        "open_created_in_period": {
            "issues": open_issues,
            "prs": open_prs,
        },
        "samples": {
            "issues": [asdict(x) for x in closed_issues[:5]],
            "prs": [asdict(x) for x in merged_prs[:5]],
        },
    }
    if include_pr_diff:
        result["pr_diff"] = collect_pr_diff_once(merged_prs)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect periodic summary data from GitHub")
    parser.add_argument("--period-type", choices=["monthly", "half-year", "yearly"], required=True)
    parser.add_argument("--label", help="Target label, e.g. 2026-03 / 2026-H1 / 2026")
    parser.add_argument("--out", help="Write JSON to file")
    parser.add_argument(
        "--skip-pr-diff",
        action="store_true",
        help="Skip PR file diff collection; by default patch/additions/deletions are included",
    )
    args = parser.parse_args()

    if not args.label:
        raise SystemExit("Specify --label")

    issues = run_gh(
        [
            "issue",
            "list",
            "--state",
            "all",
            "--limit",
            "500",
            "--json",
            "number,title,body,state,createdAt,closedAt,url",
        ]
    )
    prs = run_gh(
        [
            "pr",
            "list",
            "--state",
            "all",
            "--limit",
            "500",
            "--json",
            "number,title,body,state,createdAt,closedAt,mergedAt,url",
        ]
    )

    for x in issues:
        dt = parse_dt(x.get("closedAt"))
        x["_label"] = label_from_date(args.period_type, dt) if dt else None
        cdt = parse_dt(x.get("createdAt"))
        x["_created_label"] = label_from_date(args.period_type, cdt) if cdt else None

    for x in prs:
        dt = parse_dt(x.get("mergedAt"))
        x["_label"] = label_from_date(args.period_type, dt) if dt else None
        cdt = parse_dt(x.get("createdAt"))
        x["_created_label"] = label_from_date(args.period_type, cdt) if cdt else None

    parse_label(args.period_type, args.label)
    target_labels = [args.label]

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "period_type": args.period_type,
        "periods": [
            build_period_json(
                args.period_type,
                label,
                issues,
                prs,
                include_pr_diff=not args.skip_pr_diff,
            )
            for label in target_labels
        ],
    }

    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
    else:
        print(payload)


if __name__ == "__main__":
    main()
