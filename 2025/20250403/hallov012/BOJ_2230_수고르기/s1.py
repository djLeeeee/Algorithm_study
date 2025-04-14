import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

l, r = 0, 0
nums.sort()
ans = nums[-1] - nums[0]
while l < n and r < n:
    tmp = nums[r] - nums[l]
    if tmp >= m:
        ans = min(ans, tmp)
        l += 1
    else:
        r += 1
print(ans)