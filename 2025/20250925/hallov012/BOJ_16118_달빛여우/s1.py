import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def f_dijkstra(s):
    dist = [sys.maxsize] * (n + 1)
    dist[s] = 0
    q = []
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

def w_dijkstra(s):
    dist = [[sys.maxsize] * (n+1) for _ in range(2)]
    q = []
    heapq.heappush(q, (0, s, 0))
    while q:
        d, now, flag = heapq.heappop(q)
        if dist[flag][now] < d:
            continue
        for next, c in g[now]:
            tmp = d + c * (0.5 if not flag else 2)
            n_flag = abs(flag-1)
            if tmp < dist[n_flag][next]:
                dist[n_flag][next] = tmp
                heapq.heappush(q, (tmp, next, n_flag))
    return dist

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, d = map(int, input().split())
    g[a].append((b, d))
    g[b].append((a, d))

f_dist = f_dijkstra(1)
w_dist = w_dijkstra(1)

ans = 0
for i in range(2, n+1):
    if f_dist[i] < min(w_dist[0][i], w_dist[1][i]):
        ans += 1
print(ans)