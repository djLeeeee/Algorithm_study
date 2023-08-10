# 이거 답이 아니다
# 그림 때문에 더 헷갈리는 문제이다.
# 그림에서 0 => L1 => L2로 진행된다는 말이 아니라 0 => L1 또는 0 => L2로 진행됐을 때로 이해하자

import sys
input = sys.stdin.readline

N, Q = map(int, input().strip().split())

M = 2 ** N


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
    # 움직임은 이만큼 => 1이 1일때는 한칸, 2일때는 2칸, 3일때는 4칸....
    move = 2 ** (L-1)
    # 명령 방향 => 우 하 좌 상 *
    dr = (0, move, 0, -move)
    dc = (move, 0, -move, 0)
    
    # 회전
    # 전체 그래프를 돌면서 이동시켜주는데,
    # 움직임을 나누기 위해 격자의 시작점을 찾아보자
    # 격자의 시작점부터 끝점까지 나눈 후, 그 구역의 절반 이하와 절반 이상에 따라서 이동시키는 방향이 달라진다.
    if L != 0:
        for i in range(M):
            for j in range(M):
                # 총 4 가지 경우가 있다.
                ni = i % (2 ** L)
                nj = j % (2 ** L)
                # 기준이 되는 수 crit
                crit = 2 ** (L - 1)
                # 좌상 => 우로 이동
                if ni < crit and nj < crit:
                    g2[i + dr[0]][j + dc[0]] = g[i][j]
                # 우상 => 하로 이동
                elif ni < crit and nj >= crit:
                    g2[i + dr[1]][j + dc[1]] = g[i][j]
                # 우하 => 좌로 이동
                elif ni >= crit and nj >= crit:
                    g2[i + dr[2]][j + dc[2]] = g[i][j]
                # 좌하 => 상으로 이동
                elif ni >= crit and nj < crit:
                    g2[i + dr[3]][j + dc[3]] = g[i][j]
    else:
        g2 = g

    # 녹일 얼음 칸 체크
    # 주의해야 할 점(!!!)은, 좌표를 통해 확인하면서 바로 녹여 줄 경우에는,
    # 앞에서 녹인 얼음이 0이 되어 이후에 걸린 얼음이 녹지 않는 경우가 생긴다
    # 따라서, 일단 체크해준 후 한 번에 녹여 주어야 한다.
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

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

print(ice_num)
print(g)
