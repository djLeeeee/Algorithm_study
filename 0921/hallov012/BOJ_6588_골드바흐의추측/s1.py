import sys, math
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = 1000000
nums = [1] * (n+1)
nums[0] = nums[1] = 0
for i in range(2, int(math.sqrt(n))+1):
    if nums[i]:
        for j in range(2*i, n+1, i):
            nums[j] = 0
nums[2] = 0

while True:
    num = int(input())
    if not num:
        break
    for i in range(3, n+1):
        if nums[i]:
            if nums[num-i]:
                print(f'{num} = {i} + {num-i}')
                break


