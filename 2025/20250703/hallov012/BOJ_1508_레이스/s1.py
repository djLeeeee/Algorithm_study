import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
position = list(map(int, input().split()))

ans = ''
left, right, mid = 0, n, 0
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    arr = '1'
    prev = position[0]
    for i in range(1, k):
        if position[i] - prev >= mid:
            cnt += 1
            arr += '1'
            prev = position[i]
        else:
            arr += '0'
        if cnt == m:
            break
    # 정해진 심판의 수만큼 설 수 없다면 right를 줄이기
    if cnt < m:
        right = mid - 1
    else:

        left = mid + 1

print(ans)