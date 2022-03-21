import heapq
from sys import stdin as s

input = s.readline

N = int(input())
heap = []
for _ in range(N):
    a = int(input())
    if a:
        heapq.heappush(heap, a)
    else:
        try:
            x = heapq.heappop(heap)
        except IndexError:
            x = 0
        print(x)
