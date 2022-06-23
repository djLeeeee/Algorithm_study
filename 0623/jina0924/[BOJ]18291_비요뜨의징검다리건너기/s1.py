# 백준 18291번 비요뜨의 징검다리 건너기

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    ans = [0] * (N+1)
    ans[1] = 1
    i = 2
    while i <= N:
        ans[i] += sum(ans[:i])
        i += 1
    print(ans[N] % (10 ** 9 + 7))