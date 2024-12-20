import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
upper = defaultdict(list)
for x in range(n):
    k = 0
    while x >= k:
        num = (x-k) * n + k
        upper[x].append(num)
        k += 1

lower = defaultdict(list)
