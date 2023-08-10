# 백준 1937번 욕심쟁이 판다

import sys
sys.stdin = open('input.txt')
from collections import deque

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def dfs(r, c):
    global ans, sr, sc
    visited = [[0] * n for _ in range(n)]
    stack = deque([(r, c, 0)])

    while stack:
        cr, cc, cnt = stack.popleft()
        visited[cr][cc] = 1
        cnt += 1
        if ans < cnt:
            ans = cnt
            sr, sc = r, c
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] > forest[cr][cc]:
                if nr == sr and nc == sc:
                    ans += cnt
                    break
                stack.append((nr, nc, cnt))


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
ans = 0
sr, sc = 0, 0
for r in range(n):
    for c in range(n):
        dfs(r, c)
print(ans)