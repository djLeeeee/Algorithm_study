import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

visited = [0] * (n+1)
teams = []
for i in range(1, n+1):
    if not visited[i]:
        temp = []
        for j in range(1, n+1):
            if dp[i][j] != sys.maxsize:
                temp.append(j)
                visited[j] = 1
        teams.append(temp)

ans = []
for team in teams:
    min_num = sys.maxsize
    temp = 0
    for i in team:
        max_num = 0
        for j in team:
            if max_num < dp[i][j]:
                max_num = dp[i][j]
        if max_num < min_num:
            min_num = max_num
            temp = i
    ans.append(temp)

ans.sort()
print(len(ans))
for num in ans:
    print(num)
