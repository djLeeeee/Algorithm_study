import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
times = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

left, right = 0, max(times) * n
t = 0 # n번째 아이가 놀이기구에 타게 되는 시간
while left <= right:
    mid = (left + right) // 2
    cnt = m
    for time in times:
        cnt += mid // time
    if cnt >= n:
        t = mid
        right = mid - 1
    else:
        left = mid + 1

cnt = m
for time in times:
    cnt += (t-1) // time

for idx, time in enumerate(times):
    if t % time == 0:
        cnt += 1
    if cnt == n:
        print(idx+1)
        break