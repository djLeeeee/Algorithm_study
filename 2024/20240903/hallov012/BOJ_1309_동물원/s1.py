import sys
sys.stdin = open('input.txt')

n = int(input())
m = 9901
dp = [[0] * 3 for _ in range(n)]
dp[0] = [1, 1, 1]
for i in range(1, n):
    b_sum = sum(dp[i-1])
    dp[i][0] = b_sum % m
    dp[i][1] = (b_sum - dp[i-1][1]) % m
    dp[i][2] = (b_sum - dp[i-1][2]) % m

print(sum(dp[n-1]) % m)

