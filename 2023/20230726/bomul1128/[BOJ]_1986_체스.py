# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1986
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1986&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n, m = map(int, input().split())
queen = []
knight = []
pawn = []
nq, *qxy = map(int, input().split())
nk, *kxy = map(int, input().split())
np, *pxy = map(int, input().split())
for i in range(0, 2 * nq, 2):
    queen.append((qxy[i] - 1, qxy[i + 1] - 1))
for i in range(0, 2 * nk, 2):
    knight.append((kxy[i] - 1, kxy[i + 1] - 1))
for i in range(0, 2 * np, 2):
    pawn.append((pxy[i] - 1, pxy[i + 1] - 1))
board = [[1] * m for _ in range(n)]
for px, py in pawn:
    board[px][py] = -1
kdx = [1, 1, -1, -1, 2, 2, -2, -2]
kdy = [2, -2, 2, -2, 1, -1, 1, -1]
for kx, ky in knight:
    board[kx][ky] = -1
    for i in range(8):
        nx = kx + kdx[i]
        ny = ky + kdy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            board[nx][ny] = 0
qdx = [1, 1, 1, -1, -1, -1, 0, 0]
qdy = [1, 0, -1, 1, 0, -1, 1, -1]
for qx, qy in queen:
    board[qx][qy] = -1
    for i in range(8):
        nx = qx + qdx[i]
        ny = qy + qdy[i]
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1:
            board[nx][ny] = 0
            nx += qdx[i]
            ny += qdy[i]
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ans += 1
print(ans)
