import sys
sys.stdin = open('input.txt')

N = int(input())

def func(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    lst = func(n//2)
    res = []
    for l in lst:
        res.append(' '*(n//2)+l+' '*(n//2))

    for l in lst:
        res.append(l+' '+l)

    return res

ans = func(N)
for r in ans:
    print(r)