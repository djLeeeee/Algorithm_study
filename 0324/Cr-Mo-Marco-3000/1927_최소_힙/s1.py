import heapq
from sys import stdin

T = int(stdin.readline().rstrip())

heap = []
for _ in range(T):
    order = int(stdin.readline().rstrip())
    if order == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, order)
