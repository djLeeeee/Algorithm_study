import sys
sys.stdin = open('input.txt')

N, r, c = map(int, input().split())
ans = 0
while N > 1:
    n = 2 ** (N-1)
    if r < n:
        if c < n:
            pass
        else:
            ans += n ** 2
            c -= n
    else:
        if c < n:
            ans += (n ** 2) * 2
        else:
            ans += (n ** 2) * 3
            c -= n
        r -= n
    N -= 1

if (r, c) == (0, 0):
    pass
elif (r, c) == (0, 1):
    ans += 1
elif (r, c) == (1, 0):
    ans += 2
else:
    ans += 3

print(ans)
