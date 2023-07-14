from sys import stdin

input = stdin.readline

n = int(input())
nums = [input().strip() for _ in range(n)]
nums.sort(key=lambda xx: int(xx))
result = []
if n == 3:
    for i in range(3):
        for j in range(3):
            if i != j:
                result.append(int(nums[i] + nums[j]))
else:
    for i in range(4):
        for j in range(4):
            if i != j:
                result.append(int(nums[i] + nums[j]))
result.sort()
print(result[2])
