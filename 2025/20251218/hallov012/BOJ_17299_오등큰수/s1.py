import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
cnt = defaultdict(int)
stack = []
ans = [-1] * n

for num in nums:
    cnt[num] += 1

for idx, num in enumerate(nums):
    # 앞에 있는 것들 중 나온 횟수가 더 작은애 찾기
    while stack and cnt[nums[stack[-1]]] < cnt[num]:
        ans[stack.pop()] = num
    stack.append(idx)

print(*ans)