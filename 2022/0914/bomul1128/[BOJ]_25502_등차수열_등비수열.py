from sys import stdin

input = stdin.readline


def check(idx, val=1):
    res = [0, 0]
    if arr[idx - 1] + arr[idx + 1] == 2 * arr[idx]:
        res[0] = val
    if arr[idx - 1] * arr[idx + 1] == arr[idx] * arr[idx]:
        res[1] = val
    return res


n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
add = 0
mul = 0
for i in range(1, n - 1):
    x, y = check(i)
    add += x
    mul += y
for _ in range(m):
    i, new = map(int, input().split())
    for j in range(i - 2, i + 1):
        if 0 < j < n - 1:
            x, y = check(j, - 1)
            add += x
            mul += y
    arr[i - 1] = new
    for j in range(i - 2, i + 1):
        if 0 < j < n - 1:
            x, y = check(j)
            add += x
            mul += y
    if add == n - 2 and arr[1] > arr[0]:
        print('+')
    elif mul == n - 2 and not arr[1] % arr[0]:
        print('*')
    else:
        print('?')
