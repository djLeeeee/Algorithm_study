# 백준 1987 알파벳

import sys
sys.stdin = open('input1.txt')


def solution():
    global ans
    stack = [(0, 0, board[0][0])]

    while stack:
        cr, cc, res = stack.pop()
        ans = max(ans, len(res))

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < r and 0 <= nc < c and board[nr][nc] not in res:
                stack.append((nr, nc, res + board[nr][nc]))


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
solution()     # 좌상단에서 시작
print(ans)