from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            visited[i][j] = -1
            point = deque([(i, j)])
            while point:
                x, y = point.popleft()
                c = visited[x][y]
                if c == -1:
                    c = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L' and not visited[nx][ny]:
                            visited[nx][ny] = c + 1
                            point.append((nx, ny))
                            if ans < c + 1:
                                ans = c + 1
print(ans)
