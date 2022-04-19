import sys, math
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())

# 에라토스테네스의 체
number = [1] * (n+1)
number[0] = number[1] = 0
for i in range(2, int(math.sqrt(n)) + 1):
    if number[i]:
        for j in range(2*i, n+1, i):
            number[j] = 0
for i in range(m, n+1):
    if number[i]:
        print(i)