import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('input.txt')

def dfs(x, y):
    global ans
    # 만약 한번 방문했던 곳이라면 그곳에서 갈 수 있는 max 지점까지 이미 한번 count 한 것이기에 바로 return
    if dp[x][y]:
        return dp[x][y]
    # 현재 위치를 start 지점으로 해서 max로 갈 수 있는 수를 count 한다
    dp[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] > data[x][y]:
                # nx, ny에서 만약 2곳을 갈 수 있다면 x, y에서는 자신을 포함한 3곳을 갈 수 있으므로 +1
                # return 값이 나올 때 마다 그 전 경로는 plus count 돼서 갈 수 있는 모든 지점의 수를 count 할 수 있게 됨
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
# dfs와 dp를 연동하여 푸는 문제, 한 start 지점에서 갈 수 있는 max count는 항상 같다는 점을 이용해
# 이미 count 해준 지점들은 dp에 저장해준다
dp = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)