import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            a, b = i, j
now_size = 2
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0
exp = 0
while 1:
    que = deque([(a, b)])
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    check_d = n * n
    can_eat = []
    while que:
        x, y = que.popleft()
        if visited[x][y] > check_d:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] <= now_size:
                    if 0 < arr[nx][ny] < now_size:
                        if check_d > visited[x][y]:
                            check_d = visited[x][y]
                        can_eat.append((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        que.append((nx, ny))
    if not can_eat:
        print(ans)
        break
    else:
        can_eat.sort()
        arr[a][b] = 0
        a, b = can_eat[0]
        arr[a][b] = 9
        ans += check_d
        exp += 1
        if exp == now_size:
            now_size += 1
            exp = 0


