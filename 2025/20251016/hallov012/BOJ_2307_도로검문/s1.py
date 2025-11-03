import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(s, e):
    dist = [sys.maxsize] * (n+1)
    dist[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            # 제거할 구간은 pass
            if (now, next) in [(s, e), (e, s)]:
                continue
            if d + c < dist[next]:
                dist[next] = d + c
                if not s:
                    pre[next] = now
                heapq.heappush(q, (dist[next], next))
    return dist[n]


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    g[a].append((b, t))
    g[b].append((a, t))

# 최단 경로 진행시, 각 노드의 이전 노드 저장
pre = [0] * (n+1)
sort_dist = dijkstra(0, 0)

if sort_dist == sys.maxsize:
    print(-1)
    exit()

ans = -1
e = n

while pre[e] != 0:
    s = pre[e]
    tmp = dijkstra(s, e)
    if tmp != sys.maxsize:
        ans = max(ans, tmp-sort_dist)
    else:
        ans = -1
        break
    e = s

print(ans)