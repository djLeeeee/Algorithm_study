# https://www.acmicpc.net/problem/20529
import sys
sys.stdin = open("./input/20529.txt")
input = sys.stdin.readline
# ----------------------------------------
T = int(input())

for _ in range(T):
    ans = 999999
    N = int(input())
    
    if N > 32:
        print(0)
        continue

    MBTI = list(map(str, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                tmp = 0
                for ind in range(4):
                    a, b, c = MBTI[i][ind], MBTI[j][ind], MBTI[k][ind]
                    tmp += int(a != b) + int(b != c) + int (c != a)
                ans = min(tmp, ans)
                

    print(ans)