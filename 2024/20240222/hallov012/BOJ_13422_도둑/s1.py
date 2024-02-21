import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    money = list(map(int, input().split()))
    if n == m:
        if sum(money) < k:
            print(1)
        else:
            print(0)
        continue

    tmp = sum(money[:m])
    ans = 0
    if tmp < k:
        ans += 1
    # l:삭제할 인덱스, r: 추가할 인덱스
    l, r = 0, m
    while l < n-1:
        tmp -= money[l]
        if r == n:
            r -= n
        tmp += money[r]
        if tmp < k:
            ans += 1
        l += 1
        r += 1
    print(ans)