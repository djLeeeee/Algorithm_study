n, m = map(int, input().split())
board = [input() for _ in range(n)]
s = [[-1] * m for _ in range(n)]
w = [[-1] * m for _ in range(n)]
sw = {
    'S': s, '*': w
}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
fx, fy = 0, 0
for i in range(n):
    for j in range(m):
        if (now := sw.get(board[i][j])) is not None:
            now[i][j] = 0
            point = [(i, j)]
            for x, y in point:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                        if now[nx][ny] == -1 or now[nx][ny] > now[x][y] + 1:
                            now[nx][ny] = now[x][y] + 1
                            point.append((nx, ny))
        elif board[i][j] == 'D':
            fx, fy = i, j
ans = -1
for d in range(4):
    nx = fx + dx[d]
    ny = fy + dy[d]
    if 0 <= nx < n and 0 <= ny < m and s[nx][ny] != -1:
        if w[nx][ny] == -1 or s[nx][ny] < w[nx][ny]:
            if ans == -1 or s[nx][ny] + 1 < ans:
                ans = s[nx][ny] + 1
print('KAKTUS' if ans == -1 else ans)
