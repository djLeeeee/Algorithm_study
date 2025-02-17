import sys, heapq
from collections import defaultdict

sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (V+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            if dist[next] > d + cost:
                dist[next] = d + cost
                heapq.heappush(q, (dist[next], next))
    return dist


V, E, P = map(int, input().split())
p = list(range(V+1))
g = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

start_dist = dijkstra(1)
save_dist = dijkstra(P)

if start_dist[V] == start_dist[P] + save_dist[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')



