import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
hx, hy = map(lambda v: int(v)-1, input().split())
ex, ey = map(lambda v: int(v)-1, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0] * m for _ in range(n)] for _ in range(2)]
visited[0][hx][hy] = 1
que = deque()
que.append((hx, hy, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que:
    x, y, cnt = que.popleft()
    if ex == x and ey == y:
        print(visited[cnt][x][y] - 1)
        exit()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] and not cnt and not visited[cnt+1][nx][ny]:
                visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                que.append((nx, ny, cnt+1))
            elif not arr[nx][ny] and not visited[cnt][nx][ny]:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                que.append((nx, ny, cnt))
print(-1)
