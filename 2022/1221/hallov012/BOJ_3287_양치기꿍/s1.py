import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
wolf, lamb = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and not visited[i][j]:
            visited[i][j] = 1
            que = deque([(i, j)])
            w, l = 0, 0
            if arr[i][j] == 'v':
                w += 1
            elif arr[i][j] == 'k':
                l += 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        if not visited[nx][ny] and arr[nx][ny] != "#":
                            visited[nx][ny] = 1
                            que.append((nx, ny))
                            if arr[nx][ny] == 'v':
                                w += 1
                            elif arr[nx][ny] == 'k':
                                l += 1
            if w >= l:
                wolf += w
            else:
                lamb += l

print(lamb, wolf)

