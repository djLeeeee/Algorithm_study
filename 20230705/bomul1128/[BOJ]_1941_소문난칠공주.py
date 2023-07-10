# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1941
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1941&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from itertools import combinations

ans = 0
board = [input() for _ in range(5)]
cases = list(combinations(range(25), 7))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for case in cases:
    case = list(case)
    c = case.pop()
    pts = [(c // 5, c % 5)]
    tmp = 0
    for x, y in pts:
        if board[x][y] == 'S':
            tmp += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if nx * 5 + ny in case:
                    case.remove(nx * 5 + ny)
                    pts.append((nx, ny))
    if tmp >= 4 and len(pts) == 7:
        ans += 1
print(ans)
