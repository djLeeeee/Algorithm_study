m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (m + 1) for _ in range(n + 1)]
size = [0] * (n * m + 1)
room = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room += 1
            s = 1
            visited[i][j] = room
            point = [(i, j)]
            while point:
                x, y = point.pop()
                check = board[x][y]
                for bit in range(4):
                    if not check & (1 << bit):
                        nx = x + dx[bit]
                        ny = y + dy[bit]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            visited[nx][ny] = room
                            s += 1
                            point.append((nx, ny))
            size[room] = s
print(room)
M = max(size)
print(M)
ans = M
for i in range(n):
    for j in range(m):
        if visited[i][j] != visited[i + 1][j]:
            if ans < size[visited[i][j]] + size[visited[i + 1][j]]:
                ans = size[visited[i][j]] + size[visited[i + 1][j]]
        if visited[i][j] != visited[i][j + 1]:
            if ans < size[visited[i][j]] + size[visited[i][j + 1]]:
                ans = size[visited[i][j]] + size[visited[i][j + 1]]
print(ans)
