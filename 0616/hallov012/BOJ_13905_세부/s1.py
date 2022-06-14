import sys, heapq
sys.stdin = open('input.txt')

# 최소힙을 이용한 최댓값 찾기
def dijkstra(start, end):
    visited = [0] * (n+1)
    visited[start] = sys.maxsize
    q = []
    heapq.heappush(q, (-sys.maxsize, start))
    while q:
        w, now = heapq.heappop(q)
        w *= -1
        # 더 많은 금을 들고 그 장소까지 갈 수 있는 다른 경우가 있다면 종료
        if visited[now] > w:
            continue
        for b, k in g[now]:
            if visited[b] < min(k, w):
                visited[b] = min(k, w)
                heapq.heappush(q, (-visited[b], b))
    return visited[end]

input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    h1, h2, k = map(int, input().split())
    g[h1].append((h2, k))
    g[h2].append((h1, k))
ans = dijkstra(s, e)
print(ans)