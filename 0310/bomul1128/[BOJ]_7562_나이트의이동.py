from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())
    board = [[1] * n for _ in range(n)]
    board[x][y] = 0
    cost = 0
    start = [(x, y)]
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    while board[fx][fy] == 1:
        new_start = []
        for x, y in start:
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                    new_start.append((nx, ny))
                    board[nx][ny] = 0
        cost += 1
        start = new_start
    print(cost)
