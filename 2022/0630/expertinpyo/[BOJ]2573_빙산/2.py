# 빙산 각 부분별 높이는 배열에 양의 정수로 저장
# 바다에 해당하면 0 저장
# 한 턴 마다 동서남북에 0ㅇ이 저장된 칸의 수만큼 줄어듬
# 각 칸의 높이는 0이 최솟값
# 동서남북으로 붙어있으면 연결되어 있는 것

# 얼음이 전부 다 녹을 때 까지 두덩이 이상으로 분리되지 않으면 0 출력
# 배열 첫, 마지막 행렬은 0임

N, M = map(int, input().split())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(map(int, input().split())) for _ in range(N)]

ice_cnt = 0
x = y = -1
for i in range(1, N-1):             # 얼음 있는 칸 개수 세기
    for j in range(1, M-1):
        if arr[i][j]:
            ice_cnt += 1
            if x == y == -1:        # 첫번째 발견한 칸이면 x y 갱신
                x, y = i, j
year = 0
while ice_cnt:              # 얼음이 있다면 반복문 진행
    keeping = False
    dfs_cnt = 1
    stack = [(x, y)]
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while stack:        # 얼음 한 덩이인지 dfs로 확인
        x, y = stack.pop()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 1 <= nx < N-1 and 0 <= ny < M-1 and arr[nx][ny] and not visited[nx][ny]:
                dfs_cnt += 1
                visited[nx][ny] = 1
                stack.append((nx, ny))
    if dfs_cnt == ice_cnt:      # 기존에 셌던 얼음 수와 dfs로 확인한 수가 같다면 진행
        keeping = True
        x = y = -1

    if keeping: # 아직 한 덩어리
        melt = [[0] * M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j]:
                    for d in di:
                        ni, nj = i + d[1], j + d[0]
                        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]: # melt : 얼음 녹일 것 count
                            if melt[i][j] < arr[i][j]:
                                melt[i][j] += 1
                            if melt[i][j] == arr[i][j]:
                                ice_cnt -=1
                                break

        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j]:
                    arr[i][j] -= melt[i][j]
                    if arr[i][j] and x == y == -1:
                        x, y = i, j
        year += 1

    else:   # 분리 됐거나 없거나
        break

if not ice_cnt:
    print(0)
else:
    print(year)