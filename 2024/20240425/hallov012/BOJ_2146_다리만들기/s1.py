import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
island = [[0] * n for _ in range(n)]
side = [[]]
idx = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if arr[i][j] and not island[i][j]:
            island[i][j] = idx
            que = deque([(i, j)])
            side.append([])
            while que:
                x, y = que.popleft()
                flag = False
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny]:
                            if not island[nx][ny]:
                                que.append((nx, ny))
                                island[nx][ny] = idx
                        else:
                            flag = True
                if flag:
                    side[idx].append((x, y))
            idx += 1

ans = n * n
for i in range(1, idx):
    visited = [[0] * n for _ in range(n)]
    que = deque()
    for x, y in side[i]:
        visited[x][y] = 1
        que.append((x, y))
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if island[nx][ny] and island[nx][ny] != i:
                    ans = min(ans, visited[x][y] - 1)
                if not visited[nx][ny] and not island[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))

print(ans)


