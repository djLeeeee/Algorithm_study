# 백준 1747번 소수&팰린드롬 - 통과

import sys
sys.stdin = open('input.txt')


def isPrime(n):
    if n == 1:
        return False
    for m in range(2, int(n ** 0.5) + 1):       # 배수인지 보려면 n의 제곱근까지만 돌면 됨
        if n % m == 0:
            return False
    return True


N = int(input())
num = N
while True:
    if str(num) == str(num)[::-1]:              # 해당 숫자가 팰린드롬인지 확인
        if isPrime(num):
            print(num)
            sys.exit()
    num += 1

