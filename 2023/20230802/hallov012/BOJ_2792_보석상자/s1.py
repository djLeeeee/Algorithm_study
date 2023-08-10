import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(m)]
left, right = 1, max(jewel)
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for j in jewel:
        cnt += j // mid
        if j % mid:
            cnt += 1
    # 보석이 남는다 => 더 나눠줄 수 있음
    if cnt > n:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)