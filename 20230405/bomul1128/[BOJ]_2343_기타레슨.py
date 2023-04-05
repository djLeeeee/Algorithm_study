n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = max(arr)
right = left * (n // m + 1)
ans = 0
while left <= right:
    cnt = 0
    stack = 0
    mid = (left + right) // 2
    for a in arr:
        if stack + a <= mid:
            stack += a
        else:
            stack = a
            cnt += 1
    cnt += 1
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
print(ans)
