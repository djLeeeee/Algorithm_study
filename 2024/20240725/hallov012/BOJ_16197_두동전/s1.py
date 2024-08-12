import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
coin = []
for i in range(n):
    row = input().strip()
    for j in range(m):
        if row[j] == 'o':
            coin.append((i, j))
    arr.append(row)

visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
(a, b), (c, d) = coin
visited[a][b][c][d] = 1

que = deque()
que.append((a, b, c, d))

t = 0
while que and t < 10:
    t += 1
    k = len(que)
    for _ in range(k):
        x1, y1, x2, y2 = que.popleft()
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            flag1, flag2 = 0, 0
            if 0 <= nx1 < n and 0 <= ny1 < m:
                flag1 = 1
                if arr[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
            if 0 <= nx2 < n and 0 <= ny2 < m:
                flag2 = 1
                if arr[nx2][ny2] == '#':
                    nx2, ny2 = x2,y2

            if flag1 + flag2 == 1:
                print(t)
                exit()

            if flag1 + flag2 == 2 and not visited[nx1][ny1][nx2][ny2]:
                visited[nx1][ny1][nx2][ny2] = 1
                que.append((nx1, ny1, nx2, ny2))

print(-1)

