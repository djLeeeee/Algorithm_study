import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra(s, e):
    dist = [0] * (n+1)
    dist[s] = sys.maxsize
    q = []
    # 최대로 옮길 수 있는 양을 구할거니까 -1을 곱해 줌
    heapq.heappush(q, (-sys.maxsize, s))
    while q:
        d, now = heapq.heappop(q)
        d *= -1
        if d < dist[now]:
            continue
        for b, c in g[now]:
            # b 까지 들고 올 수 있었 던 양이, 지금까지 들 수 있었 던 양보다 작으면 갱신
            if dist[b] < min(d, c):
                dist[b] = min(d, c)
                heapq.heappush(q, (-dist[b], b))
    return dist[e]

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
s, e = map(int, input().split())
ans = dijkstra(s, e)
print(ans)