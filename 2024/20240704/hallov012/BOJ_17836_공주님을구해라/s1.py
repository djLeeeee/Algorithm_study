import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

que = deque()
que.append((0, 0))
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tmp = sys.maxsize

while que:
    x, y = que.popleft()
    if x == n-1 and y == m-1:
        tmp = min(tmp, visited[x][y])
        break
    if arr[x][y] == 2:
        dist = (n-1-x) + (m-1-y)
        tmp = min(tmp, visited[x][y] + dist)
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
if tmp > t:
    print('Fail')
else:
    print(tmp)

