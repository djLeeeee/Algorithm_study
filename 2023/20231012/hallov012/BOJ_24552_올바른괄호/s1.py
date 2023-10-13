import sys
sys.stdin = open('input.txt')

S = input()
n = len(S)
ans = 0
# 항상 여는 괄호가 더 많아야하고, 마지막에는 두개의 수가 같아야함
# i-1은 삭제할 인덱스 :)
for i in range(n):
    dp = [[0, 0] for _ in range(n+1)]
    for j in range(n):
        dp[j+1] = dp[j][::]
        if i == j:
            if j == n-1:
                if dp[j+1][0] == dp[j+1][1]:
                    ans += 1
            continue
        if S[j] == '(':
            dp[j+1][0] += 1
        else:
            dp[j+1][1] += 1

        if dp[j+1][1] > dp[j+1][0]:
            break

        if j == n-1:
            if dp[j+1][0] == dp[j+1][1]:
                ans += 1

print(ans)