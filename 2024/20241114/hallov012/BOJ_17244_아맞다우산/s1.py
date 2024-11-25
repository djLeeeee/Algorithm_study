import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = []
m, n = map(int, input().split())
cnt = 0
sx, sy = 0, 0
ex, ey = 0, 0
object = {}
for i in range(n):
    row = list(input())
    arr.append(row)
    for j in range(m):
        if row[j] == 'X':
            object[(i, j)] = cnt
            cnt += 1
        elif row[j] == 'S':
            sx, sy = i, j
            arr[i][j] = '.'
        elif row[j] == 'E':
            ex, ey = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[0] * m for _ in range(n)] for _ in range(1 << cnt)]
que = deque([(sx, sy, 0)])

while que:
    x, y, bit = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[bit][nx][ny] and arr[nx][ny] != '#':
                if arr[nx][ny] == 'X':
                    nbit = bit | 1 << object[(nx, ny)]
                    visited[nbit][nx][ny] = visited[bit][x][y] + 1
                    que.append((nx, ny, nbit))
                else:
                    nbit = bit
                    visited[bit][nx][ny] = visited[bit][x][y] + 1
                    que.append((nx, ny, bit))

                if arr[nx][ny] == 'E' and nbit == 2**cnt - 1:
                    print(visited[nbit][nx][ny])
                    break





