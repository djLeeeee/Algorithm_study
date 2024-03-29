# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2636
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2636&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ini = fin = sum(sum(line) for line in board)
t = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while fin:
    t += 1
    q = [(0, 0)]
    melt = []
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    for x, y in q:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if not board[nx][ny]:
                    q.append((nx, ny))
                else:
                    melt.append((nx, ny))
    for x, y in melt:
        board[x][y] = 0
    ini = fin
    fin = sum(sum(line) for line in board)
print(t)
print(ini)
