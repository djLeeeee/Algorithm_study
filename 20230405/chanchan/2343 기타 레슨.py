# https://www.acmicpc.net/problem/2343
import sys
sys.stdin = open("input/2343.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
videos = list(map(int, input().split()))

start = 0
end = 100_000 * 10_000
result = sum(videos)

while start <= end:
    mid = (start + end) // 2
    if mid < max(videos):
        start = mid + 1
        continue
    cnt, tmp = 1, 0

    for i in range(len(videos)):
        if tmp + videos[i] <= mid:
            tmp += videos[i]
        
        else:
            tmp = videos[i]
            cnt += 1
    if cnt <= M:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
print(result)
