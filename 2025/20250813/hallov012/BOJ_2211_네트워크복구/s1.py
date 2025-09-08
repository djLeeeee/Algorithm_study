import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            if dist[next] > d + c:
                dist[next] = d + c
                p[next] = now
                heapq.heappush(q, (dist[next], next))


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = [sys.maxsize] * (n+1)
p = list(range(n+1))

dijkstra(1)
print(n-1)
for i in range(2, n+1):
    print(i, p[i])