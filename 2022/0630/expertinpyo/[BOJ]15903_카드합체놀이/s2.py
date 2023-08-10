n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(m):
    x, y = arr[0], arr[1]
    arr[0] = arr[1] = x + y
    arr.sort()
print(sum(arr))