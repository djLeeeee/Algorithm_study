# 백준 25502번 등차수열? 등비수열? - 시간초과

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 수열의 길이 / M: 연산의 개수
arr = list(map(int, input().split()))
for _ in range(M):
    i, x = map(int, input().split())
    arr[i-1] = x
    d, r = arr[1] - arr[0], arr[1] / arr[0]
    ans = '+'
    if d <= 0:
        ans = '*'
        if r <= 0:
            ans = '?'
            print(ans)
            continue
    for i in range(2, N):
        if arr[i] - arr[i-1] != d:
            ans = '*'
            if arr[i] / arr[i-1] != r:
                ans = '?'
                break
    print(ans)