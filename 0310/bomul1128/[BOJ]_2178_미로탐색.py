from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start = [(0, 0)]
board[0][0] = 0
day = 1
flag = False
while board[-1][-1] == 1:
    new_start = []
    for x, y in start:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                new_start.append((nx, ny))
                board[nx][ny] = 0
    day += 1
    start = new_start
print(day)
