from sys import stdin

input = stdin.readline

n, k, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
p = -1
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for a in arr:
        if k <= a < 2 * k:
            cnt += (a - k) // mid
        elif a >= 2 * k:
            cnt += (a - 2 * k) // mid
    if cnt >= m:
        p = mid
        start = mid + 1
    else:
        end = mid - 1
print(p)
