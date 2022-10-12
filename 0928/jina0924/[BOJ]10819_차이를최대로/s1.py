# 백준 10819번 차이를 최대로

import sys
sys.stdin = open('input.txt')
from itertools import permutations as p

N = int(input())
arr = list(map(int, input().split()))
ans = 0
for pp in p(arr, N):
    res = 0
    for i in range(1, N):
        res += abs(pp[i] - pp[i-1])
    if ans < res:
        ans = res
print(ans)