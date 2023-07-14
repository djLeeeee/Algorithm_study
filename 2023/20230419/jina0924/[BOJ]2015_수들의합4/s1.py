# 백준 2015번 수들의 합 4 - 시간초

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
if arr[0] == K:
    cnt += 1
for i in range(1, N):
    arr[i] += arr[i - 1]
    if arr[i] == K:
        cnt += 1
    for j in range(i):
        if arr[i] - arr[j] == K:
            cnt += 1

print(cnt)