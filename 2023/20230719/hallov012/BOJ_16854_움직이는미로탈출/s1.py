import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = []
walls = deque()
n = 8
for i in range(n):
    row = list(input().rstrip())
    arr.append(row)
    for j in range(n):
        if row[j] == '#':
            walls.append((i, j))

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
que = deque([(7, 0)])
ans = 0

while que:
    # 이동
    visited = [[0] * n for _ in range(n)]
    for _ in range(len(que)):
        x, y = que.popleft()
        if (x, y) in walls:
            continue
        if x == 0 and y == n-1:
            ans = 1
            break
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not (nx, ny) in walls and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
    if ans:
        break

    # 벽 내리기
    if walls:
        for _ in range(len(walls)):
            x, y = walls.popleft()
            if x < n-1:
                walls.append((x+1, y))

print(ans)

