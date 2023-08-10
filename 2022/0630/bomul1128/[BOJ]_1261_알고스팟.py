from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

m, n = map(int, input().split())
board = [input().strip() for _ in range(n)]
INF = float('inf')
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
heap = [(0, 0, 0)]
while heap:
    cost, x, y = heappop(heap)
    if x == n - 1 and y == m - 1:
        break
    if dist[x][y] < cost:
        continue
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == '1' and dist[nx][ny] > cost + 1:
                dist[nx][ny] = cost + 1
                heappush(heap, (cost + 1, nx, ny))
            elif board[nx][ny] == '0' and dist[nx][ny] > cost:
                dist[nx][ny] = cost
                heappush(heap, (cost, nx, ny))
print(cost)
