import sys
input = sys.stdin.readline

n, l, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]
fish = [list(map(int, input().split())) for _ in range(m)]
for x, y in fish:
    dp[x][y] = 1
case = []
for i in range(1, l//2):
    j = (l - 2*i) // 2
    if i < n and j < n:
        case.append((i, j))

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + dp[i][j]

for i, j in fish:
    for x, y in case:
        for a in range(i-x, i+1):
            for b in range(j-y, j+1):
                if 0 <= a <= n and 0 <= b <= n:
                    temp = dp[a][b] - dp[a][j-1] - dp[i-1][b] + dp[i-1][j-1]
                    if temp > ans:
                        ans = temp
                        if ans == m:
                            print(m)
                            exit()
print(ans)