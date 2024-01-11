import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
t_list = [int(input()) for _ in range(n)]

start, end = min(t_list), max(t_list) * m
ans = end

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for t in t_list:
        # m이라는 시간동안 몇명을 심사할 수 있는지 count
        cnt += mid // t
    # 인원보다 더 많이 검사 가능하면 시간을 줄인다
    if cnt >= m:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)

