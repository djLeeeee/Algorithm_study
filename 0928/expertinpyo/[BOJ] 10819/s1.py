N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 음수일 때 생각해보기
if not N % 2:
    for i in range(N):
        if i < N // 2:
            arr[i] *= -1
            if i != N//2 - 1:
                arr[i] *= 2
        elif i > N // 2:
            arr[i] *= 2
else:
    for i in range(N):
        if i <= N//2:
            arr[i] *= -1
            if i != N//2 and i != 0:
                arr[i] *= 2
        else:
            arr[i] *= 2
print(sum(arr))