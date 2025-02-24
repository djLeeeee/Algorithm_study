import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dh = [1, -1, 0, 0, 0, 0]

cnt = 0
total = 0
que = deque()

arr = []
for k in range(H):
    box = []
    for i in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        for j in range(M):
            if row[j] >= 0:
                total += 1
                if row[j] == 1:
                    cnt += 1
                    que.append((i, j, k))
    arr.append(box)

day = 0
while que:
    if cnt == total:
        print(day)
        exit()
    n = len(que)
    for _ in range(n):
        x, y, h = que.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nh = h + dh[d]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
                if arr[nh][nx][ny] == 0:
                    arr[nh][nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny, nh))
    day += 1

print(day if cnt == total else -1)
