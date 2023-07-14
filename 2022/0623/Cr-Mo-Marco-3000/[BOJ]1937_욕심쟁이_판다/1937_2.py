import sys

input = sys.stdin.readline

def do(r, c, cnt):
    global ans
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N and g[nr][nc] > g[r][c]:
            if visited[nr][nc] == 1:
                do(nr, nc, cnt + 1)
            else:
                visited[i][j] = max(visited[i][j], cnt + visited[nr][nc])
                ans = max(ans, cnt + visited[nr][nc])
    else:
        ans = max(ans, cnt)
        visited[i][j] = max(visited[i][j], cnt)

N = int(input().strip())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

g = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[1] * N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        do(i, j, 1)
print(ans)
