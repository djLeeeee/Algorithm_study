from sys import stdin
from itertools import combinations

input = stdin.readline


def sol(o):
    res = 0
    for ii in range(n):
        for jj in range(n):
            if memo[o[0]][ii][jj] == 1:
                continue
            val = -1
            for op in o:
                now = memo[op][ii][jj]
                if not now:
                    continue
                if val == -1 or val > now - 2:
                    val = now - 2
            if val == -1:
                return None
            if res == 0 or val > res:
                res = val
    return res


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            board[i][j] = 0
            virus.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
memo = {}
for p in virus:
    memo[p] = [line[:] for line in board]
    memo[p][p[0]][p[1]] = 2
    point = [p]
    for x, y in point:
        v = memo[p][x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and memo[p][nx][ny] == 0:
                memo[p][nx][ny] = v + 1
                point.append((nx, ny))
ans = -1
for order in combinations(virus, m):
    k = sol(order)
    if k is None:
        continue
    if ans == -1 or ans > k:
        ans = k
print(ans)
