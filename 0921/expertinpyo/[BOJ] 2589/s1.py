# bfs
# 가능한 점 마다 다 볼 필요는 있으나, 부르트포스로 풀게 되면 너무 비효율 적일 것 같음
from collections import deque
def bfs(x, y):
    cnt = 0
    queue = deque([])
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < L and 0 <= ny < W and arr[nx][ny] == 'L' and visited_2[nx][ny] == -1:
                queue.append((nx, ny))
                visited_2[nx][ny] = visited_2[x][y] + 1
                if cnt < visited_2[nx][ny]:
                    cnt = visited_2[nx][ny]
    return cnt

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
L, W = map(int, input().split())
arr = [list(input()) for _ in range(L)]

check = []
visited = [[-1] * W for _ in range(L)]
for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L' and visited[i][j] == -1:
            visited[i][j] = 0
            cnt = bfs(i, j)
            for a in range(L)