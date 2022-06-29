import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
data = [input() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[sys.maxsize] * m for _ in range(n)]
visited[0][0] = 0
que = deque([(0, 0, 0)])
while que:
    x, y, cnt = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == '1' and visited[nx][ny] > cnt + 1:
                visited[nx][ny] = cnt + 1
                que.append((nx, ny, cnt + 1))
            elif data[nx][ny] == '0' and visited[nx][ny] > cnt:
                visited[nx][ny] = cnt
                que.append((nx, ny, cnt))
print(visited[n-1][m-1])

