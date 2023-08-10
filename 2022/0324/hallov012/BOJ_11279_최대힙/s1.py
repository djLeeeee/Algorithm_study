import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1 * m)
