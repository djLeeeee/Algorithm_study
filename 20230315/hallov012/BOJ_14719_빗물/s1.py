import sys, heapq
sys.stdin = open('input.txt')

h, w = map(int, input().split())
block = list(map(int, input().split()))
heap = []
ans = 0
for i in range(w-1):
    b = block[i]
    if not heap:
        heapq.heappush(heap, -b)
    else:
        max_b = -heapq.heappop(heap)
        if b < max_b:
            heapq.heappush(heap, -max_b)
            heapq.heappush(heap, -b)
        else:
            for num in heap:
                ans += max_b + num
            heap = []
            heapq.heappush(heap, -b)
for num in heap:
    if block[-1] + num > 0:
        ans += block[-1] + num
print(ans)
