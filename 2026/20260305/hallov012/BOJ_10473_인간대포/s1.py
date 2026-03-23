import sys, heapq
from collections import defaultdict
from math import sqrt
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(s):
    q = []
    dist = [sys.maxsize] * (n+2)
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        if now == n+1:
            return dist[now]
        for next, cost in g[now]:
            tmp = dist[now] + cost
            if dist[next] > tmp:
                dist[next] = tmp
                heapq.heappush(q, (tmp, next))
    return dist[n+1]

sx, sy = map(float, input().split())
ex, ey = map(float, input().split())
n = int(input())
cannon_list = [[sx, sy]] + [list(map(float, input().split())) for _ in range(n)] + [[ex, ey]]

g = defaultdict(list)
for i in range(n+2):
    for j in range(i+1, n+2):
        x1, y1 = cannon_list[i]
        x2, y2 = cannon_list[j]
        dist = sqrt((x1-x2)**2 + (y1-y2)**2)
        walk_t = dist / 5
        cannon_t = 2 + abs(dist-50) / 5
        g[i].append((j, walk_t))
        if i > 0:
            g[i].append((j, cannon_t))
            g[j].append((i, walk_t))
            g[j].append((i, cannon_t))

print(dijkstra(0))