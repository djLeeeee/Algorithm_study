from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 0
while True:
    outside = [[False] * m for _ in range(n)]
    outside[0][0] = True
    point = [(0, 0)]
    while point:
        x, y = point.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny] and not outside[nx][ny]:
                outside[nx][ny] = True
                point.append((nx, ny))
    melt = []
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if board[x][y]:
                c = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if outside[nx][ny]:
                        c += 1
                if c >= 2:
                    melt.append((x, y))
    if not melt:
        break
    day += 1
    for x, y in melt:
        board[x][y] = 0
print(day)
