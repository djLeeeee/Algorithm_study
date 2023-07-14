# 백준 1041번 주사위

import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
ans = -1
if N <= 1:
    ans = sum(nums) - max(nums)
else:
    min_nums = []
    min_nums.append(min(nums[0], nums[5]))
    min_nums.append(min(nums[1], nums[4]))
    min_nums.append(min(nums[2], nums[3]))
    min_nums.sort()
    min_side = min_nums[0]
    min_corner = min_nums[0] + min_nums[1]
    min_apex = min_nums[0] + min_nums[1] + min_nums[2]
    apex_cnt = 4
    corner_cnt = (N - 2) * 4 + (N - 1) * 4
    side_cnt = (N - 2) * (N - 1) * 4 + (N - 2) ** 2
    ans = min_apex * apex_cnt + min_corner * corner_cnt + min_side * side_cnt
print(ans)