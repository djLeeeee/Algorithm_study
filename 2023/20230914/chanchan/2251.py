# https://www.acmicpc.net/problem/2251
import sys
sys.stdin = open("./input/2251.txt")
input = sys.stdin.readline
from collections import deque
# 골5 ----------------------------------------

def pour(bottle1, bottle2):
    

def bfs(init):
    que = deque([(0, 0, init[2])])
    vst[0][0] = 1

    while que:
        b1, b2, b3 = que.popleft()
        b12, b21 = pour(b1, b2)
        b13, b31 = pour(b1, b3)
        b23, b32 = pour(b2, b3)

        

# ----------------------------------------

bottles = list(map(int, input().split()))
vst = [[-1] * (max(bottles) + 1) for _ in range(2)]

bfs(bottles)