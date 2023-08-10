# 백준 5525번 IOIOI

import sys
sys.stdin = open('input2.txt')

N = int(input())
P = 'I' + 'OI' * N
length = int(input())
S = input()
cnt = 0
for i in range(length - 2 * N):
    tmp = S[i : i + 2 * N + 1]
    if tmp == P:
        cnt += 1
print(cnt)