from sys import stdin

input = stdin.readline


def find(target):
    if parent[target] == target:
        return parent[target]
    parent[target] = find(parent[target])
    return parent[target]


n, m = map(int, input().split())
parent = list(range(n + 1))
c, *t = map(int, input().split())
if c == 0:
    print(m)
    exit()
mt = min(t)
for st in t:
    parent[st] = mt
party = [list(map(int, input().split())) for _ in range(m)]
for k, *l in party:
    for i in range(k - 1):
        pa, pb = find(l[i - 1]), find(l[i])
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb
ans = 0
mt = find(mt)
for _, a, *_ in party:
    if find(a) != mt:
        ans += 1
print(ans)
