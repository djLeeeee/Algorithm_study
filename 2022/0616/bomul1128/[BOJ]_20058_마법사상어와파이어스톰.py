from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 4)


# 스톰
def storm(level):
    side = 2 ** level

    def rotate():
        target = [board[ii + di][jj:jj + side] for di in range(side)]
        for ni in range(side):
            for nj in range(side):
                board[ii + ni][jj + nj] = target[side - nj - 1][ni]

    for ii in range(1, n, side):
        for jj in range(1, n, side):
            rotate()


# 파이어
def fire():
    melt = []
    for ii in range(1, n + 1):
        for jj in range(1, n + 1):
            if board[ii][jj]:
                adj = 0
                for dd in range(4):
                    if board[ii + dx[dd]][jj + dy[dd]]:
                        adj += 1
                if adj < 3:
                    melt.append((ii, jj))
    for mx, my in melt:
        board[mx][my] -= 1


# DFS
def dfs(x, y):
    global size
    if visited[x][y] or board[x][y] == 0:
        return
    visited[x][y] = True
    size += 1
    for d in range(4):
        if not visited[x + dx[d]][y + dy[d]]:
            dfs(x + dx[d], y + dy[d])


# Input
n, q = map(int, input().split())
n = 2 ** n
board = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    board[i][1:-1] = list(map(int, input().split()))
order = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 파이어 스톰
for o in order:
    if o:
        storm(o)
    fire()

# 가장 큰 얼음 찾기
visited = [[True] * (n + 2) for _ in range(n + 2)]
for j in range(1, n + 1):
    for k in range(1, n + 1):
        visited[j][k] = False
remain = 0
ans = 0
for j in range(1, n + 1):
    for k in range(1, n + 1):
        remain += board[j][k]
        if not visited[j][k] and board[j][k]:
            size = 0
            dfs(j, k)
            ans = max(ans, size)

# 답 출력
print(remain)
print(ans)
