import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
d_dict = defaultdict(int)
r_dict = defaultdict(int)
for i in range(1, n):
    d_dict[nums[i]-nums[i-1]] += 1
    r_dict[nums[i]/nums[i-1]] += 1

for _ in range(m):
    idx, num = map(int, input().split())
    idx -= 1

    if idx > 0:
        d_dict[nums[idx] - nums[idx-1]] -= 1
        r_dict[nums[idx] / nums[idx-1]] -= 1

    if idx < n-1:
        d_dict[nums[idx+1] - nums[idx]] -= 1
        r_dict[nums[idx + 1] / nums[idx]] -= 1

    nums[idx] = num
    if idx > 0:
        d_dict[nums[idx] - nums[idx-1]] += 1
        r_dict[nums[idx] / nums[idx-1]] += 1
    if idx < n-1:
        d_dict[nums[idx+1] - nums[idx]] += 1
        r_dict[nums[idx+1] / nums[idx]] += 1

    if d_dict[nums[1]-nums[0]] == n-1 and nums[1] - nums[0] > 0:
        print('+')
    elif r_dict[nums[1]/nums[0]] == n-1 and nums[1]/nums[0] == int(nums[1]/nums[0]):
        print('*')
    else:
        print('?')