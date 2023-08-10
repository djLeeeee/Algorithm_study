# 크기 N * M
# 벽은 부술 수 있음
# 벽을 최소 몇개 부셔야 하는지
# 벽을 부수는 것을 가중치라고 생각 => dijkstra
import heapq
def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if not visited[x][y]:
            visited[x][y] = 1
            dist[x][y] = weight
            if x == N-1 and y == M-1:
                return
            for d in di:
                nx, ny = x + d[1], y + d[0]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if int(arr[nx][ny]):
                        new_w = 1
                    else:
                        new_w = 0
                    heapq.heappush(heap, (weight+new_w, nx, ny))

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dijkstra()
print(dist[-1][-1])