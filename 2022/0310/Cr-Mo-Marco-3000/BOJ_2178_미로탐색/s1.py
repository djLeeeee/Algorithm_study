import sys

sys.stdin = open("input.txt")


def marco(r, c):
    Q = [[r, c]]
    visited[r][c] = 1
    while Q:
        v = Q.pop(0)
        r, c = v[0], v[1]
        if r == N - 1 and c == M - 1:
            return visited[r][c]
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and g[nr][nc] == 1:
                    Q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1


# 아 기억안나
# N: 행, M: 열
N, M = map(int, input().split())

g = [list(map(int, input())) for _ in range(N)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[0] * M for _ in range(N)]
print(marco(0, 0))
