# https://www.acmicpc.net/problem/2151
import sys
sys.stdin = open("./input/2151.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------
def find_doors():
    doors = []
    for i in range(N):
        for j in range(N):
            if BOARD[i][j] == DOOR:
                doors.append((i, j))
    return doors
    
    
def in_board(ni, nj):
    cond1 = 0 <= ni < N
    cond2 = 0 <= nj < N
    return cond1 and cond2

def bfs(start, vst):
    si, sj = start

    que = deque()
    for way in range(4):
        que.append((si, sj, way))
        
    vst[si][sj] = 1
    while que:
        ci, cj, cw = que.popleft()
        
        cv = vst[ci][cj]
        ni, nj = ci + di[cw], cj + dj[cw]
        while in_board(ni, nj):
            cond1 = BOARD[ni][nj] in (DOOR, MIRROR)
            cond2 = vst[ni][nj] > cv + 1
            
            if BOARD[ni][nj] == WALL:
                break

            if cond1 and cond2:
                vst[ni][nj] = cv + 1
                for way in range(4):
                    que.append((ni, nj, way))
            ni, nj = ni + di[cw], nj + dj[cw]
            

#-----------------------------------
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
MIRROR, DOOR, WALL = ["!", "#", "*"]
N = int(input())
END = N - 1
BOARD = [list(input().rstrip()) for _ in range(N)]
vst = [[sys.maxsize] * N for _ in range(N)]
#-----------------------------------
start, end = find_doors()
bfs(start, vst)
ei, ej = end
print(vst[ei][ej] - 2)