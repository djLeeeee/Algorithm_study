import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
sx = sy = ex = ey = -1
for i in range(n):
    row = input().rstrip()
    for j in range(m):
        if row[j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j
    arr.append(row)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
que = deque()
que.append((sx, sy, -1, -1))

ans = n * m + 1
visited = [[[n * m + 1] * m for _ in range(n)] for _ in range(4)]
while que:
    x, y, d, cnt = que.popleft()
    if x == ex and y == ey:
        ans = min(ans, cnt)
        continue
    for i in range(4):
        # 현재와 반대 방향은 갈 수 없음 (-1은 초기 start 값 => 모두 가능)
        if d != -1 and abs(d-i) == 2:
            continue
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '*':
            val = cnt if d == i else cnt+1
            if visited[i][nx][ny] > val:
                visited[i][nx][ny] = val
                que.append((nx, ny, i, val))

print(ans)


