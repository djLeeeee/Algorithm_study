from sys import stdin
from collections import defaultdict

input = stdin.readline


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    p = find(a)
    q = find(b)
    if p < q:
        parents[q] = p
    else:
        parents[p] = q
    return


case = 0
while True:
    n, m = map(int, input().split())
    ans = n
    if n == m == 0:
        break
    case += 1
    parents = list(range(n + 1))
    degree = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        degree[x] += 1
        degree[y] += 1
        union(x, y)
    ans = defaultdict(list)
    for i in range(1, n + 1):
        ans[find(i)].append(i)
    tree = 0
    for value in ans.values():
        total = 0
        for v in value:
            total += degree[v]
        total //= 2
        if total == len(value) - 1:
            tree += 1
    if tree > 1:
        print(f'Case {case}: A forest of {tree} trees.')
    elif tree == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
