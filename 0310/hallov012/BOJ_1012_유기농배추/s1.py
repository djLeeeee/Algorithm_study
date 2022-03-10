import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    checked = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    check = False
    ans = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] and not checked[i][j]:
                checked[i][j] = 1
                que = deque([[i, j]])
                while que:
                    x, y = que.popleft()
                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if 0 <= nx < n and 0 <= ny < m:
                            if farm[nx][ny] and not checked[nx][ny]:
                                check = True
                                checked[nx][ny] = 1
                                que.append([nx, ny])
                ans += 1
    print(ans)


