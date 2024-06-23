import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
mt = [list(map(int, input())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = 0
print(mt)

for r in range(n):
    for c in range(m):
        if r == 0 or c == 0:
            dp[r][c] = mt[r][c]
        else:
            dp[r][c] = (mt[r][c] and min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]))+mt[r][c]

        ans = max(dp[r][c], ans)


print(ans**2)