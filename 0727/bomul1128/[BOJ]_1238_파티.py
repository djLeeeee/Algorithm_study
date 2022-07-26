from sys import stdin
from heapq import *

input = stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph_inv = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph_inv[e].append((s, t))
INF = float('inf')
dist = [INF] * (n + 1)
dist[x] = 0
point = [(0, x)]
while point:
    c, idx = heappop(point)
    if dist[idx] < c:
        continue
    for adj, ex in graph[idx]:
        if dist[adj] > c + ex:
            dist[adj] = c + ex
            heappush(point, (dist[adj], adj))
dist_inv = [INF] * (n + 1)
dist_inv[x] = 0
point = [(0, x)]
while point:
    c, idx = heappop(point)
    if dist_inv[idx] < c:
        continue
    for adj, ex in graph_inv[idx]:
        if dist_inv[adj] > c + ex:
            dist_inv[adj] = c + ex
            heappush(point, (dist_inv[adj], adj))
ans = 0
for idx in range(1, n + 1):
    if ans < dist[idx] + dist_inv[idx]:
        ans = dist[idx] + dist_inv[idx]
print(ans)
