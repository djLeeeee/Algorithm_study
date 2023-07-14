import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while cheese:
        x, y, cnt = cheese.popleft()
        empty_cnt = 0
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                empty_cnt += 1
        if empty_cnt < 2:
            cheese.append((x, y, cnt + 1))
    return cnt




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheese = deque()
for i in range(N):
    for j in range(M):
        pass


answer = bfs()
print(answer)
