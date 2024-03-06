import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def check(idx, cnt, diff):
    global ans
    if cnt >= ans:
        return
    if idx == n:
        ans = cnt
        return
    tmp = nums[idx] - nums[idx-1]
    if tmp == diff:
        check(idx+1, cnt, diff)
    elif tmp == diff + 1:
        nums[idx] -= 1
        check(idx+1, cnt+1, diff)
        nums[idx] += 1
    elif tmp == diff - 1:
        nums[idx] += 1
        check(idx+1, cnt+1, diff)
        nums[idx] -= 1
    else:
        return


n = int(input())
nums = list(map(int, input().split()))

if n <= 2:
    print(0)
    exit()

ans = n+1
d = [-1, 0, 1]

for i in range(3):
    nums[0] += d[i]
    for j in range(3):
        nums[1] += d[j]
        cnt = abs(d[i])
        cnt += abs(d[j])
        diff = nums[1] - nums[0]
        check(2, cnt, diff)
        nums[1] -= d[j]
    nums[0] -= d[i]


print(ans if ans != n+1 else -1)

