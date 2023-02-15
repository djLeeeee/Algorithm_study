# 백준 10800번 컬러볼 - 시간초과

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline

N = int(input())
balls = [0] * N
ans = [0] * N
for i in range(N):
    color, size = map(int, input().split())
    balls[i] = (color, size)
    for j in range(i):
        if balls[j][0] != color:
            if balls[j][1] < size:
                ans[i] += balls[j][1]
            elif balls[j][1] > size:
                ans[j] += size
print(*ans, sep='\n')