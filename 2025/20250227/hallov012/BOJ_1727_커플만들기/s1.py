import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

# 무조건 m이 더 크게(b그룹 사람이 더 많게)
if n > m:
    a_lst, b_lst = b_lst, a_lst
    n, m = m, n

a_lst.sort()
b_lst.sort()

dp = [[0] * m for _ in range(n)]
dp[0][0] = abs(a_lst[0]-b_lst[0])
# a 그룹 첫번째 사람과, 다른 b그룹 사이의 성격차
for i in range(1, m-(n-1)):
    dp[0][i] = min(abs(a_lst[0]-b_lst[i]), dp[0][i-1])

for i in range(1, n):
    for j in range(i, m-(n-i-1)):
        gap = abs(a_lst[i]-b_lst[j])
        if i == j:
            dp[i][j] = dp[i-1][j-1] + gap
        else:
            # 차이가 min인 값 누적
            dp[i][j] = min(dp[i-1][j-1] + gap, dp[i][j-1])

print(dp[n-1][m-1])


