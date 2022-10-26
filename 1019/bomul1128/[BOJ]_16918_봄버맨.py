r, c, n = map(int, input().split())
board = [[0] * c for _ in range(r)]
for i in range(r):
    line = input()
    for j in range(c):
        if line[j] == 'O':
            board[i][j] = 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for t in range(n - 1):
    for x in range(r):
        for y in range(c):
            board[x][y] += 1
    ex = []
    for x in range(r):
        for y in range(c):
            if board[x][y] == 4:
                ex.append((x, y))
    for x, y in ex:
        board[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                board[nx][ny] = 0
for line in board:
    ans = ['O' if c else '.' for c in line]
    print(''.join(ans))
