# 분할정복 거듭제곱
# 정확히 도착해야함
from sys import stdin
def powers(k):
    result = 1
    c = 2
    while k:
        if k & 1:
            result *= c
            result %= mod
        c *= c
        c %= mod
        k //= 2

    return result

input = stdin.readline
T = int(input())
mod = 10**9 + 7
for tc in range(T):
    n = int(input())
    if n >= 2:
        print(powers(n-2))
    else:
        print(1)