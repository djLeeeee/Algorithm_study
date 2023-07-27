# https://www.acmicpc.net/problem/1986
import sys
sys.stdin = open("./input/1986.txt")
input = sys.stdin.readline
# ----------------------------------------
from itertools import combinations, product

# 기본 보드(체스판) 설정
N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

# knight, queen 의 이동 경로/방향 저장
knight_move = list((a, b) for (a, b) in product([2, -2, 1, -1], repeat=2) if abs(a) != abs(b))
queen_move = list(product([1, -1, 0], repeat=2))

# 체스 기물 정보 저장
chess_pieces = [[] for _ in range(3)]
for kind in range(3):
    nums, *cords = list(map(int, input().split()))

    for ind in range(nums):
        i, j = map(lambda x: x - 1, cords[ind * 2:ind * 2+2])
        board[i][j] = kind + 1
        chess_pieces[kind].append((i, j))

# 체스 움직임
for kind in range(2):
    pieces = chess_pieces[kind]
    
    if kind == 1:
        for (ci, cj) in pieces:
            for (di, dj) in knight_move:
                ni, nj = ci + di, cj + dj
                if (0 <= ni < N and 0 <= nj < M and board[ni][nj] <= 0):
                    board[ni][nj] = -1
        continue

    for (i, j) in pieces:
        for (di, dj) in queen_move:
            ci, cj = i, j
            while True:
                ni, nj = ci + di, cj + dj
                if (0 <= ni < N and 0 <= nj < M and board[ni][nj] <= 0):
                    board[ni][nj] = -1
                    ci, cj = ni, nj
                else:
                    break

ans = 0
for line in board:
    ans += line.count(0)

print(ans)
