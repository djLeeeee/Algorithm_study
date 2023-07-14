import sys

sys.stdin = open('input.txt')


def cal(x, y, order):
    if order == 0:
        return x + y
    elif order == 1:
        return x - y
    elif order == 2:
        return x * y
    else:
        if x < 0:
            x *= -1
            x //= y
            return -x
        else:
            return x // y


def dfs(ans, array, k):
    if k == n - 1:
        result.append(ans)
    for i in range(4):
        if array[i]:
            new = array[:]
            new[i] -= 1
            dfs(cal(ans, nums[k + 1], i), new, k + 1)


for tc in range(1, int(input()) + 1):
    n = int(input())
    orders = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    result = []
    dfs(nums[0], orders, 0)
    print(f'#{tc} {max(result) - min(result)}')
