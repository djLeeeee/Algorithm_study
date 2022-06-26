from sys import stdin

input = stdin.readline
div = 1000000007


def power(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
            result %= div
        a = a * a
        a %= div
        b >>= 1
    return result


for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(power(2, N - 2) % div)
