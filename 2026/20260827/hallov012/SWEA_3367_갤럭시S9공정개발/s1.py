import sys
sys.stdin = open('input.txt')

T = int(input())
INF = 10 ** 30
for tc in range(1, T+1):
    k = int(input())
    files = list(map(int, input().split()))

    arr = [INF] + files + [INF]
    ans = 0

    while len(arr) > 3:
        i = 1
        # arr[i-1] <= arr[i+1] 을 만족하는 위치 탐색
        while arr[i-1] > arr[i+1]:
            i += 1
        # i-1, i 합치기
        merged = arr[i-1] + arr[i]
        ans += merged

        del arr[i-1:i+1]
        j = i-2
        while arr[j] < merged:
            j -= 1
        arr.insert(j+1, merged)

    print(f"#{tc} {ans}")
