import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue=deque()
    queue.append((i, j))
    visited = [[0]* N for _ in range(M)]
    visited[i][j] = 1
    temp = 0
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if (0 <= nx < M and 0 <= ny < N) and trea_map[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                temp = max(temp, visited[nx][ny])
                queue.append((nx, ny))
    return temp - 1


M, N = map(int, input().split())
trea_map = [list(input()) for _ in range(M)]
dist = [[0]*N for _ in range(M)]
# 시작점 후보 저장
land = []
for i in range(M):
    for j in range(N):
        if trea_map[i][j] == 'L':
            land.append((i, j))
# print(land)
answer = 0
for dot in land:
    answer = max(answer, bfs(dot[0], dot[1]))
print(answer)
