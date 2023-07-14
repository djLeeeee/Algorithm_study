import sys
from collections import deque
sys.stdin = open('input.txt')

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[987654321] * M for _ in range(N)]

dist[0][0] = 0
queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] == 987654321:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
print(dist[N-1][M-1])



