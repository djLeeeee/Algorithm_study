from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [[]] * n
virus1 = set()
virus2 = set()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            virus1.add((i, j))
        elif line[j] == 2:
            virus2.add((i, j))
    board[i] = line
while virus1 or virus2:
    new_virus1 = set()
    new_virus2 = set()
    for x, y in virus1:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    new_virus1.add((nx, ny))
    for x, y in virus2:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    new_virus2.add((nx, ny))
                elif board[nx][ny] == 1:
                    if (nx, ny) in new_virus1:
                        board[nx][ny] = 3
                        new_virus1.remove((nx, ny))
    virus1 = new_virus1
    virus2 = new_virus2
ans = [0, 0, 0]
for line in board:
    for i in line:
        if i > 0:
            ans[i - 1] += 1
print(*ans)
