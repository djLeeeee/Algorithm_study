import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    nlst = list(map(int, input().split()))
    cnt = 0
    num = sum(nlst[:M])
    if num < K:
        cnt += 1
    for i in range(M, N+M-1):
        f, r = (i-M)%N, i%N
        if f != r:
            num += nlst[r]-nlst[f]
            if num < K:
                cnt += 1
    print(cnt)
