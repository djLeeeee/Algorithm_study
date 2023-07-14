# 백줕 13164번 행복 유치원

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(300000)


def group(total, rest, s):
    global ans

    if rest <= 1:
        ans = min(total + (h[N - 1] - h[s]), ans)
        return
    for e in range(s, N - rest + 1):
        group(h[e] - h[s] + total, rest - 1, e + 1)


N, K = map(int, input().split())
h = list(map(int, input().split()))
ans = (10 ** 9) * K
if K == 1:
    ans = h[N - 1] - h[0]
else:
    for e in range(N - K + 1):
        group(h[e] - h[0], K - 1, e + 1)
print(ans)