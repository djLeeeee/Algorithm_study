import sys, math
sys.stdin = open('input.txt')

n = int(input())
m = 1500000
nums = [1] * (m+1)
nums[0] = nums[1] = 0
for i in range(2, int(m**0.5)+1):
    if nums[i]:
        for j in range(2*i, m+1, i):
            nums[j] = 0

ans = 0
for i in range(n, m):
    if nums[i]:
        temp = str(i)
        if temp == temp[::-1]:
            ans = temp
            break

print(ans)