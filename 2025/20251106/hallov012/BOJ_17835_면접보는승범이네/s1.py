import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra():
    dist = [sys.maxsize] * (n+1)
    q = []
    for s in k_lst:
        dist[s] = 0
        heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            if d + c < dist[next]:
                dist[next] = d + c
                heapq.heappush(q, (dist[next], next))
    return dist

n, m, k = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    u, v, c = map(int, input().split())
    # 면접장에서 역으로 갈거니까 역으로 저장
    g[v].append((u, c))

k_lst = list(map(int, input().split()))
dist = dijkstra()
max_idx, max_d = 0, 0
for i, d in enumerate(dist):
    if d > max_d and d != sys.maxsize:
        max_idx, max_d = i, d
print(max_idx)
print(max_d)
