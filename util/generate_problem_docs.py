"""
Generate docs/problems by difficulty level
Parses all README.md files and fetches problem info from solved.ac API
"""
import os
import re
import json
import time
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from collections import defaultdict

import requests

BOJ_URL = "https://www.acmicpc.net/problem"
SOLVED_AC_API = "https://solved.ac/api/v3"

# solved.ac level to tier mapping
TIERS = {
    0: ("Unrated", "unrated"),
    1: ("Bronze V", "bronze"), 2: ("Bronze IV", "bronze"), 3: ("Bronze III", "bronze"),
    4: ("Bronze II", "bronze"), 5: ("Bronze I", "bronze"),
    6: ("Silver V", "silver"), 7: ("Silver IV", "silver"), 8: ("Silver III", "silver"),
    9: ("Silver II", "silver"), 10: ("Silver I", "silver"),
    11: ("Gold V", "gold"), 12: ("Gold IV", "gold"), 13: ("Gold III", "gold"),
    14: ("Gold II", "gold"), 15: ("Gold I", "gold"),
    16: ("Platinum V", "platinum"), 17: ("Platinum IV", "platinum"), 18: ("Platinum III", "platinum"),
    19: ("Platinum II", "platinum"), 20: ("Platinum I", "platinum"),
    21: ("Diamond V", "diamond"), 22: ("Diamond IV", "diamond"), 23: ("Diamond III", "diamond"),
    24: ("Diamond II", "diamond"), 25: ("Diamond I", "diamond"),
    26: ("Ruby V", "ruby"), 27: ("Ruby IV", "ruby"), 28: ("Ruby III", "ruby"),
    29: ("Ruby II", "ruby"), 30: ("Ruby I", "ruby"),
}


@dataclass
class Problem:
    id: int
    title: str
    level: int
    tier_name: str
    tier_group: str
    study_dates: list[str]


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def find_all_readme_files(root: Path) -> list[Path]:
    """Find all README.md files in year folders"""
    readmes = []
    for year in ["2022", "2023", "2024", "2025", "2026"]:
        year_path = root / year
        if year_path.exists():
            readmes.extend(year_path.glob("*/README.md"))
    return sorted(readmes)


def extract_problem_ids(readme_path: Path) -> list[tuple[int, str]]:
    """Extract BOJ problem IDs from README.md file"""
    content = readme_path.read_text(encoding="utf-8")

    # Pattern: /problem/12345 in URLs
    pattern = r"acmicpc\.net/problem/(\d+)"
    matches = re.findall(pattern, content)

    # Get study date from path (e.g., 2022/0310 or 2023/20230104)
    parts = readme_path.parts
    year_idx = next(i for i, p in enumerate(parts) if p in ["2022", "2023", "2024", "2025", "2026"])
    year = parts[year_idx]
    date_str = parts[year_idx + 1]

    # Normalize date format to YYYY.MM.DD
    if len(date_str) == 4:  # MMDD format (2022 style)
        study_date = f"{year}.{date_str[:2]}.{date_str[2:]}"
    elif len(date_str) == 8:  # YYYYMMDD format (2023+ style)
        study_date = f"{date_str[:4]}.{date_str[4:6]}.{date_str[6:]}"
    else:
        study_date = f"{year}.{date_str}"

    return [(int(pid), study_date) for pid in matches]


def fetch_problem_info(problem_id: int) -> Optional[dict]:
    """Fetch problem info from solved.ac API"""
    url = f"{SOLVED_AC_API}/problem/show?problemId={problem_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"  Error fetching {problem_id}: {e}")
    return None


def fetch_problems_batch(problem_ids: list[int]) -> dict[int, dict]:
    """Fetch multiple problems using batch API"""
    results = {}
    # solved.ac API supports up to 100 problems at once
    batch_size = 100

    for i in range(0, len(problem_ids), batch_size):
        batch = problem_ids[i:i + batch_size]
        ids_str = ",".join(map(str, batch))
        url = f"{SOLVED_AC_API}/problem/lookup?problemIds={ids_str}"

        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                data = response.json()
                for problem in data:
                    results[problem["problemId"]] = problem
            else:
                print(f"  Batch API error: {response.status_code}")
        except Exception as e:
            print(f"  Error fetching batch: {e}")

        # Rate limiting
        if i + batch_size < len(problem_ids):
            time.sleep(0.5)

    return results


def generate_tier_markdown(tier_group: str, problems: list[Problem]) -> str:
    """Generate markdown content for a tier group"""
    tier_display = {
        "bronze": "Bronze",
        "silver": "Silver",
        "gold": "Gold",
        "platinum": "Platinum",
        "diamond": "Diamond",
        "ruby": "Ruby",
        "unrated": "Unrated",
    }

    lines = [
        f"# {tier_display[tier_group]} 문제 목록\n",
        f"총 {len(problems)}문제\n",
    ]

    # Group by specific tier (e.g., Silver I, Silver II)
    by_tier = defaultdict(list)
    for p in problems:
        by_tier[p.tier_name].append(p)

    # Sort tiers (higher tier first: I > II > III > IV > V)
    tier_order = ["I", "II", "III", "IV", "V"]
    sorted_tiers = sorted(
        by_tier.keys(),
        key=lambda t: tier_order.index(t.split()[-1]) if t.split()[-1] in tier_order else 99
    )

    for tier_name in sorted_tiers:
        tier_problems = sorted(by_tier[tier_name], key=lambda p: p.id)
        lines.append(f"\n## {tier_name}\n")
        lines.append("| 번호 | 제목 | 스터디 날짜 |")
        lines.append("|------|------|-------------|")

        for p in tier_problems:
            dates = ", ".join(sorted(set(p.study_dates)))
            lines.append(f"| [{p.id}]({BOJ_URL}/{p.id}) | {p.title} | {dates} |")

    return "\n".join(lines) + "\n"


def generate_index_markdown(all_problems: dict[str, list[Problem]]) -> str:
    """Generate index markdown with summary"""
    lines = [
        "# 백준 문제 모음 (2022-2026)\n",
        "알고리즘 스터디에서 풀었던 백준 문제들을 난이도별로 정리했습니다.\n",
        "## 요약\n",
        "| 난이도 | 문제 수 |",
        "|--------|---------|",
    ]

    tier_order = ["ruby", "diamond", "platinum", "gold", "silver", "bronze", "unrated"]
    tier_display = {
        "bronze": "Bronze",
        "silver": "Silver",
        "gold": "Gold",
        "platinum": "Platinum",
        "diamond": "Diamond",
        "ruby": "Ruby",
        "unrated": "Unrated",
    }

    total = 0
    for tier in tier_order:
        if tier in all_problems:
            count = len(all_problems[tier])
            total += count
            lines.append(f"| [{tier_display[tier]}](./{tier}.md) | {count} |")

    lines.append(f"| **합계** | **{total}** |")

    lines.append("\n## 바로가기\n")
    for tier in tier_order:
        if tier in all_problems:
            lines.append(f"- [{tier_display[tier]}](./{tier}.md)")

    return "\n".join(lines) + "\n"


def main():
    root = get_project_root()
    docs_dir = root / "docs"
    docs_dir.mkdir(exist_ok=True)

    print("Scanning README files...")
    readme_files = find_all_readme_files(root)
    print(f"Found {len(readme_files)} README files")

    # Collect all problem IDs with their study dates
    problem_dates: dict[int, list[str]] = defaultdict(list)
    for readme in readme_files:
        for pid, date in extract_problem_ids(readme):
            problem_dates[pid].append(date)

    unique_ids = list(problem_dates.keys())
    print(f"Found {len(unique_ids)} unique BOJ problems")

    # Fetch problem info from solved.ac
    print("Fetching problem info from solved.ac API...")
    problem_info = fetch_problems_batch(unique_ids)
    print(f"Fetched info for {len(problem_info)} problems")

    # Build Problem objects
    problems: list[Problem] = []
    for pid, dates in problem_dates.items():
        if pid in problem_info:
            info = problem_info[pid]
            level = info.get("level", 0)
            tier_name, tier_group = TIERS.get(level, ("Unrated", "unrated"))
            problems.append(Problem(
                id=pid,
                title=info.get("titleKo", f"Problem {pid}"),
                level=level,
                tier_name=tier_name,
                tier_group=tier_group,
                study_dates=dates,
            ))
        else:
            print(f"  Warning: No info for problem {pid}")

    # Group by tier
    by_tier: dict[str, list[Problem]] = defaultdict(list)
    for p in problems:
        by_tier[p.tier_group].append(p)

    # Generate markdown files
    print("Generating markdown files...")
    for tier_group, tier_problems in by_tier.items():
        filepath = docs_dir / f"{tier_group}.md"
        content = generate_tier_markdown(tier_group, tier_problems)
        filepath.write_text(content, encoding="utf-8")
        print(f"  Created {filepath.name} ({len(tier_problems)} problems)")

    # Generate index
    index_path = docs_dir / "README.md"
    index_content = generate_index_markdown(by_tier)
    index_path.write_text(index_content, encoding="utf-8")
    print(f"  Created README.md")

    print("\nDone! Check the docs/ folder.")


if __name__ == "__main__":
    main()
