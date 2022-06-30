import sys
import heapq
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = list(map(int, input().split()))
heapq.heapify(nums)
# print(nums)
for i in range(M):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a + b)
    heapq.heappush(nums, a + b)
print(sum(nums))
