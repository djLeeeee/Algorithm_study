import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = 12, 6
arr = [list(input().rstrip()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
while True:
    visited = [[0] * m for _ in range(n)]
    boom = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != '.' and not visited[i][j]:
                visited[i][j] = 1
                que = deque([(i, j)])
                temp = arr[i][j]
                connected = [(i, j)]
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and arr[nx][ny] == temp:
                                visited[nx][ny] = 1
                                connected.append((nx, ny))
                                que.append((nx, ny))
                if len(connected) >= 4:
                    boom.append(connected)
    if boom:
        for case in boom:
            for x, y in case:
                arr[x][y] = '.'
        ans += 1
    else:
        break

    new_arr = [['.'] * m for _ in range(n)]
    for j in range(m):
        rest = []
        for i in range(n):
            if arr[i][j] != '.':
                rest.append(arr[i][j])
        for k in range(-1, -len(rest)-1, -1):
            new_arr[k][j] = rest[k]
    arr = new_arr

print(ans)




