import sys, heapq
from collections import defaultdict

sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(s):
    dist = [INF] * (V+3)
    dist[s] = 0
    q = [(0, s)]
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            if next in (m_node, s_node):
                continue
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
S, y = map(int, input().split())
s_lst = list(map(int, input().split()))

m_node = V+1
for m in m_lst:
    g[m].append((m_node, 0))
    g[m_node].append((m, 0))
s_node = V+2
for s in s_lst:
    g[s].append((s_node, 0))
    g[s_node].append((s, 0))

m_dist = dijkstra(m_node)
s_dist = dijkstra(s_node)

ans = INF
for i in range(1, V+1):
    m_d, s_d = m_dist[i], s_dist[i]
    if not m_d or not s_d:
        continue
    if m_d <= x and s_d <= y:
        ans = min(ans, m_d + s_d)
print(ans if ans != INF else -1)