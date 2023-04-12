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
            data[c] = -1
            queue.appendleft((r, c, -1))        # 물이 찰 예정인 칸으로 이동할 수 없으므로 물 먼저 이동
        elif data[c] == 'S':
            data[c] = 1
            queue.append((r, c, 1))
    forest.append(data)
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
while queue:
    cr, cc, cnt = queue.popleft()
    isWater = True
    if cnt > 0:
        isWater = False
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if forest[nr][nc] == '.':
                if isWater:
                    forest[nr][nc] = cnt - 1
                    queue.append((nr, nc, cnt - 1))
                else:
                    forest[nr][nc] = cnt + 1
                    queue.append((nr, nc, cnt + 1))
            elif forest[nr][nc] == 'D' and not isWater:
                print(cnt)
                sys.exit()
print("KAKTUS")