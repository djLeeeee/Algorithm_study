# https://www.acmicpc.net/problem/3085'
import sys
sys.stdin = open("./input/3085.txt")
input = sys.stdin.readline
# ----------------------------------------
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
ans = 0 

def swap(board, i, j, flag):
    if flag:
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    else:
        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
    

def check(board):
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(N):
            cond = board[i][j] == board[i][j - 1]
            cnt = cnt + 1 if cond else 1
            max_cnt = max(cnt, max_cnt)
        
        cnt = 1
        for j in range(N):
            cond = board[j][i] == board[j - 1][i]
            cnt = cnt + 1 if cond else 1
            max_cnt = max(cnt, max_cnt)
    return max_cnt


for i in range(N):
    for j in range(N):
        if (i + 1) < N:
            swap(board, i, j, 0)
            ans = max(ans, check(board))
            swap(board, i, j, 0)
        if (j + 1) < N:
            swap(board, i, j, 1)
            ans = max(ans, check(board))
            swap(board, i, j, 1)

print(ans)