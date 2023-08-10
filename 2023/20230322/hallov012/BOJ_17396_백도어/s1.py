import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            if dist[next] > dist[now] + c and not visible[next]:
                dist[next] = dist[now] + c
                heapq.heappush(q, (dist[next], next))
    return dist

n, m = map(int, input().split())
visible = list(map(int, input().split()))
visible[-1] = 0
g = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    g[a].append((b, t))
    g[b].append((a, t))
dist = dijkstra(0)

if dist[-1] == sys.maxsize:
    print(-1)
else:
    print(dist[-1])