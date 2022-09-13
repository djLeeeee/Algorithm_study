import sys
sys.stdin = open('input.txt')

string = input().split('-')
nums = []
for a in string:
    if '+' in a:
        plus_nums = a.split('+')
        plus_nums = list(map(int, plus_nums))
        nums.append(sum(plus_nums))
    else:
        nums.append(int(a))
ans = nums[0]
if len(nums) > 1:
    for i in range(1, len(nums)):
        ans -= nums[i]
print(ans)
