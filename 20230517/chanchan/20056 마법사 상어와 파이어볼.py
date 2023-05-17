# https://www.acmicpc.net/problem/20056'
from collections import deque
import math
import sys
sys.stdin = open("./input/20056.txt")
input = sys.stdin.readline
# ----------------------------------------

def solution():
    N, M, K = map(int, input().split())
    board = [[deque() for _ in range(N)] for _ in range(N)]
    
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    def get_next_cord(ball: set, s: int, d: int):
        ci, cj = ball
        ni = (ci + di[d] * s) % N
        nj = (cj + dj[d] * s) % N
        return (ni, nj)

    def move_balls(ci: int, cj: int):
        
        while board[ci][cj] and board[ci][cj][0][0] == 0:
            _, m, s, d = board[ci][cj].popleft()
            
            ni, nj = get_next_cord((ci, cj), s, d)
            board[ni][nj].append((1, m, s, d))
    
    def merge_and_split(ci: int, cj: int):
        flag, rm, rs, rd = 0, 0, 0, []
        while board[ci][cj]:
            _, m, s, d = board[ci][cj].popleft()
            rm += m
            rs += s
            rd.append(d)
        
        rm = math.floor(rm / 5)
        rs = math.floor(rs / len(rd))
        for ind in range(len(rd) - 1):
            if rd[ind] % 2 != rd[ind + 1] % 2:
                flag = 1
                break
        
        if rm:
            for n in range(4):
                board[ci][cj].append((0, rm, rs, flag + 2 * n))

    def set_not_moved(i, j):
        _, r, s, d = board[i][j].popleft()
        board[i][j].append((0, r, s, d))

    def step1():
        for i in range(N):
            for j in range(N):
                if (len(board[i][j])):
                    move_balls(i, j)

    def step2():
        for i in range(N):
            for j in range(N):
                length = len(board[i][j])
                if (length > 1):
                    merge_and_split(i, j)
                elif (length == 1):
                    set_not_moved(i, j)

    for _ in range(M):
        i, j, m, s, d = map(int, input().split())
        board[i-1][j-1].append((0, m, s, d))

    for _ in range(K):
        step1()
        step2()
            
    answer = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                answer += sum([info[1] for info in board[i][j]])
    print(answer)

solution()