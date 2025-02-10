import sys
sys.stdin = open('input.txt')

def find(idx):
    # 한 조각의 길이
    for i in range(1, (idx//2) + 1):
        if nums[-i:] == nums[-2*i: -i]:
            return False
    if idx == n:
        for i in range(n):
            print(nums[i], end='')
        return True
    for i in range(1, 4):
        nums.append(i)
        if find(idx+1):
            return True
        nums.pop()

n = int(input())
nums = []
find(0)