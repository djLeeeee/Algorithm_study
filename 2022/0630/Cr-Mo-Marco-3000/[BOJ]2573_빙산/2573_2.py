import sys, collections

input = sys.stdin.readline

N, M = map(int, input().strip().split())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ice_list = collections.deque([])

melt_list = []
year = 0
g = [list(map(int, input().strip.split())) for _ in range(N)]   # 그래프
visited = [[0] * M for _ in range(N)]

# 얼음 리스트 생성
for i in range(N):
    for j in range(M):
        if g[i][j]:
            ice_list.append((i, j))
            break
    if ice_list:
        break

while True:
    year += 1
    cnt = 0
    r, c = ice_list.pop()
    Q = collections.deque([r, c])
    while Q:
        r, c = Q.popleft()
        if not visited[r][c]:
            visited[r][c] = 1
            cnt += 1
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if not visited[nr][nc] and g[nr][nc]:

