import sys
sys.stdin = open('input.txt')

def dfs(color, x, y, cnt, sx, sy):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if cnt >= 4 and nx == sx and ny == sy:
                print('Yes')
                exit()
            if arr[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(color, nx, ny, cnt+1, sx, sy)
                visited[nx][ny] = False

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
colors = []
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(arr[i][j], i, j, 1, i, j)

print('No')


