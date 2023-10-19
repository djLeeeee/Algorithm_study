# https://www.acmicpc.net/problem/18405
import sys
sys.stdin = open("./input/18405.txt")
input = sys.stdin.readline

from collections import deque 
# 골5 ----------------------------------------
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def get_cords_init(board):
    ret_val = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                ret_val.append((board[i][j], i, j))
    ret_val.sort(key = lambda x: x[0])
    return ret_val

def in_board(i, j):
    cond1 = 0 <= i < N
    cond2 = 0 <= j < N
    return cond1 and cond2


def get_next_cords(board, i, j):
    ret_val = []
    for way in range(4):
        ni, nj = i + di[way], j + dj[way]
        if in_board(ni, nj) and board[ni][nj] == 0 :
            board[ni][nj] = board[i][j]
            ret_val.append((ni, nj))
    return ret_val

# input 정보들 ---------------------------
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time_limit, X, Y = map(int, input().split())

# ----------------------------------------
que = deque(get_cords_init(board))

while time_limit > 0 and que:
    time_limit -= 1
    next_que = deque()
    while que:
        cv, ci, cj = que.popleft()
        for (ni, nj) in get_next_cords(board, ci, cj):
            next_que.append((cv, ni, nj))
    que = next_que
    
print(board[X - 1][Y - 1])


