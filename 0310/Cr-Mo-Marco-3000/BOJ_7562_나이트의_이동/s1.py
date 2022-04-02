import sys

sys.stdin = open("input.txt")


def marco(r, c):
    Q = [[r, c]]
    while Q:
        v = Q.pop(0)
        r, c = v[0], v[1]
        if r == tr and c == tc:
            return g[tr][tc]
        for w in range(8):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < I and 0 <= nc < I:
                if g[nr][nc] == 0:
                    Q.append([nr, nc])
                    # 그 visited를 처리하는 게 관건인 것 같다.
                    # 최단경로를 찾을 때니까, 단순히 길이 없냐 있냐와는 달리, 최단거리를 누적시켜가며 진행해야 한다.
                    g[nr][nc] = g[r][c] + 1



T = int(input())
# 착한말 고운말
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]
for safdf in range(T):
    # 체스판의 길이 I
    I = int(input())
    g = [[0 for _ in range(I)] for _ in range(I)]
    # r, c : 현재 있는 칸
    sr, sc = map(int, input().split())
    # tr, tc: 목표 칸
    tr, tc = map(int, input().split())

    print(marco(sr, sc))
