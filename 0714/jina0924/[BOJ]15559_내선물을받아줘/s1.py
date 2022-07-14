# 백준 15559번 내 선물을 받아줘

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline
from collections import deque


def solution(r, c):
    global group
    queue = deque([(r, c)])
    visited[r][c] = group

    while queue:
        cr, cc = queue.popleft()
        d = 0
        if data[cr][cc] == 'S':
            d = 1
        elif data[cr][cc] == 'W':
            d = 2
        elif data[cr][cc] == 'E':
            d = 3
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = group
                queue.append((nr, nc))
            elif visited[nr][nc] < group:
                return 0
    return 1


N, M = map(int, input().split())
data = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
group = ans = 0
for cr in range(N):
    for cc in range(M):
        if not visited[cr][cc]:
            group += 1
            ans += solution(cr, cc)
print(ans)