import sys
from collections import deque
sys.stdin = open('input.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(storage, ripe):
    while ripe:
        x, y, cnt = ripe.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and storage[nx][ny] == 0:
                storage[nx][ny] = cnt + 1
                ripe.append((nx, ny, cnt + 1))



M, N = map(int, input().split())
storage = [list(map(int, input().split())) for _ in range(N)]
# print(storage)
ripe = deque()
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            ripe.append((i, j, 1))
# print(ripe)
bfs(storage, ripe)
max_date = 0
for line in storage:
    if max_date < max(line):
        max_date = max(line)
    if line.count(0) > 0:
        print(-1)
        break
else:
    if max_date > 1:
        print(max_date-1)
    else:
        print(0)
# print(storage)