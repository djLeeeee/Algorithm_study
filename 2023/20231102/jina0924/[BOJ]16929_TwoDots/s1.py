# 백준 16929번 Two Dots

import sys
sys.stdin = open('input.txt')


def dfs(r, c, cnt):
    global color, sr, sc

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == color:
            if cnt >= 4 and nr == sr and nc == sc:
                print('Yes')
                sys.exit()
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = 0


n, m = map(int, input().split())
board = list(list(input()) for _ in range(n))
visited = [[0] * m for _ in range(n)]
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
color = ''
sr, sc = 0, 0
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            color = board[r][c]
            sr, sc = r, c
            visited[r][c] = 1
            dfs(r, c, 1)
print('No')