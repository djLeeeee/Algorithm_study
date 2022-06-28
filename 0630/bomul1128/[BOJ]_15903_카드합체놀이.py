from sys import stdin
from heapq import *

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)
for _ in range(m):
    s = heappop(arr) + heappop(arr)
    heappush(arr, s)
    heappush(arr, s)
print(sum(arr))