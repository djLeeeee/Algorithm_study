import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y] # 이미 갔으면 다시 가지 않기
    dp[x][y] = 1
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < N and 0 <= ny < N and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]






N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
dp = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(dfs(i, j), answer)
print(answer)
