import sys
from collections import deque

sys.stdin = open('input.txt')

n, m = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt_g = [[0] * m for _ in range(n)]

queue = deque([[0, 0]])
visited[0][0] = True
cnt_g[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt_g[nx][ny] = cnt_g[x][y] + 1
print(cnt_g[n-1][m-1])