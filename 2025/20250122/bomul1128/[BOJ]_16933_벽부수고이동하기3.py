# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/16933
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=16933&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dist = defaultdict(int)
for dk in range(0, k + 1):
    dist[(0, 0, dk)] = 1
q = [(0, 0, 0, 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for x, y, t, d in q:
    if dist[(x, y, t)] < d:
        continue
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1 and t < k:
            dd = 1 if d % 2 else 2
            if dist[(nx, ny, t + 1)] == 0 or dist[(nx, ny, t + 1)] > d + dd:
                for dt in range(t + 1, k + 1):
                    dist[(nx, ny, dt)] = d + dd
                q.append((nx, ny, t + 1, d + dd))
        elif board[nx][ny] == 0:
            if dist[(nx, ny, t)] == 0 or dist[(nx, ny, t)] > d + 1:
                for dt in range(t, k + 1):
                    dist[(nx, ny, dt)] = d + 1
                q.append((nx, ny, t, d + 1))
entry = []
for t in range(k + 1):
    if dist[(n - 1, m - 1, t)] > 0:
        entry.append(dist[(n - 1, m - 1, t)])
print(min(entry) if entry else -1)
