import sys
sys.stdin = open('input.txt')

n = int(input())
num = n
max_len = 0
result = []
for i in range(1, n+1):
    ans = [n]
    ans.append(i)
    while num > 0:
        num = ans[-2] - ans[-1]
        if num > 0:
            ans.append(num)
        elif not num:
            ans.append(num)
            num = n
        else:
            num = n
            break
    if len(ans) > max_len:
        max_len = len(ans)
        result = ans
print(max_len)
print(*result)

