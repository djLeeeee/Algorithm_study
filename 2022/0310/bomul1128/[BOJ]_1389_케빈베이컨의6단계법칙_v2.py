from sys import stdin

input = stdin.readline


def bfs(idx):
    start = [idx]
    visited = [False] * (n + 1)
    kv = 0
    res = 0
    while start:
        new_start = []
        for now in start:
            if visited[now]:
                continue
            visited[now] = True
            for adj in graph[now]:
                if not visited[adj]:
                    new_start.append(adj)
        kv += 1
        res += kv * len(start)
        start = new_start
    return res


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
min_kv = 10000
for i in range(1, n + 1):
    if bfs(i) < min_kv:
        min_kv = bfs(i)
        ans = i
print(ans)
