import sys
from collections import deque
sys.stdin = open('input.txt')

def melt():
    melt_lst = []
    for x, y in ice:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not data[nx][ny]:
                cnt += 1
        if cnt:
            melt_lst.append((x, y, cnt))
    for x, y, cnt in melt_lst:
        data[x][y] -= cnt
        if data[x][y] < 0:
            data[x][y] = 0

def bfs():
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            que.append((nx, ny))
    return cnt

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
ice = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j]:
            ice.append((i, j))
    data.append(line)
ans = 0
while True:
    ans += 1
    melt()
    cnt = bfs()
    if cnt == 0:
        ans = 0
        break
    elif cnt > 1:
        break
print(ans)
