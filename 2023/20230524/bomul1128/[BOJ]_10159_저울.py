# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/10159
from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    dp[x][y] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if not dp[j][k]:
                if dp[j][i] and dp[i][k]:
                    dp[j][k] = 1
for target in range(1, n + 1):
    ans = n - 1
    for compare in range(1, n + 1):
        ans -= dp[target][compare] + dp[compare][target]
    print(ans)
