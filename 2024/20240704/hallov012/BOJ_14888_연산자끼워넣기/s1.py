import sys
sys.stdin = open('input.txt')

def find(idx, val):
    global max_num, min_num
    if idx == n:
        max_num = max(max_num, val)
        min_num = min(min_num, val)
        return

    for i in range(4):
        if cnt[i]:
            cnt[i] -= 1
            find(idx+1, calculate(i, val, nums[idx]))
            cnt[i] += 1

def calculate(o_idx, a, b):
    if o_idx == 0:
        return a + b
    elif o_idx == 1:
        return a - b
    elif o_idx == 2:
        return a * b
    elif o_idx == 3:
        tmp = abs(a) // abs(b)
        if a * b >= 0:
            return tmp
        else:
            return -tmp

n = int(input())
nums = list(map(int, input().split()))
# +, -, *, %
cnt = list(map(int, input().split()))

max_num, min_num = -sys.maxsize, sys.maxsize

find(1, nums[0])

print(max_num)
print(min_num)

