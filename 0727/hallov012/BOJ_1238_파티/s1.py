import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    while que:
        d, now = heapq.heappop(que)
        if dist[now] < d:
            continue
        for b, c in g[now]:
            if dist[b] > d + c:
                dist[b] = d + c
                heapq.heappush(que, (dist[b], b))
    return dist

input = sys.stdin.readline

n, m, x = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
ans = 0
# x에서 돌아가는 거리 구해놓기
back = dijkstra(x)
for i in range(1, n+1):
    go = dijkstra(i)
    temp = go[x] + back[i]
    ans = max(ans, temp)
print(ans)

