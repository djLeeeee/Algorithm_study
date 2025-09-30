import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))

ans = nums[0] + nums[n-1]
l, r = 0, n-1

while l < r:
    tmp = nums[l] + nums[r]
    if abs(tmp) < abs(ans):
        ans = tmp
    if tmp < 0:
        l += 1
    else:
        r -= 1

print(ans)
