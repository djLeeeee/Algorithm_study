import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n, k = map(int, input().split())
nums = list(map(int, input().split()))
sum_dict = defaultdict(int)
sum_dict[0] += 1
sum_num = 0
ans = 0
for num in nums:
    sum_num += num
    if sum_num - k in sum_dict.keys():
        ans += sum_dict[sum_num - k]
    sum_dict[sum_num] += 1
print(ans)