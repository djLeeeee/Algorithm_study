import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            val = dist[now] + cost
            if val < dist[next]:
                dist[next] = val
                heapq.heappush(q, (val, next))
    return dist

n, m, x, y = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = dijkstra(y)
dist.sort()
if dist[-1] * 2 > x:
    print(-1)
    exit()
idx, cnt, ans = 0, 0, 1
for d in dist:
    if cnt + d*2 <= x:
       cnt += d*2
    else:
        ans += 1
        cnt = d*2
print(ans)
