import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
time = list(map(int, input().split()))
left, right = max(time), sum(time)
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    temp = 0
    for t in time:
        if temp + t > mid:
            temp = t
            cnt += 1
        else:
            temp += t
    # 갯수가 m보다 작으면 영상 길이를 줄인다
    if cnt <= m:
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)