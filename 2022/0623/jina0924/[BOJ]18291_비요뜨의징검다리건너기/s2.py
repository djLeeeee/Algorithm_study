# 백준 18291번 비요뜨의 징검다리 건너기

import sys
sys.stdin = open('input.txt')

'''
징검다리 개수 N개 일 때 경우의 수 구하기
1개 : 1
2개 : 1
3개 : 1 + 1 = 2
4개 : 1 + 1 + 2 = 4
5개 : 1 + 1 + 2 + 4 = 8
=> f(n) = f(n-1) + f(n-2) + ... + f(2)초항이 1, 공비가 2인 등비수열
∴ f(n) = 2^(n-2)
'''
T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    ans, n, k = 1, 2, N - 2
    mod = 1000000007
    if N == 1:
        print(1)
    else:
        while k:
            if k % 2:
                ans *= n
                ans %= mod
            n *= n
            k //= 2
            n %= mod
        print(ans % mod)