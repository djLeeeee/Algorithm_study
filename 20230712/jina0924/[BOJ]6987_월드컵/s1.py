# 6987번 월드컵 - x

import sys
sys.stdin = open('input.txt')

for _ in range(4):
    data = list(map(int, input().split()))
    total_win, total_draw, total_lose, draw_cnt = 0, 0, 0, 0
    ans = 1
    for m in range(1, 18, 3):
        win, draw, lose = data[m-1], data[m], data[m+1]
        if win + draw + lose != 5:
            ans = 0
            break
        total_win += win
        total_draw += draw
        total_lose += lose
        if draw:
            draw_cnt += 1
    if draw_cnt % 2 or total_win != total_lose or total_win + total_draw + total_lose != 30:
        ans = 0
    print(ans, end=' ')