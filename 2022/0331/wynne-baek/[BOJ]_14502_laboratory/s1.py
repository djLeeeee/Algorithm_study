import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    global answer
    Q = deque()
    new_lab = [item[:] for item in arr]
    cnt = 0
    for idx_x in range(N):
        for idx_y in range(M):
            if new_lab[idx_x][idx_y] == 2:
                Q.append((idx_x, idx_y))
            elif new_lab[idx_x][idx_y] == 0:
                cnt += 1

    while Q:
        if cnt < answer:
            return
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2
                Q.append((nx, ny))
                cnt -= 1
    answer = max(answer, cnt)

def wall(wall_count):
    if wall_count == 3:
        spread()
        return
    else:
        for i in range(N):
            for j in range(M):
                if not arr[i][j]:
                    arr[i][j] = 1
                    wall(wall_count + 1)
                    arr[i][j] = 0

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(N)]
answer = 0
wall(0)
print(answer)
