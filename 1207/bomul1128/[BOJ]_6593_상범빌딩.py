from sys import stdin

input = stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while True:
    n, m, h= map(int, input().split())
    if n == m == h == 0:
        break
    building = []
    for _ in range(n):
        board = [list(input().strip()) for _ in range(m)]
        building.append(board)
        input()
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if building[i][j][k] == 'S':
                    start = (i, j, k)
                    building[i][j][k] = '#'
                    break
            
    point = [start]
    flag = True
    t = 0
    while point and flag:
        new = []
        t += 1
        for x, y, z in point:
            for d in range(6):
                nx = x + dx[d]
                ny = y + dy[d]
                nz = z + dz[d]
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    adj = building[nx][ny][nz]
                    if adj == '.':
                        new.append((nx, ny, nz))
                    elif adj == 'E':
                        flag = False
                    building[nx][ny][nz] = '#'
        point = new
    print(f"Escaped in {t} minute(s)." if not flag else "Trapped!")
