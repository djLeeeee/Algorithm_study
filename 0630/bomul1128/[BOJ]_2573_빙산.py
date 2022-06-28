from sys import stdin

input = stdin.readline


def melt():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    memo = []
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                ex = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if not board[nx][ny]:
                        ex += 1
                memo.append((x, y, ex))
    remain = []
    while memo:
        x, y, ex = memo.pop()
        if board[x][y] <= ex:
            board[x][y] = 0
        else:
            board[x][y] -= ex
            remain.append((x, y))
    visited = [[False] * m for _ in range(n)]
    result = 0
    for x, y in remain:
        if not visited[x][y]:
            if result:
                return 2
            result += 1
            visited[x][y] = True
            point = [(x, y)]
            while point:
                nx, ny = point.pop()
                for d in range(4):
                    nnx = nx + dx[d]
                    nny = ny + dy[d]
                    if board[nnx][nny] and not visited[nnx][nny]:
                        visited[nnx][nny] = True
                        point.append((nnx, nny))
    return result


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
day = 0
glacier = 1
while glacier == 1:
    day += 1
    glacier = melt()
print(day if glacier else 0)
