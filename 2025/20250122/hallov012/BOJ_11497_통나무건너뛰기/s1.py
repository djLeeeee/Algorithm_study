import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline()

T = int(input())
for _ in range(T):
    n = int(input())
    h_lst = list(map(int, input().split()))
    h_lst.sort()

    lst = [0] * n
    k = n//2 if not n%2 else n//2+1
    for i in range(k):
        l, r = i*2, i*2+1

        lst[i] = h_lst[l]
        if r < n:
            lst[n-i-1] = h_lst[r]

    ans = 0
    for i in range(n):
        x, y = i, (i+1)%n
        ans = max(ans, abs(lst[x] - lst[y]))

    print(ans)
