from sys import stdin

input = stdin.readline


def get_distance(idx, adj):
    result = (xy[idx][0] - xy[adj][0]) ** 2 + (xy[idx][1] - xy[adj][1]) ** 2
    return result ** 0.5


def find(target):
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]


n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
dist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist.append((get_distance(i, j), i, j))
dist.sort(reverse=True)
parent = list(range(n))
edge = 0
for _ in range(m):
    x, y = map(lambda k: find(int(k) - 1), input().split())
    if x != y:
        edge += 1
        parent[x] = y
ans = 0
while edge < n - 1:
    d, x, y = dist.pop()
    x, y = find(x), find(y)
    if x != y:
        edge += 1
        parent[x] = y
        ans += d
print('{0:.2f}'.format(ans))
