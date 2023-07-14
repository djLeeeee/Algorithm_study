# 설명을 이상하게 써놨네
# 예시그림때문에 더 헷갈리는건 처음이다

import sys

input = sys.stdin.readline

N, Q = map(int, input().strip().split())

M = 2 ** N

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def do(r, c):
    global ans
    visited[r][c] = 1
    stack = [(r, c)]
    cnt = 1
    while stack:
        r, c = stack.pop()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < M and 0 <= nc < M and g[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                stack.append((nr, nc))
    if cnt > ans:
        ans = cnt


# 그래프를 받아 준다. => 받아 주면서 얼음의 총 량을 저장해준다.
ice_num = 0
g = []

for _ in range(M):
    temp = list(map(int, input().strip().split()))
    for k in temp:
        ice_num += k
    g.append(temp)

# 명령 리스트
orders = tuple(map(int, input().strip().split()))

# 얼음을 녹일 리스트
ice = []

# 명령 횟수만큼 돌려준다.
for tc in range(Q):
    # 돌린 배열을 등록할 그래프
    g2 = [[0] * M for _ in range(M)]
    # 명령
    L = orders[tc]

    # 회전
    # 전체 그래프를 돌면서 이동시켜주는데,
    # 움직임을 나누기 위해 격자의 시작점을 찾아보자
    # 격자의 시작점부터 끝점까지 나눈 후, 그 구역의 절반 이하와 절반 이상에 따라서 이동시키는 방향이 달라진다.
    if L != 0:
        # 큰 격자 i j
        for i in range(0, M, 2 ** L):
            for j in range(0, M, 2 ** L):
                # 작은 격자 r, c
                # g 좌측 상단부터 하측으로 : 좌 우 => g2 우측 상단부터 좌측으로 상 하
                for r in range(2 ** L):
                    for c in range(2 ** L):
                        nc = (2 ** L) - 1 - r
                        nr = c
                        g2[i + nr][j + nc] = g[i + r][j + c]
    else:
        g2 = g

    # 녹일 얼음 칸 체크
    # 주의해야 할 점(!!!)은, 좌표를 통해 확인하면서 바로 녹여 줄 경우에는,
    # 앞에서 녹인 얼음이 0이 되어 이후에 걸린 얼음이 녹지 않는 경우가 생긴다
    # 따라서, 일단 체크해준 후 한 번에 녹여 주어야 한다.

    for r in range(M):
        for c in range(M):
            cnt = 0
            if g2[r][c] == 0:
                continue
            for w in range(4):
                nr = r + dr[w]
                nc = c + dc[w]
                if 0 <= nr < M and 0 <= nc < M and g2[nr][nc]:
                    cnt += 1
            if cnt < 3:
                ice.append((r, c))

    # 얼음을 녹여준다.
    while ice:
        r, c = ice.pop()
        g2[r][c] -= 1
        ice_num -= 1

    # 그래프를 체인지해 준 후 반복한다.
    g = g2

# dfs
ans = 0
visited = [[0] * M for _ in range(M)]

for m in range(M):
    for n in range(M):
        if not visited[m][n] and g[m][n]:
            do(m, n)

print(ice_num)
print(ans)

