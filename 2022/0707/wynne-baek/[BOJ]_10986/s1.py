import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    num = 0
    for j in range(i, N):
        num += arr[j]
        if num % M == 0:
            cnt += 1
print(cnt)