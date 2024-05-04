import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n, l = map(int, input().split())
spots = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for x, y in animals:
    left, right = 0, m-1
    while left < right:
        mid = (left + right) // 2
        # 제일 가까운 spot 찾기
        if spots[mid] < x:
            left = mid+1
        else:
            right = mid
    # right는 x 좌표보다 크거나 같은 마지막 요소
    a_dist = abs(x-spots[right]) + y
    b_dist = abs(x-spots[right-1]) + y
    if a_dist <= l or b_dist <= l:
        ans += 1

print(ans)