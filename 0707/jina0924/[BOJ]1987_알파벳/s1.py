# 백준 1987 알파벳

import sys
sys.stdin = open('input3.txt')


def solution(cr, cc, res):
    global ans
    if ans < len(res):          # 지금 살펴본 값이 최대 칸 수라면 갱신하기
        ans = len(res)

    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < r and 0 <= nc < c and board[nr][nc] not in res:
            solution(nr, nc, res + board[nr][nc])


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
solution(0, 0, board[0][0])     # 좌상단에서 시작
print(ans)