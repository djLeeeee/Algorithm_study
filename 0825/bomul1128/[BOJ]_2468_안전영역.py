from sys import stdin

input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for limit in range(1, 100):
    visited = [[False] * n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > limit and not visited[i][j]:
                temp += 1
                stack = [(i, j)]
                visited[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] > limit and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
    if temp > ans:
        ans = temp
    elif not temp:
        break
print(ans)
