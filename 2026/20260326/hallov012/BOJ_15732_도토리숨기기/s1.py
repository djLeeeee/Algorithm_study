import sys
sys.stdin = open('input.txt')

def check(target):
    res = 0
    for a, b, c in rules:
        if target < a:
            continue
        b = min(b, target)
        res += (b-a) // c + 1
    return res >= d

n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

l, r = 0, n
while l < r:
    m = (l+r) // 2
    if check(m):
        r = m
    else:
        l = m+1

print(r)