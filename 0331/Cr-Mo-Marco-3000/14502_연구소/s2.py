import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt')

dr = (-1, 0, 1, 0, -1, 1, 1, -1)
dc = (0, 1, 0, -1, 1, 1, -1, -1)

N, M = map(int, sys.stdin.readline().rstrip().split())

wall_list = []
com_list = []
virus_list = []
g = []
num_0 = -3
ans = 0
# 그래프 생성
# 0 자리에 벽을 세울 수 있으니까 wall_list에 추가
# 바이러스가 있는 좌표를 virus_list에 추가
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(M):
        if temp[j] == 0:
            num_0 += 1
            wall_list.append((i, j))
        elif temp[j] == 2:
            virus_list.append((i, j))
    g.append(temp)

# 빈 칸에 벽을 세울 수 있는 모든 경우를 생성
com_list = tuple(combinations(wall_list, 3))
for i in com_list:
    # 한 경우를 뽑아서 그 벽을 세운 다음
    for j in i:
        g[j[0]][j[1]] = 1
    # 난 왜 이렇게 헛된 시간을....
    # can = 0
    # for k in i:
    #     r = k[0]
    #     c = k[1]
    #     for w in range(8):
    #         nr = r + dr[w]
    #         nc = c + dc[w]
    #         if 0 <= nr < N and 0 <= nc < M and g[nr][nc]:
    #             can += 1
    #             break
    # if can != 3:
    #     for j in i:
    #         g[j[0]][j[1]] = 0
    #     continue

    # 돌려준다.
    cnt = num_0
    visited = [[0] * M for _ in range(N)]
    Q = deque(virus_list)
    while Q:
        if cnt < ans:
            break
        r, c = Q.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            # g를 새로 선언하기는 함수를 쓰지 않으므로, visited만 새로 만들어 준다.
            if 0 <= nr < N and 0 <= nc < M and not g[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                cnt -= 1
    if cnt > ans:
        ans = cnt
    for j in i:
        g[j[0]][j[1]] = 0
print(ans)
