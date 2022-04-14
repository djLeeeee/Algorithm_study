from sys import stdin

input = stdin.readline


def spread():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_board = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                new_board[x][y] += board[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] >= 0:
                        new_board[nx][ny] += board[x][y] // 5
                        new_board[x][y] -= board[x][y] // 5
    new_board[ccw][0] = -1
    new_board[cw][0] = -1
    return new_board


def rotate():
    x = ccw
    while x > 1:
        board[x - 1][0] = board[x - 2][0]
        x -= 1
    y = 0
    while y + 1 < m:
        board[0][y] = board[0][y + 1]
        y += 1
    x = 0
    while x < ccw:
        board[x][-1] = board[x + 1][-1]
        x += 1
    y = m - 1
    while y > 1:
        board[ccw][y] = board[ccw][y - 1]
        y -= 1
    x = cw + 1
    while x + 1 < n:
        board[x][0] = board[x + 1][0]
        x += 1
    y = 0
    while y + 1 < m:
        board[-1][y] = board[-1][y + 1]
        y += 1
    x = n - 1
    while x > cw:
        board[x][-1] = board[x - 1][-1]
        x -= 1
    y = m - 1
    while y > 1:
        board[cw][y] = board[cw][y - 1]
        y -= 1
    board[ccw][1] = 0
    board[cw][1] = 0
    return


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if board[i][0] == -1:
        ccw, cw = i, i + 1
        break
for _ in range(t):
    board = spread()
    rotate()
print(sum([sum(line) for line in board]) + 2)
