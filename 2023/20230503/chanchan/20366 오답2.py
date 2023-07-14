# https://www.acmicpc.net/problem/20366
import sys
import itertools
sys.stdin = open("./input/20366.txt")
input = sys.stdin.readline

N = int(input())
snows = list(map(int, input().split()))
snows.sort()
answer = sys.maxsize

for i in range(N):
    for j in range(i + 3, N):
        l, r = i + 1, j -1
        while l < r:
            outside = snows[i] + snows[j]
            inside = snows[l] + snows[r]
            gap = outside - inside
            if abs(gap) < answer:
                answer = abs(gap)
            
            if gap >= 0:
                l += 1
            else:
                r -= 1
print(answer)