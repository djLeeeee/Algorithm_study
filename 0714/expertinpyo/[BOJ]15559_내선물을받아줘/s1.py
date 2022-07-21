def dfs(ax, ay):
    stack = [(ax, ay)]
    while stack:
        x, y = stack.pop()
        pos.append((x, y))
        if arr[x][y] == 'N':
            nx, ny = x - 1, y
        elif arr[x][y] == 'S':
            nx, ny = x + 1, y
        elif arr[x][y] == 'W':
            nx, ny = x, y - 1
        else:
            nx, ny = x, y + 1
        if 0 <= nx < N and 0 <= ny < M:
            if not checked[nx][ny]:
                if nx == ay and ny == ay:
                    return True
                stack.append((nx, ny))
            else:
                return False

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = 0
checked = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not checked[i][j]:
            if dfs(i, j):
                ans += 1
                checked[i][j] = ans
            else:
                checked[i][j] = -1

print(ans)