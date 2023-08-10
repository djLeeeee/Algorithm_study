import sys
from collections import defaultdict
sys.stdin = open('input.txt')

"""
제거 우선 순위
1. 추천이 가장 적은 사진
2. 게시된 지 가장 오래된 사진 
"""
n = int(input())
m = int(input())
nums = list(map(int, input().split()))
cnt = defaultdict(int)
date = {}
stack = []

for i in range(m):
    num = nums[i]
    if num in stack:
        cnt[num] += 1
    else:
        if len(stack) == n:
            min_cnt = 1000
            min_date = 1000
            tmp = -1
            for x in stack:
                if cnt[x] < min_cnt:
                    min_cnt = cnt[x]
                    min_date = date[x]
                    tmp = x
                elif cnt[x] == min_cnt:
                    if min_date > date[x]:
                        min_date = date[x]
                        tmp = x
            del cnt[tmp]
            del date[tmp]
            stack.remove(tmp)
        stack.append(num)
        cnt[num] += 1
        date[num] = i

print(*sorted(stack))