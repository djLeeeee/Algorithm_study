# 백준 10993번 별 찍기-18

import sys
input = sys.stdin.readline


def star(n, start):
    if n == 0:
        return
    hh, ww = size[n][0], size[n][1]         # hh, ww: n일 때 삼각형 가로, 세로 길이
    m = (w - 1) // 2                        # board의 가운데
    r = start
    k = 0                                   # 별 간격을 위한 변수
    if n % 2:
        while hh > 1:                       # 삼각형 밑변을 제외한 모서리 그리기
            board[r][m-k] = board[r][m+k] = '*'
            r += 1
            k += 1
            hh -= 1
        board[r][m] = '*'
        while k:                            # 삼각형 밑변 그리기
            board[r][m-k] = board[r][m+k] = '*'
            k -= 1
        star(n-1, r-1)                      # 그 다음 삼각형의 한 변의 길이는 짝수 => 역삼각형 => 밑변 바로 위에서 시작
    if n % 2 == 0:
        while hh > 1:
            board[r][m-k] = board[r][m+k] = '*'
            r -= 1
            k += 1
            hh -= 1
        board[r][m] = '*'
        while k:
            board[r][m - k] = board[r][m + k] = '*'
            k -= 1
        star(n-1, r+1)


N = int(input())

size = [(0, 0), (1, 1)]                     # n일 때 삼각형 가로, 세로 길이 담을 리스트
h = w = cnt = 1
while cnt < N:
    h = h * 2 + 1
    w = 2 * h - 1
    size.append((h, w))
    cnt += 1

board = [[' '] * w for _ in range(h)]
print(board)
if N % 2:                                   # N이 홀수면 삼각형
    star(N, 0)
elif N % 2 == 0:                            # N이 짝수면 역삼각형
    star(N, h-1)
for line in board:
    print(''.join(line).rstrip())
