from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tomato = deque()
rare = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tomato.append((i, j))
        elif not board[i][j]:
            rare += 1
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while tomato:
    x, y = tomato.popleft()
    ans = board[x][y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
            tomato.append((nx, ny))
            board[nx][ny] = ans + 1
            rare -= 1
if rare:
    print(-1)
else:
    print(ans - 1)
