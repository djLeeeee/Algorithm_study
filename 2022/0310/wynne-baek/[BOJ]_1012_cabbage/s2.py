import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))
    return

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    field = [[0]*M for ___ in range(N)]
    cnt = 0
    for __ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    for idx in range(N):
        for idx2 in range(M):
            if field[idx][idx2] == 1:
                bfs(idx, idx2)
                field[idx][idx2] = 0
                cnt += 1
    print(cnt)