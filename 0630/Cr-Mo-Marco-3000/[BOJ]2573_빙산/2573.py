import sys, collections

input = sys.stdin.readline

N, M = map(int, input().strip().split())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ice_list = []                                   # 얼음 좌표와 얼음의 양 리스트                      
g = []                                          # 그래프
for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(M):
        if temp[j]:
            ice_list.append((i, j, temp[j]))
    g.append(temp)

# 여기부터 반복
year = 0
while True:
    neo_ice_list = []
    # 1. 얼음 줄어들게 하기
    for r, c, ice in ice_list:
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if not g[nr][nc]:                                 # 상하좌우에 패딩이 있으므로 범위 제한이 필요없다.
                ice -= 1
        if ice <= 0:
            neo_ice_list.append((r, c, 0))
        else:
            neo_ice_list.append((r, c, ice))

    # 2. 줄어든 얼음 그래프에 적용
    ice_list = []
    while neo_ice_list:
        r, c, ice = neo_ice_list.pop()
        if not ice:
            g[r][c] = 0
        else:
            g[r][c] = ice
            ice_list.append((r, c, ice))

    if not ice_list:                            # 마지막까지 한 덩어리인 경우를 안 해줘서 틀렸었다.
        print(0)                                # 문제를 잘 읽고, 엣지 케이스 주의하자
        break

    # 3. bfs로 카운트 센 후 비교하기
    year += 1
    iceberg = len(ice_list)
    visited = [[0] * M for _ in range(N)]
    r, c = ice_list[0][0], ice_list[0][1]
    Q = collections.deque([(r, c)])

    cnt = 1
    visited[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if not visited[nr][nc] and g[nr][nc]:
                visited[nr][nc] = 1
                cnt += 1
                Q.append((nr, nc))

    if iceberg != cnt:
        print(year)
        break
