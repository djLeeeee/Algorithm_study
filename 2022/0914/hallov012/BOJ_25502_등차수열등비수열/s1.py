import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def arithmetic_squence():
    d = nums[2] - nums[1]
    flag = True
    if d > 0:
        if total == n * (2*nums[1] + (n-1)*d) // 2:
            for i in range(3, n+1):
                if nums[i] - nums[i-1] != d:
                    flag = False
                    break
        else:
            flag = False
    else:
        flag = False
    return flag

def geometric_squence():
    r = nums[2] / nums[1]
    flag = True
    if r == int(r):
        if total == nums[1] * (r ** n - 1) // (r - 1):
            for i in range(3, n+1):
                if nums[i] / nums[i-1] != r:
                    flag = False
                    break
        else:
            flag = False
    else:
        flag = False
    return flag


n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
total = sum(nums)
ans = []
if arithmetic_squence():
    ans.append('+')
elif geometric_squence():
    ans.append('*')
else:
    ans.append('?')

for _ in range(m):
    idx, num = map(int, input().split())
    if num == nums[idx]:
        ans.append(ans[-1])
        continue
    total = total - nums[idx] + num
    nums[idx] = num
    if ans[-1] == '?':
        if arithmetic_squence():
            ans.append('+')
        elif geometric_squence():
            ans.append('*')
        else:
            ans.append('?')
    else:
        ans.append('?')

for i in range(1, m+1):
    print(ans[i])
