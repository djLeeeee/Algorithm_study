import sys, heapq
input = sys.stdin.readline
M, N = map(int, input().strip().split())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

g = [list(map(int, input().strip())) for _ in range(N)]
visited = [[M * N] * M for _ in range(N)]

heap = [(0, 0, 0)]                         # 힙생성
visited[0][0] = 0                          # 벽 부순 개수 세는 visited 생성

while heap:
    weight, r, c = heapq.heappop(heap)     # heap 쓸 것이기 때문에 가중치를 제일 앞에 깔아줍니다.
    if r == N-1 and c == M-1:              # 목표에 도착한 상황이면, 힙에서는 무조건 최소이기 때문에 그냥 끝.
        print(visited[r][c])
        break
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < M:    
            if not g[nr][nc] and visited[nr][nc] > weight:     # 벽이 없는 통로인데 도달하는 데 부순 벽의 수가 더 적으면
                visited[nr][nc] = weight
                heapq.heappush(heap, (weight, nr, nc))
            elif g[nr][nc] and visited[nr][nc] > weight + 1:   # 벽이 있는 통로인데 동조건이면
                visited[nr][nc] = weight + 1
                heapq.heappush(heap, (weight + 1, nr, nc))

# 일반적인 bfs를 응용해서 풀어보려고 했는데,
# 생각해보니 응용 bfs랑 다익스트라랑 별 차이가 없는 것 같아서
# 그냥 다익스트라로 푸는 게 맞는 것 같다.
