from sys import stdin
import heapq

input = stdin.readline

tc = 0
INF = float('inf')
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    n = int(input())
    if n == 0:
        break
    tc += 1
    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = board[0][0]
    point = [(dist[0][0], 0, 0)]
    while point:
        c, x, y = heapq.heappop(point)
        if x == y == n - 1:
            break
        if dist[x][y] < c:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and c + board[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = c + board[nx][ny]
                heapq.heappush(point, (dist[nx][ny], nx, ny))
    print(f"Problem {tc}: {c}")
