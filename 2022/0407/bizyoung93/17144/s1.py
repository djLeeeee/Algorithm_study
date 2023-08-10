import sys

def do(r, c):
    # 4방향 확산
    cnt = 0
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]

        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != -1:
            # 만약 사방향이 범위 안이고, 공기청정기가 아니라면 확산
            g2[nr][nc] += g[r][c] // 5
            cnt += 1
        # 확산된 미세먼지 부분의 양을 줄임
    g2[r][c] += g[r][c] - (g[r][c] // 5) * cnt






sys.stdin = open('input.txt')
# R, C, T초
R, C, T = map(int,  sys.stdin.readline().rstrip().split())
aircon_a = 0
aircon_b = 0
g = []
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
dr2 = (1, 0, -1, 0)
dc2 = (0, 1, 0, -1)
for i in range(R):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(C):
        if temp[j] == -1 and not aircon_a:
            aircon_a = (i, j)
            aircon_b = (i+1, j)
    g.append(temp)

for tc in range(T):
    g[aircon_a[0]][aircon_a[1]] = -1
    g[aircon_b[0]][aircon_b[1]] = -1
    g2 = [[0] * C for _ in range(R)]
    # 확산
    spread = []
    for r in range(R):
        for c in range(C):
            if g[r][c] and g[r][c] != -1:
                do(r, c)
    g = g2
    # g2[aircon_a[0]][aircon_a[1]] = -1
    # g2[aircon_b[0]][aircon_b[1]] = -1

    # 에어컨 a 순환 => 순환은 거꾸로 하자
    # print(g)
    a, b = aircon_a[0], aircon_a[1]
    w = 0
    while not(a == aircon_a[0] and b == aircon_a[1] and w == 3):
        na, nb = a + dr[w], b + dc[w]
        if not (0 <= na < aircon_a[0] + 1) or not(0 <= nb < C):
            w += 1
            continue
        g[a][b] = g[na][nb]
        a, b = na, nb

    # 에어컨 b 순환
    a, b = aircon_b[0], aircon_b[1]
    w = 0
    while not(a == aircon_b[0] and b == aircon_b[1] and w == 3):
        na, nb = a + dr2[w], b + dc2[w]
        if not (aircon_b[0] <= na < R) or not (0 <= nb < C):
            w += 1
            continue
        g[a][b] = g[na][nb]
        a, b = na, nb
    g[aircon_a[0]][aircon_a[1] + 1] = 0
    g[aircon_b[0]][aircon_b[1] + 1] = 0
    a = 0

g[aircon_a[0]][aircon_a[1]] = -1
g[aircon_b[0]][aircon_b[1]] = -1
ans = 0
for i in range(R):
    for j in range(C):
        if g[i][j]:
            ans += g[i][j]
ans += 2
print(ans)