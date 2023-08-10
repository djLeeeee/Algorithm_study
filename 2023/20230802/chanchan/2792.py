# https://www.acmicpc.net/problem/2792
import sys
sys.stdin = open("./input/2792.txt")
input = sys.stdin.readline
# ----------------------------------------
import math

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]
s, e = 1, max(colors)

min_jeal = sys.maxsize
while s <= e:
    cnt = 0
    mid = (s + e) // 2
    for c in colors:
        cnt += math.ceil(c/mid)
        
    if cnt > N:
        s = mid + 1
    else:
        e = mid - 1
        min_jeal = min(min_jeal, mid)

print(min_jeal)