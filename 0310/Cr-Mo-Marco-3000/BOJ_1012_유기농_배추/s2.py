import sys


sys.setrecursionlimit(100000000)


# 재귀로 풀자
def marco2(r, c):
    if g[r][c] == 1:
        g[r][c] += 1
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < M:
            if g[nr][nc] == 1:
                marco2(nr, nc)


T = int(input())

for tc in range(T):
    # M: 가로길이:C, N: 세로길이:r, K: 배추개수
    M, N, K = map(int, input().split())

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt = 0

    g = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        g[b][a] = 1

    # 제발 시간초과 뜨지마라...
    for r in range(N):
        for c in range(M):
            if g[r][c] == 1:
                marco2(r, c)
                cnt += 1
    print(cnt)
