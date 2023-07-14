import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
ans = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(m):
    for j in range(n):
        if not arr[i][j]:
            cnt = 1
            que = deque([(i, j)])
            arr[i][j] = 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and not arr[nx][ny]:
                        arr[nx][ny] = 1
                        cnt += 1
                        que.append((nx, ny))
            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)
