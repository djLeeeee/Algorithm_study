import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

n = 3
arr = [list(map(int, input().split())) for _ in range(n)]
target = '123456780'
now = ''
x, y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        now += str(arr[i][j])
        if arr[i][j] == 0:
            x, y = i, j

que = deque()
visited = defaultdict(int)
que.append((now, x*n + y, x, y))
visited[now] += 1

while que:
    now, idx, x, y = que.popleft()
    if now == target:
        print(visited[now]-1)
        exit()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            n_idx = nx * n + ny
            if idx > n_idx:
                idx_1, idx_2, value_1, value_2 = n_idx, idx, now[idx], now[n_idx]
            else:
                idx_1, idx_2, value_1, value_2 = idx, n_idx, now[n_idx], now[idx]
            next = now[:idx_1] + value_1 + now[idx_1+1:idx_2] + value_2 + now[idx_2+1:]
            if not visited[next]:
                visited[next] = visited[now] + 1
                que.append((next, n_idx, nx, ny))
print(-1)


