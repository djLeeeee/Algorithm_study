# 동서남북 네방향에서 0의 개수만큼 줄어듬
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
tc = 0
while True:
    cnt = 0
    for i in range(n):  # 얼음 개수 확인
        for j in range(m):
            if arr[i][j]:
                cnt += 1
    if not cnt:
        print(0)

    ice = [[0] * m for _ in range(n)]
    btn = False
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                for d in di:
                    ni, nj = i + d[1], j + d[0]
                    if 0 <= ni < n and 0 <= nj < m and not arr[ni][nj]:
                        ice[i][j] += 1
                    if ice[i][j] >= arr[i][j]:
                        btn = True
                        cnt -= 1
                        break
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if ice[i][j]:
                arr[i][j] -= ice[i][j]
                if arr[i][j] and x == -1 and y == -1:
                    x, y = i, j
    tc += 1
    if btn: # 얼음 분리 되었는지 확인
        stack = [(x, y)]
        visited = [[0] * m for _ in range(n)]
        visited[x][y] = 1
        while stack:
            x, y = stack.pop()
            for d in di:
                nx, ny = x + d[1], y + d[0]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                    cnt -= 1
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
        if cnt:
            print(tc)
            break
