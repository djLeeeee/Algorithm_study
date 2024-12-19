import sys
sys.stdin = open('input.txt')

N, M, L = map(int, input().split())
l_lst = sorted([0] + list(map(int, input().split())) + [L])
s, e = 1, L-1
ans = 0
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in range(1, N+2):
        d = l_lst[i] - l_lst[i-1]
        if d > m:
            cnt += (d-1) // m
    if cnt > M:
        s = m+1
    else:
        ans = m
        e = m-1
print(ans)
