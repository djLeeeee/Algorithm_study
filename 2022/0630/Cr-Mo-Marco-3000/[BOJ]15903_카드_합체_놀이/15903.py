import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().strip().split())
heap = list(map(int, input().strip().split()))
heapq.heapify(heap)

for _ in range(M):
    v1 = heapq.heappop(heap)
    v2 = heapq.heappop(heap)
    v3 = v1 + v2
    heapq.heappush(heap, v3)
    heapq.heappush(heap, v3)

print(sum(heap))