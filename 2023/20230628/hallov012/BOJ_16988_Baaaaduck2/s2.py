import sys
from collections import deque
sys.stdin = open('input.txt')

def find_position(cnt, temp, idx):
    if cnt == 2:
        cases.append(temp.copy())
        return
    for i in range(idx+1, len(empty)):
        temp.append(empty[i])
        find_position(cnt+1, temp, i)
        temp.pop()

def bfs(a, b):
    if visited[a][b]:
        return 0
    visited[a][b] = 1
    que = deque([(a, b)])
    cnt = 1
    flag = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if not arr[nx][ny]:
                    flag = False
                elif arr[nx][ny] == 2:
                    cnt += 1
                    visited[nx][ny] = 1
                    que.append((nx, ny))
    return cnt if flag else 0

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
empty = []
ai = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(m):
        if not arr[i][j]:
            empty.append((i, j))
        elif arr[i][j] == 2:
            ai.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

cases = []
find_position(0, [], -1)

for case in cases:
    visited = [[0] * m for _ in range(n)]
    for x, y in case:
        arr[x][y] = 1

    ai_cnt = 0
    for a, b in ai:
        ai_cnt += bfs(a, b)

    for x, y in case:
        arr[x][y] = 0

    ans = max(ans, ai_cnt)

print(ans)
