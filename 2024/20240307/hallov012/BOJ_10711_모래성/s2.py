import sys
from collections import deque
sys.stdin = open('input.txt')

"""
8방향 중, 모래성이 없는 부분의 수가 자신의 수보다 많거나 같으면 무너질 수 있음
모래성이 무너진다 = 새로 빈 곳이 생긴다
"""

input = sys.stdin.readline

h, w = map(int, input().split())
arr = [[0] * w for _ in range(h)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

que = deque()

for i in range(h):
    data = input().rstrip()
    for j in range(w):
        if data[j] != '.':
            arr[i][j] = int(data[j])
        else:
            que.append((i, j))

ans = -1
while que:
    l = len(que)
    for _ in range(l):
        x, y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] > 0:
                    arr[nx][ny] -= 1
                    if arr[nx][ny] == 0:
                        que.append((nx, ny))
    ans += 1

print(ans)

