# 15903
# 가장 작은 숫자 2개를 찾아서 더한다
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(m):
    x, y = arr[0], arr[1]
    arr[0] = arr[1] = x + y
    for i in range(2, n-1):
        if arr[i] < arr[0]:
            if arr[i+1] < arr[0]:
                arr[0], arr[1], arr[i], arr[i+1] = arr[i], arr[i+1], arr[0], arr[1]
            elif arr[i+1] == arr[0]:
                arr[i], arr[0] = arr[0], arr[i]
            break
print(sum(arr))