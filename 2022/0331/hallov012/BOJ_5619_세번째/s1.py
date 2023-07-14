import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
ans = []
nums = [int(input().strip()) for _ in range(n)]
nums.sort()
if len(nums) == 3:
    for i in range(n):
        for j in range(n):
            if i != j:
                ans.append(int(str(nums[i]) + str(nums[j])))
else:
    for i in range(4):
        for j in range(4):
            if i != j:
                ans.append(int(str(nums[i]) + str(nums[j])))
ans.sort()
print(ans[2])
