def no_more_star(n):
    if n == 1:
        return ['*']
    if n == 2:
        return ['*', '***', '*****']
    x = no_more_star(n - 1)
    x.reverse()
    a = len(x)
    b = 2 * a + 1
    result = ['*'] * b
    for i in range(1, a):
        result[i] = '*' + ' ' * (2 * i - 1) + '*'
    for j in range(a):
        result[a + j] = '*' + ' ' * 2 * j + x[j] + ' ' * 2 * j + '*'
    result[-1] = '*' * (b * 2 - 1)
    return result


idx = int(input())
ans = no_more_star(idx)
length = len(ans)
if idx % 2:
    for p in range(length):
        print(' ' * (length - 1 - p), end='')
        print(ans[p])
else:
    for q in range(length):
        print(' ' * q, end='')
        print(ans[-q - 1])
