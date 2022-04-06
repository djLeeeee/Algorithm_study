import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = []
result = []
for _ in range(N):
    nums.append(sys.stdin.readline().strip())
nums.sort(key=int)
if N == 3:
    for i in range(N):
        for j in range(N):
            if i != j:
                num = nums[i] + nums[j]
                result.append(int(num))
else:
    for i in range(4):
        for j in range(4):
            if i != j:
                num = nums[i] + nums[j]
                result.append(int(num))
result = sorted(result)
print(result[2])