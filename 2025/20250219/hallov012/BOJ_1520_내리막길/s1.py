import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[x][y] > arr[nx][ny]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0, 0)
print(visited[0][0])