# 백준 1937번 욕심쟁이 판다 - x

import sys
sys.stdin = open('input.txt')
from collections import deque

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def dfs(r, c):
    global ans
    move = 1
    stack = deque([(r, c, 1)])

    while stack:
        cr, cc, cnt = stack.pop()
        if move < cnt:
            move = cnt
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and forest[nr][nc] > forest[cr][cc]:
                if dist[nr][nc] and dist[nr][nc] + cnt > dist[cr][cc]:
                    dist[cr][cc] = dist[nr][nc] + cnt
                    if move < dist[cr][cc]:
                        move = dist[cr][cc]
                elif dist[nr][nc] == 0:
                    dist[cr][cc] = 1
                    stack.append((nr, nc, cnt + 1))
    dist[r][c] = move
    if ans < move:
        ans = move


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
ans = 0
for r in range(n):
    for c in range(n):
        dfs(r, c)
print(dist)
print(ans)