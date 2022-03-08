from sys import stdin
from sys import setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(x, y):
    if not board[x][y]:
        return
    board[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
            dfs(nx, ny)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        bx, by = map(int, input().split())
        board[bx][by] = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)
