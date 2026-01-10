"""
README.md generator
"""
from typing import Optional

BOJ = "https://www.acmicpc.net"
ENDPOINT = "https://solved.ac/api/v3"


def makeTimestamp(study_day: int = 4) -> str:
    from datetime import date, timedelta

    today = date.today()
    delta = (study_day - today.isoweekday()) % 7
    next_day = today + timedelta(days=delta if delta else 7)
    return next_day.__str__().replace('-', '')


def wrapper(idx: int) -> Optional[str]:
    import requests
    import json

    url = f"{ENDPOINT}/problem/show?problemId={idx}"
    response = json.loads(requests.get(
        url=url
    ).content)
    if not isinstance(response, dict):
        return None
    if (title := response.get('titleKo')) is None:
        return None
    return f'- [백준 {idx} {title}]({BOJ}/problem/{idx})\n'


def main():
    import os

    stamp = makeTimestamp()
    problems: list[int] = []
    # TODO change to argument
    while True:
        n = input(
            "Problem ID?"
        )
        if not n.isdigit():
            break
        problems.append(int(n))

    filename = f"2026/{stamp}/README.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(file=filename, mode="w", encoding="utf-8") as readme:
        readme.write(f"# {stamp} 알고리즘 스터디 문제\n\n")
        for problem in problems:
            readme.write(wrapper(problem))
        readme.close()
    print(f"README.md generated successfully!", flush=True)


if __name__ == "__main__":
    main()
