import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = n+1
tmp = 0
left = 0

for right in range(n):
    tmp += nums[right]
    while tmp >= s:
        ans = min(ans, right-left+1)
        tmp -= nums[left]
        left += 1

print(ans if ans != n+1 else 0)