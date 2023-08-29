import sys
from collections import deque
sys.stdin = open('input.txt')

r, c = map(int, input().split())
arr = []
fire = deque()
sx, sy = 0, 0
for i in range(r):
    line = list(input())
    arr.append(line)
    for j in range(c):
        if arr[i][j] == 'J':
            sx, sy = i, j
            arr[i][j] = '.'
            if sx == 0 or sx == r-1 or sy == 0 or sy == c-1:
                print(1)
                exit()
        elif arr[i][j] == 'F':
            fire.append((i, j))

visited = [[0] * c for _ in range(r)]
visited[sx][sy] = 1
que = deque([(sx, sy)])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    n = len(fire)
    for _ in range(n):
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == '.':
                    arr[nx][ny] = 'F'
                    fire.append((nx, ny))
    m = len(que)
    for _ in range(m):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and arr[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
                    if nx == 0 or nx == r-1 or ny == 0 or ny == c-1:
                        print(visited[nx][ny])
                        exit()
    if not que:
        break

print('IMPOSSIBLE')
