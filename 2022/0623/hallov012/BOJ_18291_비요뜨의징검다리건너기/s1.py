import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    if n <= 2:
        print(1)
    else:
        """
        n = 1: ans = 1
        n = 2: ans = 1
        n = 3: ans = 2
        n = 4: ans = 4
        => f[x] = f[x-1] * 2
                = 2 ** (x-2) 라고 볼 수 있음 
        """
        m = n - 2
        k = 1000000007
        a, b = 2, m
        ans = 1
        while b:
            if b % 2:
                ans *= a
                ans %= k
            a *= a
            a %= k
            b //= 2
        print(ans)