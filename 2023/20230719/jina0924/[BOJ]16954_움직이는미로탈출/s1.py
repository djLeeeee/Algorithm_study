# 백준 16954번 움직이는 미로 탈출

import sys
sys.stdin = open('input.txt')
from collections import deque


def move():
    dr, dc = (0, -1, -1, 0, 0, -1, -1, 1, 1), (0, 0, 0, -1, 1, -1, 1, 1, -1)

    while queue:
        cr, cc, piece = queue.popleft()
        if piece == '*' and board[cr][cc] != '#':
            board[cr][cc] = '.'
            for d in range(8):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] != '#':
                    if nr == 0 and nc == 7:
                        return 1
                    board[nr][nc] = piece
                    queue.append((nr, nc, piece))
        elif piece == '#':
            board[cr][cc] = '.'
            nr = cr + 1
            if 0 <= nr < 8:
                board[nr][cc] = piece
                queue.append((nr, cc, piece))

    return 0


board = [list(input()) for _ in range(8)]
queue = deque([(7, 0, '*')])
for r in range(7, -1, -1):
    for c in range(8):
        if board[r][c] == '#':
            queue.append((r, c, '#'))
print(move())