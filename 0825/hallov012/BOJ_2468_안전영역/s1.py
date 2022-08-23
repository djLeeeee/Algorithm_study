import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = []
min_h, max_h = 100, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    row = list(map(int, input().split()))
    min_h = min(min_h, min(row))
    max_h = max(max_h, max(row))
    arr.append(row)

ans = 0
# 아무곳도 안잠기는 경우도 고려해야하므로 min_h - 1 부터
for h in range(min_h-1, max_h):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > h:
                visited[i][j] = 1
                que = deque([(i, j)])
                cnt += 1
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and arr[nx][ny] > h:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
    ans = max(ans, cnt)

print(ans)

