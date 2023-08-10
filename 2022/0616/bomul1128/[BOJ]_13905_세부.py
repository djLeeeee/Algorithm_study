from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def find(idx):
    if idx == parents[idx]:
        return idx
    parents[idx] = find(parents[idx])
    return parents[idx]


def union(idx, adj):
    idx = find(idx)
    adj = find(adj)
    parents[adj] = idx


n, m = map(int, input().split())
s, e = map(int, input().split())
bridge = [(0, s, e)]
for _ in range(m):
    x, y, k = map(int, input().split())
    bridge.append((k, x, y))
bridge.sort()
parents = list(range(n + 1))
while find(s) != find(e):
    d, x, y = bridge.pop()
    if find(x) != find(y):
        union(x, y)
print(d)
