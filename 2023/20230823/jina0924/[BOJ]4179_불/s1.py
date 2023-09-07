# 백준 4179번 불!

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def fire(r, c):
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and maze[nr][nc] != 'F':
            maze[nr][nc] = 'F'
            queue.append((nr, nc, -1))


def move(r, c, cnt):
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if maze[nr][nc] == '.':
                maze[nr][nc] = 'J'
                queue.append((nr, nc, cnt + 1))
        else:
            print(cnt)
            sys.exit()


def bfs():
    while queue:
        cr, cc, cnt = queue.popleft()
        if cnt < 0:
            fire(cr, cc)
        else:
            move(cr, cc, cnt)


R, C = map(int, input().split())
maze = []

queue = deque([])
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for r in range(R):
    row = list(input().rstrip())
    for c in range(C):
        if row[c] == 'J':
            queue.append((r, c, 1))
        elif row[c] == 'F':
            queue.appendleft((r, c, -1))
    maze.append(row)

ans = 0
bfs()
print('IMPOSSIBLE')