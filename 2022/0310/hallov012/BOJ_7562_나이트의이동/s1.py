import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    cnt_g = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    que = [[sx, sy]]
    visited[sx][sy] = 1
    while que:
        x, y = que.pop(0)
        if x == ex and y == ey:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny])
    print(visited[ex][ey]-1)