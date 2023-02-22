# https://www.acmicpc.net/problem/14267

import sys
sys.stdin = open("14267.txt")
sys.setrecursionlimit(10**6)  # 이거 안 하면 Recursion Error 발생
input = sys.stdin.readline

N, M = map(int, input().split())

relation = list(map(int, input().split()))
sub = [[] for _ in range(N + 1)]

# 한 사람이 여러 부하직원을 데리고 있을 수도 있다.
for n in range(N):
    sup = relation[n]
    if (sup > 0):
        sub[sup].append(n + 1)

compliments = [0] * (N + 1)
dp = [0] * (N + 1)

for _ in range(M):
    i, w = map(int, input().split())
    compliments[i] += w


def getSum(n, w):
    if (dp[n]):
        return

    dp[n] = w + compliments[n]

    for next in sub[n]:
        getSum(next, dp[n])


for n in range(1, N + 1):
    for next in sub[n]:
        getSum(next, compliments[n])

print(*dp[1:])
