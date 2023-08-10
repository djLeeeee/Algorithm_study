board = [list(input()) for _ in range(12)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] in 'RGBPY':
                T = board[i][j]
                board[i][j] = '.'
                point = [(i, j)]
                memo = [(i, j)]
                while point:
                    x, y = point.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == T:
                            board[nx][ny] = '.'
                            point.append((nx, ny))
                            memo.append((nx, ny))
                if len(memo) < 4:
                    for x, y in memo:
                        board[x][y] = T
                else:
                    flag = True
    for j in range(6):
        col = '.' * 12
        for i in range(12):
            if board[i][j] != '.':
                col += board[i][j]
        for i in range(-1, -13, -1):
            board[i][j] = col[i]
    if not flag:
        break
    ans += 1
print(ans)
