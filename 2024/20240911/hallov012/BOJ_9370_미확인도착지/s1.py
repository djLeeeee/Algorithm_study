import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra(s):
    dist = [sys.maxsize] * (n+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in graph[now]:
            if dist[next] > d + cost:
                dist[next] = d + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)
    gh_dist = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a, b) == (g, h) or (a, b) == (h, g):
            gh_dist = d

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    ans = []
    for _ in range(t):
        x = int(input())
        g_to_h = dist_s[g] + gh_dist + dist_h[x]
        h_to_g = dist_s[h] + gh_dist + dist_g[x]
        if dist_s[x] == g_to_h or dist_s[x] == h_to_g:
            ans.append(x)
    ans.sort()
    print(*ans)
