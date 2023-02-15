from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for x in range(a, c):
        for y in range(b, d):
            board[x][y] = 1
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
for x in range(m):
    for y in range(n):
        if not board[x][y]:
            board[x][y] = 1
            ans += 1
            cnt = 1
            point = [(x, y)]
            for nx, ny in point:
                for d in range(4):
                    mx = nx + dx[d]
                    my = ny + dy[d]
                    if 0 <= mx < m and 0 <= my < n and not board[mx][my]:
                        board[mx][my] = 1
                        cnt += 1
                        point.append((mx, my))
            result.append(cnt)
result.sort()
print(ans)
print(*result)
