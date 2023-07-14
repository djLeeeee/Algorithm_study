# https://www.acmicpc.net/problem/20366
import sys
import itertools
sys.stdin = open("./input/20366.txt")
input = sys.stdin.readline

N = int(input())
snows = list(map(int, input().split()))
snows.sort()
answer = sys.maxsize

l, r = 0, len(snows) - 1
while r - l >= 3:
    outside = snows[l] + snows[r]
    inside = snows[l+1] + snows[r-1]
    gap = outside - inside
    
    if gap >= 0:
        r -= 1
    else:
        l += 1
    
    if abs(gap) < answer:
        answer = abs(gap)

print(answer)