import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().strip().split())

ans = [0] * (N+1)

def do(j):
    heap = [(0, j)]
    visited = [0] * (N+1)
    dist = [100001] * (N+1)
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v] and w < dist[v]:
            if v == X and j != X:
                ans[v] += w
                return
            visited[v] = 1
            dist[v] = w
            for way in g[v]:
                if not visited[way[0]] and w + way[1] < dist[way[0]]:
                    heapq.heappush(heap, (w + way[1], way[0]))
    if j == X:
        for l in range(1, N+1):
            ans[l] += dist[l]


g = [[] for _ in range(N+1)]

for i in range(M):
    start, end, weight = map(int, input().strip().split())
    g[start].append((end, weight))

for j in range(1, N+1):
    do(j)

print(max(ans))