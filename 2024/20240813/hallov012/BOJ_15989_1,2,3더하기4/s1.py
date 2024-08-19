import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
m = 10000
# 1만 쓰는 경우는 항상 존재하니까 1로 설정
dp = [1] * (m+1)
for i in range(2, m+1):
    dp[i] += dp[i-2]
for i in range(3, m+1):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])

