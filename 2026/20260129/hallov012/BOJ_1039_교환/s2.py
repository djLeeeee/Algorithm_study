import sys
sys.stdin = open('input.txt')

from collections import deque

n, k = map(int, input().split())
ans = 0
que = deque([(n, 0)])
visited = set()

while que:
    now, cnt = que.popleft()
    if cnt == k:
        ans = max(ans, now)
        continue
    nums = list(map(int, str(now)))
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1, l):
            if i == 0 and nums[j] == 0:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            next = int(('').join(map(str, nums)))
            temp = (next, cnt+1)
            if temp not in visited:
                visited.add(temp)
                que.append(temp)
            nums[i], nums[j] = nums[j], nums[i]

print(ans if ans > 0 else -1)