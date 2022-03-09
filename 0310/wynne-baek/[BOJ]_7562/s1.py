from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I:
                if chess[nx][ny] == 0:
                    chess[nx][ny] = chess[x][y] + 1
                    queue.append((nx, ny))
    return chess[end_x][end_y]

import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    I = int(input())
    chess = [[0]*I for _ in range(I)]
    x, y = map(int, input().split())
    end_x, end_y = map (int, input().split())
    if x == end_x and y == end_y:
        print(0)
    else:
        print(bfs(x, y))