import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

def mining(d):
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] * m for _ in range(n)]
    que = deque()
    for i in range(n):
        for j in range(m):
            if i != 0 and 0 < j < m-1:
                continue
            if mineral[i][j] <= d:
                visited[i][j] = 1
                que.append((i, j))
                cnt += 1
                if cnt == k:
                    return True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mineral[nx][ny] <= d and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    cnt += 1
                    if cnt == k:
                        return True
    return cnt >= k

n, m, k = map(int, input().split())
mineral = [list(map(int, input().split())) for _ in range(n)]

start, end = 0, max(max(mineral[i]) for i in range(n))
while start < end:
    mid = (start + end) // 2
    if mining(mid):
        end = mid
    else:
        start = mid + 1
print(end)