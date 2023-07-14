# brute force
# bfs 최단 거리 중 최대 거리 찾기 문제
# bfs로 한 영역의 연결 상태를 구한다
# 해당 영역에서 거리를 가지고 그레프를 만든다
# 그래프에서 거리가 가장 먼 곳들을 구한다.
from collections import deque

def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < L and 0 <= ny < W and arr[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
L, W = map(int, input().split())
arr = [list(input()) for _ in range(L)]

visited = [[-1] * W for _ in range(L)]
for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L' and visited[i][j] == -1:
            visited[i][j] = 0
            bfs(i, j)
print(visited)
