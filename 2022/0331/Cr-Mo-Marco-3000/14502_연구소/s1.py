import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())

def do(wall):
    global ans
    if wall == 3:
        cnt_0 = num_0
        visited = [[0] * M for _ in range(N)]
        Q = deque(point)
        while Q:
            if cnt_0 < ans:
                return
            else:
                r, c = Q.popleft()
                for w in range(4):
                    nr = r + dr[w]
                    nc = c + dc[w]
                    if 0 <= nr < N and 0 <= nc < M and g[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = 2
                        cnt_0 -= 1
                        Q.append((nr, nc))
        if cnt_0 > ans:
            ans = cnt_0
    else:
        for i in range(N):
            for j in range(M):
                if g[i][j] == 1 or g[i][j] == 2:
                    for k in range(8):
                        ni = i + dr[k]
                        nj = j + dc[k]
                        if 0 <= ni < N and 0 <= nj < M:
                            if g[ni][nj] == 0:
                                g[ni][nj] = 1
                                do(wall + 1)
                                g[ni][nj] = 0



g = []
# 그래프에서 0의 총 개수
# 그래프에서 2의 좌표들
point = []
dr = (-1, 0, 1, 0, -1, 1, 1, -1)
dc = (0, 1, 0, -1, 1, 1, -1, -1)
ans = 0
num_0 = -3
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(temp)):
        if temp[j] == 0:
            num_0 += 1
        elif temp[j] == 2:
            point.append((i, j))
    g.append(temp)
do(0)
print(ans)

