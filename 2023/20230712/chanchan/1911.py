# https://www.acmicpc.net/problem/1911
import sys
import math
sys.stdin = open("./input/1911.txt")
input = sys.stdin.readline
# ----------------------------------------
N, L = map(int, input().split())

waters = [list(map(int, input().split())) for _ in range(N)]
waters.sort()

cnt = 0
cur = 0
for (s, e) in waters:
    if (e <= cur):
        continue

    cur = s if cur < s else cur
    board = math.ceil((e - cur) / L)
    
    cur += board * L
    cnt += board
print(cnt)
