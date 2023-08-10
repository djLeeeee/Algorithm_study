import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

green_tomato = 0
red_tomato = []

g = []
for i in range(M):
    temp = list(map(int, input().strip().split()))
    for j in range(N):
        if temp[j] == 1:
            red_tomato.append((i, j, 0))    # 익은 토마토 좌표를 리스트로 받아줌
        elif temp[j] == 0:
            green_tomato += 1               # 안 익은 토마토의 수 green_tomato
    g.append(temp)                          # 이거 안 해줘서 큰일날 뻔 했다.

max_day = 0                                 # 익는 최대 날짜를 0으로 잡아줌

Q = deque(red_tomato)                       # bfs 쓸 거면 덱 써주어야지
    
dr = (-1, 0, 1, 0)                          # 방향 델타 잡아주고
dc = (0, 1, 0, -1)

while Q:
    r, c, day = Q.popleft()                 # while문 돌려준다.
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < M and 0 <= nc < N:     # 범위 내에 있고
            if g[nr][nc] == 0:              # 안 익은 토마토라면
                Q.append((nr, nc, day + 1)) # 큐에 넣고
                g[nr][nc] = 1               # 익히고
                green_tomato -= 1           # 안 익은 토마토 숫자에서 빼주고
                if day + 1 > max_day:       # 익는 데 걸리는 최대 일수 갱신
                    max_day = day + 1

if green_tomato >= 1:                       # 안 익은 토마토 존재시
    print(-1)                               # -1 프린트
else:
    print(max_day)                          # 다 익었으면 최대 일수 출력

# 평범한 bfs문제이다.
