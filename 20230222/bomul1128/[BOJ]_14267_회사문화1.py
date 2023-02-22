from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
root = 0
for i, j in enumerate(arr):
    if j != -1:
        tree[j].append(i + 1)
    else:
        root = i + 1
val = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    val[u] += v
ans = [0] * (n + 1)
point = [root]
for idx in point:
    ans[idx] += val[idx]
    for adj in tree[idx]:
        ans[adj] += ans[idx]
        point.append(adj)
print(*ans[1:])
