# https://www.acmicpc.net/p roblem/1041
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

if N == 1:
    answer = sum(nums) - max(nums)
    
else:    
    temp = []
    temp.append(min(nums[0], nums[5]))
    temp.append(min(nums[1], nums[4]))
    temp.append(min(nums[2], nums[3]))
    
    min_values= sorted(temp)
    n1 = min_values[0]
    n2 = n1 + min_values[1]
    n3 = n2 + min_values[2]

    cnt1 = (N - 2) * (N - 2) + 4* ( N - 1) * (N - 2)
    cnt2 = 4 * (N - 2) + 4 * (N - 1)
    cnt3 = 4

    tot = n1 * cnt1 + n2 * cnt2 + n3 * cnt3
    answer = tot

print(answer)