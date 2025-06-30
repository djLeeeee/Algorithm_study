import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(q, dist):
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            cost = d + c
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(q, (cost, next))
    return dist

INF = int(9e9)
V, E = map(int, input().split())
g = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

M, x = map(int, input().split())
m_lst = list(map(int, input().split()))
m_dist = [INF] * (V+1)
m_q = []
for m in m_lst:
    m_dist[m] = 0
    m_q.append((0, m))
dijkstra(m_q, m_dist)

S, y = map(int, input().split())
s_lst = list(map(int, input().split()))
s_dist = [INF] * (V+1)
s_q = []
for s in s_lst:
    s_dist[s] = 0
    s_q.append((0, s))
dijkstra(s_q, s_dist)

ans = -1
for i in range(1, V+1):
    if not m_dist[i] or not s_dist[i]:
        continue
    if m_dist[i] <= x and s_dist[i] <= y:
        if ans == -1:
            ans = m_dist[i] + s_dist[i]
        else:
            ans = min(ans, m_dist[i] + s_dist[i])

print(ans)