import sys
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
nums = []
ans = 0
for _ in range(n):
    num = int(input())
    heapq.heappush(nums, num)

if n == 1:
    print(0)
else:
    while len(nums) > 1:
        cnt = heapq.heappop(nums) + heapq.heappop(nums)
        ans += cnt
        heapq.heappush(nums, cnt)
    print(ans)

# 합쳐둔 카드들의 크기가 그 다음 카드묶음 보다 항상 작지 않기 떄문에
# heap에 넣어서 또 다시 정렬해주어야 한다
