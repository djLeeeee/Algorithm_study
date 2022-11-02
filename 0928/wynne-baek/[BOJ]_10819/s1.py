import sys
from itertools import permutations
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))

cases = list(permutations(A))
max_sum = 0
for case in cases:
    temp = 0
    for i in range(len(A)-1):
        temp += abs(case[i] - case[i+1])
    max_sum = max(temp, max_sum)
print(max_sum)
