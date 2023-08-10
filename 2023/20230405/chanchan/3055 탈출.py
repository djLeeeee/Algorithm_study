# https://www.acmicpc.net/problem/3055
from collections import deque
import copy
import sys
sys.stdin = open("input/3055.txt")
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
distances = [[0] * C for _ in range(R)]
que = deque()

def isInBoard(i, j):
    cond1 = 0<=i<R
    cond2 = 0<=j<C
    return cond1 and cond2

def bfs(i, j):
    while que:
        ci, cj = que.popleft()
        if board[i][j] == "S":
            return distances[i][j]
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if isInBoard(ni, nj):
                if (board[ni][nj] == "." or board[ni][nj]=="D") and board[ci][cj] == "S":
                    board[ni][nj] = "S"
                    distances[ni][nj] = distances[ci][cj] + 1
                    que.append((ni, nj))
                elif (board[ni][nj] == "." or board[ni][nj] == "S") and board[ci][cj] == "*":
                    board[ni][nj] = "*"
                    que.append((ni, nj))
    return "KAKTUS"

for i in range(R):
    for j in range(C):
        if board[i][j] == "S":
            que.append((i, j))
        elif board[i][j] == "D":
            goal = (i, j)

for i in range(R):
    for j in range(C):
        if board[i][j] == "*":
            que.append((i, j))

answer = bfs(*goal)
print(answer)