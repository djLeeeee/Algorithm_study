# 수업이 동일하게 시작하는 경우는 없다고 생각하기
import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : x[0])

heap = []
for a, b in arr:
    if not len(heap):
        heapq.heappush(heap, (b, a))
        continue
    heapq.heappush(heap, (b, a))
    if heap[0][0] <= a:
        heapq.heappop(heap)
print(len(heap))