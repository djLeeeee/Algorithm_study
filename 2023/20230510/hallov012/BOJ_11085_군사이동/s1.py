import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
parent = list(range(p+1))
g = defaultdict(list)
for _ in range(w):
    i, j, z = map(int, input().split())
    g[i].append((j, z))
    g[j].append((i, z))

visited = [0] * p
q = []
heapq.heappush(q, (-sys.maxsize, c))
ans = sys.maxsize
# 크루스칼
while q:
    cost, now = heapq.heappop(q)
    cost *= -1
    if visited[now]:
        continue
    visited[now] = 1
    ans = min(ans, cost)
    if now == v:
        break
    for next, val in g[now]:
        heapq.heappush(q, (-val, next))
print(ans)
