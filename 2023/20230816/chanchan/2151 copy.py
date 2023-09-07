# https://www.acmicpc.net/problem/2151
import sys
sys.stdin = open("./input/2151.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------
def find_doors():
    doors = []
    for way in range(2):
        ci = END * (way == 0)
        for cj in range(1, END):
            if BOARD[ci][cj] == DOOR:
                doors.append((ci, cj, way))

    for way in range(3, 5):
        cj = END * (way == 3)
        for ci in range(1, END):
            if BOARD[ci][cj] == DOOR:
                doors.append((ci, cj, way))
    return doors
    
    
def in_board(ni, nj):
    cond1 = 0 <= ni < N
    cond2 = 0 <= nj < N
    return cond1 and cond2

def bfs(start, end, vst):
    si, sj, sw = start
    ei, ej, ew = end

    que = deque([start])
    vst[si][sj] = 1
    while que:
        ci, cj, cw = que.popleft()
        cv = vst[ci][cj]
        ni, nj = ci + di[cw], cj + dj[cw]
        while in_board(ni, nj):
            print(ni, nj, vst[ni][nj])
            ni, nj = ci + di[cw], cj + dj[cw]
            cond1 = BOARD[ni][nj] in (DOOR, MIRROR)
            cond2 = vst[ni][nj] > cv + 1
            if cond1 and cond2:
                vst[ni][nj] = cv + 1
                for way in range(4):
                    que.append((ni, nj, way))
            ci, cj = ni, nj
            

#-----------------------------------
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
MIRROR = "!"
DOOR = "#"
N = int(input())
END = N - 1
BOARD = [list(input().rstrip()) for _ in range(N)]
vst = [[sys.maxsize] * N for _ in range(N)]
#-----------------------------------
start, end = find_doors()
bfs(start, end, vst)
