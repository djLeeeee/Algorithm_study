def dfs(x, y, cnt):
    if visited[x][y]:
        return visited[x][y]
    visited[x][y] = cnt
    nx, ny = di[arr[x][y]][1] + x, di[arr[x][y]][0] + y
    visited[x][y] = dfs(nx, ny, cnt)
    return visited[x][y]

di = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans = max(dfs(i, j, ans+1), ans)
# print(visited)
print(ans)