import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
visited = [[-1] * m for _ in range(n)]
que = deque()
for i in range(n):
    row = list(map(str, input().rstrip()))
    arr.append(row)
    for j in range(m):
        if row[j] == '0':
            x, y = i, j
            arr[i][j] = '.'
            visited[i][j] = -1
            que.append((i, j, 0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
key = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}
door = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}

while que:
    x, y, cnt, bit = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#':
            if visited[nx][ny] != -1 and visited[nx][ny] | bit == visited[nx][ny]:
                continue
            visited[nx][ny] = bit
            if not visited[nx][ny]:
                visited[nx][ny] = 0
            if arr[nx][ny] == '.':
                que.append((nx, ny, cnt+1, bit))
            elif arr[nx][ny] == '1':
                print(cnt+1)
                exit()
            else:
                k = key.get(arr[nx][ny])
                if k != None:
                    que.append((nx, ny, cnt+1, bit|k))
                else:
                    d = door.get(arr[nx][ny])
                    if d | bit == bit:
                        que.append((nx, ny, cnt+1, bit))
print(-1)
