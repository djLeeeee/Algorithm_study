from sys import stdin

input = stdin.readline

n = int(input())
dp = [[1] * n for _ in range(n)]
board = []
bamboo = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        bamboo.append((line[j], i, j))
    board.append(line)
bamboo.sort()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 1
while bamboo:
    size, x, y = bamboo.pop()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            if dp[x][y] < dp[nx][ny] + 1:
                dp[x][y] = dp[nx][ny] + 1
                if ans < dp[x][y]:
                    ans = dp[x][y]
print(ans)
