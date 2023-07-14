# 백준 3085번 사탕 게임

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def counting():
    global ans

    for r in range(N):
        # 가로
        cnt = 0
        color = board[r][0]
        for c in range(N):
            if board[r][c] == color:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
                color = board[r][c]
        ans = max(ans, cnt)

        # 세로
        cnt = 0
        color = board[0][r]
        for c in range(N):
            if board[c][r] == color:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
                color = board[c][r]
        ans = max(ans, cnt)


ans = 0
for r in range(N):
    for c in range(N):
        color = board[r][c]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != color:
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                counting()
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
print(ans)