import sys
sys.stdin = open('input.txt')

def pass_target_idx(idx, l, r):
    if idx == l:
        a = l + 1
    else:
        a = l
    if idx == r:
        b = r - 1
    else:
        b = r
    return (a, b)

n = int(input())
nums = sorted(list(map(int, input().split())))

if n <= 2:
    print(0)
    exit()

ans = 0
for i in range(2, n):
    target = nums[i]
    l, r = pass_target_idx(i, 0, n-1)
    while l < r:
        tmp = nums[l] + nums[r]
        if tmp == target:
            ans += 1
            break
        elif tmp > target:
            r -= 1
        else:
            l += 1
        l, r = pass_target_idx(i, l, r)

print(ans)
