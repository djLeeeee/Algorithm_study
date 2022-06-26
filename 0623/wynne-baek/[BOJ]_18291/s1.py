import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def power(k):
    result = 1
    n = 2
    while k:
        if k & 1:
            result *= n
            result %= modulo
        n *= n
        n %= modulo
        k //= 2
    return result




T = int(input())
modulo = 10**9 + 7
for _ in range(T):
    N = int(input())
    if N >= 2:
        print(power(N-2))
    else:
        print(1)
