import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx_8 = [-1, -2, -2, -1, 1, 2, 2, 1]
dy_8 = [-2, -1, 1, 2, -2, -1, 1, 2]
dx_4 = [1, -1, 0, 0]
dy_4 = [0, 0, 1, -1]

visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = 1
que = deque([(0, 0, 0, 0)])

while que:
    x, y, move, h_move = que.popleft()
    if x == n-1 and y == m-1:
        print(move)
        exit()
    if h_move < k:
        for i in range(8):
            nx = x + dx_8[i]
            ny = y + dy_8[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny] and not visited[h_move+1][nx][ny]:
                    visited[h_move+1][nx][ny] = 1
                    que.append((nx, ny, move+1, h_move+1))
    for j in range(4):
        nx = x + dx_4[j]
        ny = y + dy_4[j]
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[nx][ny] and not visited[h_move][nx][ny]:
                visited[h_move][nx][ny] = 1
                que.append((nx, ny, move+1, h_move))

print(-1)
