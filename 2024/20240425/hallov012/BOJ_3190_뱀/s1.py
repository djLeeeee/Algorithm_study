import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

snake = deque()
snake.append((0, 0))
S = -1
arr[0][0] = S

l = int(input())
rotate = {}
for _ in range(l):
    x, c = input().split()
    rotate[int(x)] = 1 if c == 'D' else -1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

t = 1
while True:
    x, y = snake[0]
    # 뱀 꼬리 위치
    tx, ty = snake.pop()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != S:
        snake.appendleft((nx, ny))
        if arr[nx][ny] == 1:
            snake.append((tx, ty))
        else:
            arr[tx][ty] = 0
        arr[nx][ny] = S
    else:
        break

    if t in rotate.keys():
        dir += rotate[t]
        dir %= 4

    t += 1

print(t)
