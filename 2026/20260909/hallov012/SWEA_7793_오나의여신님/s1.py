import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = []
    devil = deque()
    que = deque()
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        row = list(input().strip())
        arr.append(row)
        for j in range(m):
            if row[j] == '*':
                devil.append((i, j))
            elif row[j] == 'S':
                que.append((i, j, 0))
                visited[i][j] = 1
    ans = 0
    while que:
        d_len = len(devil)
        for _ in range(d_len):
            x, y = devil.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if not arr[nx][ny] in ('X', 'D', '*'):
                        arr[nx][ny] = '*'
                        devil.append((nx, ny))
        q_len = len(que)
        for _ in range(q_len):
            x, y, t = que.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 'D':
                        ans = t+1
                        break
                    elif arr[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        que.append((nx, ny, t+1))
            if ans:
                break
        if ans:
            break
    print(f"#{tc} {ans if ans else 'GAME OVER'}")