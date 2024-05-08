import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
wall = []
for i in range(n):
    row = tuple(map(int, input().split()))
    for j in range(m):
        if row[j]:
            wall.append((i, j))

h, w, sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1
visited = [[0] * m for _ in range(n)]
visited[sx][sy] = 1
que = deque()
que.append((sx, sy))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
    x, y = que.popleft()
    if x == ex and y == ey:
        print(visited[x][y] - 1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n-h+1 and 0 <= ny < m-w+1 and not visited[nx][ny]:
            for a, b in wall:
                if nx <= a < nx+h and ny <= b < ny+w:
                    break
            else:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
else:
    print(-1)