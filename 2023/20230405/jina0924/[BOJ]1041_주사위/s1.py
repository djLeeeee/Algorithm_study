# 백준 1041번 주사위

import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
apexes = ((0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5))
corners = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5))
ans = -1
if N <= 1:
    ans = sum(nums) - max(nums)
else:
    min_apex, min_corner = 150, 100             # 3면의 합의 최소, 2면의 합의 최소
    for apex in apexes:
        tmp1 = nums[apex[0]] + nums[apex[1]] + nums[apex[2]]
        min_apex = min(min_apex, tmp1)
    for corner in corners:
        tmp2 = nums[corner[0]] + nums[corner[1]]
        min_corner = min(min_corner, tmp2)
    apex_cnt = 4                                # 상단 네 꼭짓점
    corner_cnt = (N - 2) * 4 + (N - 1) * 4      # 꼭짓점을 제외한 정육면체 각 모서리
    side_cnt = (N - 2) * (N - 1) * 4 + (N - 2) ** 2
    ans = min_apex * apex_cnt + min_corner * corner_cnt + min(nums) * side_cnt
print(ans)