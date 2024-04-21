def solution(land):
    n = len(land)
    m = len(land[0])
    get = [0] * m
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(n):
        for j in range(m):
            if land[i][j]:
                ys = {j}
                q = [(i, j)]
                land[i][j] = 0
                for x, y in q:
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny]:
                            ys.add(ny)
                            q.append((nx, ny))
                            land[nx][ny] = 0
                for y in ys:
                    get[y] += len(q)
    return max(get)
