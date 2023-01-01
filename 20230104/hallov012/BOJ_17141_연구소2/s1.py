import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

def bfs(que):
    check = [[0] * n for _ in range(n)]
    for x, y in que:
        check[x][y] = 1
    time = -1
    cnt = m
    while que:
        k = len(que)
        for _ in range(k):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not check[nx][ny] and arr[nx][ny] == 0:
                        check[nx][ny] = 1
                        cnt += 1
                        que.append((nx, ny))
        time += 1
    return time, cnt

def select(cnt, idx):
    global ans
    if cnt == m:
        que = deque()
        for i in range(len(virus)):
            if visited[i]:
                que.append((virus[i]))
        time, cnt = bfs(que)
        if cnt == empty:
            if ans > time:
                ans = time
        return
    for i in range(idx+1, len(virus)):
        if not visited[i]:
            visited[i] = 1
            select(cnt+1, i)
            visited[i] = 0

n, m = map(int, input().split())
arr = []
virus = []
wall = 0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i, j))
            arr[i][j] = 0
        elif arr[i][j] == 1:
            wall += 1

visited = [0] * len(virus)
empty = n*n - wall
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = sys.maxsize
select(0, -1)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)