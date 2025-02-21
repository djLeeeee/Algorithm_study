# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/7569
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=7569&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
h, m, n = map(int, input().split())
board = []
for _ in range(n):
    floor = [list(map(int, input().split())) for _ in range(m)]
    board.append(floor)
q = []
visited = [[[False] * h for _ in range(m)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        for z in range(h):
            if board[x][y][z] == 1:
                q.append((x, y, z))
                visited[x][y][z] = True
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for x, y, z in q:
    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and not visited[nx][ny][nz] and board[nx][ny][nz] == 0:
            visited[nx][ny][nz] = True
            board[nx][ny][nz] = board[x][y][z] + 1
            q.append((nx, ny, nz))
ans = 0
for x in range(n):
    for y in range(m):
        for z in range(h):
            if board[x][y][z] == 0:
                print(-1)
                exit()
            ans = max(ans, board[x][y][z])
print(ans - 1)
