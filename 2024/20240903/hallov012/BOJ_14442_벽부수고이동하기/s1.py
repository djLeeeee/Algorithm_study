import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = 1
que = deque([(0, 0, 0)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que:
    x, y, cnt = que.popleft()
    if x == n-1 and y == m-1:
        print(visited[cnt][x][y])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[nx][ny]:
                if not visited[cnt][nx][ny]:
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    que.append((nx, ny, cnt))
            elif cnt < k:
                if not visited[cnt+1][nx][ny]:
                    visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                    que.append((nx, ny, cnt+1))

print(-1)