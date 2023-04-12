# 백준 3055번 탈출

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
forest = []
queue = deque([])
for r in range(R):
    data = list(input().rstrip())
    for c in range(C):
        if data[c] == '*':
            queue.appendleft((r, c))
        elif data[c] == 'S':
            data[c] = 1
            queue.append((r, c))
    forest.append(data)
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
while queue:
    cr, cc = queue.popleft()
    isWater = True
    if type(forest[cr][cc]) == int:
        isWater = False
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if forest[nr][nc] == '.':
                if isWater:
                    forest[nr][nc] = '*'
                    queue.append((nr, nc))
                else:
                    cnt = forest[cr][cc] + 1
                    forest[nr][nc] = cnt
                    queue.append((nr, nc))
            elif forest[nr][nc] == 'D' and not isWater:
                print(forest[cr][cc])
                sys.exit()
print("KAKTUS")