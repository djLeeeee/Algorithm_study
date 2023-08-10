from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def find(idx):
    if idx == parent[idx]:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = list(range(n + 1))
for _ in range(m):
    x, y = map(int, input().split())
    px, py = find(x), find(y)
    if cost[px - 1] < cost[py - 1]:
        parent[py] = px
    else:
        parent[px] = py
parent_set = set()
for i in range(1, n + 1):
    parent_set.add(find(i))
ans = sum([cost[j - 1] for j in parent_set])
if ans <= k:
    print(ans)
else:
    print("Oh no")
