from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)

point = [[[0, 0, 0, 0] for _ in range(4)] for _ in range(6)]
for k in range(4):
    point[1][k][k] = 1
    point[2][k][k] = 1
    point[2][k][(k + 2) % 4] = 1
    point[3][k][k] = 1
    point[3][k][(k + 1) % 4] = 1
    for kk in range(3):
        point[4][k][(k + kk) % 4] = 1
point[5] = [[1, 1, 1, 1] for _ in range(4)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(stack):
    if len(stack) == len(cctv):
        check = [[False] * m for _ in range(n)]
        temp = n * m - wall
        for idx in range(len(cctv)):
            x, y = cctv[idx]
            state = board[x][y]
            if not check[x][y]:
                check[x][y] = True
                temp -= 1
            d = stack[idx]
            for go in range(4):
                if point[state][d][go]:
                    nx, ny = x, y
                    while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
                        if not check[nx][ny]:
                            check[nx][ny] = True
                            temp -= 1
                        nx += dx[go]
                        ny += dy[go]
        global ans
        if temp < ans:
            ans = temp
        return
    for d in range(4):
        dfs(stack + [d])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []
wall = 0
for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            cctv.append((i, j))
        elif board[i][j] == 6:
            wall += 1
ans = n * m
dfs([])
print(ans)
