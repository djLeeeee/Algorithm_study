# https://www.acmicpc.net/problem/4179
import sys
sys.stdin = open("./input/4179.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------

# 불과 지훈이의 좌표를 구하는 함수
def get_cords(R, C, board):
    J, fires = None, []
    for i in range(R):
        for j in range(C):
            if board[i][j] == FIRE:
                fires.append((i, j))
            elif (board[i][j] == JIHOON):
                J = (i, j)
    return (J, fires)

def in_board(i, j):
    cond1 = 0 <= i < R
    cond2 = 0 <= j < C
    return cond1 and cond2

def get_next_cords(i, j):
    cords = []
    for way in range(4):
        ni, nj = i + di[way], j + dj[way]
        cords.append((ni, nj))
    return cords

def bfs(arr, vst):
    que = deque(arr)
    for (i, j) in arr:
        vst[i][j] = 1
        
    while que:
        ci, cj = que.popleft()
        for (ni, nj) in get_next_cords(ci, cj):
            if in_board(ni, nj) and board[ni][nj] != "#" and vst[ni][nj] == sys.maxsize:
                vst[ni][nj] = vst[ci][cj] + 1
                que.append((ni, nj))

def compare(i, j):
    jj = J_cnt[i][j]
    ff = F_cnt[i][j]
    return jj < ff

# ----------------------------------------
JIHOON = "J"
FIRE = "F"
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
# ----------------------------------------

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
J, fires = get_cords(R, C, board)

J_cnt = [[sys.maxsize] * C for _ in range(R)]
F_cnt = [[sys.maxsize] * C for _ in range(R)]

bfs([J], J_cnt)
bfs(fires, F_cnt)

min_val = sys.maxsize

for i in range(R - 1):
    if compare(i, 0):
        min_val = min(J_cnt[i][0], min_val)
    if compare(i, C - 1):
        min_val = min(J_cnt[i][C-1], min_val)

for j in range(C - 1):
    if compare(0, j):
        min_val = min(J_cnt[0][j], min_val)
    if compare(R - 1, j):
        min_val = min(J_cnt[R-1][j], min_val)

print(min_val if min_val != sys.maxsize else "IMPOSSIBLE")