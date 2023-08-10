import sys, collections
input = sys.stdin.readline
N = int(input())
g = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

normal = 0
disabled = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            color = g[i][j]
            Q = collections.deque([(i, j)])
            while Q:
                r, c = Q.popleft()
                for w in range(4):
                    nr = r + dr[w]
                    nc = c + dc[w]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and g[nr][nc] == color:
                        visited[nr][nc] = 1
                        Q.append((nr, nc))
            normal += 1

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            visited[i][j] = 0
            Q = collections.deque([(i, j)])
            color = 'B'
            if g[i][j] == color:
                while Q:
                    r, c = Q.popleft()
                    for w in range(4):
                        nr = r + dr[w]
                        nc = c + dc[w]
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] and g[nr][nc] == color:
                            visited[nr][nc] = 0
                            Q.append((nr, nc))
                disabled += 1
            else:
                while Q:
                    r, c = Q.popleft()
                    for w in range(4):
                        nr = r + dr[w]
                        nc = c + dc[w]
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] and g[nr][nc] != color:
                            visited[nr][nc] = 0
                            Q.append((nr, nc))
                disabled += 1

print(normal, disabled)

