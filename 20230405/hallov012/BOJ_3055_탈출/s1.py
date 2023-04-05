import sys
from collections import deque
sys.stdin = open('input.txt')

def water_move():
    new_water = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                arr[nx][ny] = '*'
                new_water.append((nx, ny))
    return new_water

def move():
    new_que = deque()
    while que:
        x, y = que.popleft()
        if arr[x][y] == 'D':
            print(visited[x][y] - 1)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == '.' or arr[nx][ny] == 'D':
                    visited[nx][ny] = visited[x][y] + 1
                    new_que.append((nx, ny))
    if not new_que:
        print("KAKTUS")
        exit()
    return new_que

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
water = deque()
que = deque()
visited = [[0] * c for _ in range(r)]
sx, sy = 0, 0
ex, ey = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append((i, j))
        elif arr[i][j] == 'S':
            sx, sy = i, j
            arr[i][j] = '*'
            visited[i][j] = 1
        elif arr[i][j] == 'D':
            ex, ey = i, j
que.append((sx, sy))

while True:
    water = water_move()
    que = move()
