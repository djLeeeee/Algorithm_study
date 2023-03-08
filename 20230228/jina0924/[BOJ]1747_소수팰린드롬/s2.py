# 백준 1747번 소수&팰린드롬 - 시간초과

import sys

N = int(input())
prime = set(range(2, N + 1))
for n in range(2, int(N ** 0.5) + 1):
    for m in range(2, int(N ** 0.5) + 1):
        num = n * m
        if num in prime:
            prime.remove(num)
ans = N
while True:
    isPrime = True
    for p in prime:
        if ans % p == 0:
            isPrime = False
            break
    if isPrime:
        if str(ans) == str(ans)[::-1]:
            print(ans)
            sys.exit()
        prime.add(ans)
    ans += 1