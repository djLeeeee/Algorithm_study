"""
# TLE
from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
chk = list(map(int, input().split()))
chk[-1] = 0
graph: defaultdict[int, dict[int, int]] = defaultdict(dict)
for _ in range(m):
    x, y, d = map(int, input().split())
    if chk[x] == chk[y] == 0:
        graph[x][y] = d
        graph[y][x] = d
dist = [-1] * n
dist[0] = 0
points: list[int] = [0]
inq = [False] * n
inq[0] = True
for idx in points:
    for adj, c in graph[idx].items():
        if dist[adj] == -1 or dist[adj] > dist[idx] + c:
            dist[adj] = dist[idx] + c
            if not inq[adj]:
                inq[adj] = True
                points.append(adj)
    inq[idx] = False
print(dist[-1])

"""
from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
chk = list(map(int, input().split()))
chk[-1] = 0
graph: defaultdict[int, dict[int, int]] = defaultdict(dict)
for _ in range(m):
    x, y, d = map(int, input().split())
    if chk[x] == chk[y] == 0:
        graph[x][y] = d
        graph[y][x] = d
dist = [-1] * n
dist[0] = 0
points = [(0, 0)]
while points:
    idx, u = heappop(points)
    if dist[idx] < u:
        continue
    if idx == n - 1:
        break
    for adj, v in graph[idx].items():
        if dist[adj] == -1 or dist[adj] > u + v:
            dist[adj] = u + v
            heappush(points, (adj, u + v))
print(dist[-1])
