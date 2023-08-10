from collections import deque

def bfs(x, y):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))

    return maze[N-1][M-1]





import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    maze = [list(map(int, input())) for __ in range(N)]
    #print(maze)
    print(bfs(0, 0))