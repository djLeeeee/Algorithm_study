import sys
from collections import deque
sys.stdin = open('input.txt')

"""1) 얼음이 있는지
    2) 얼음이 분리되어 있는지
    만약 얼음이 있고 분리되지 않았으면 킵고잉
    얼음이 있는데 분리되었으면 멈추고 카운트 리턴
    얼음이 없으면 0이 답!"""

def melt():
    temp = [[0] * M for _ in range(N)]
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if sea[x][y]:
                cnt = 0
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if not sea[nx][ny]:
                        cnt += 1
                if sea[x][y] - cnt <= 0:
                    temp[x][y] = 0
                else:
                    temp[x][y] = sea[x][y] - cnt
    return temp

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        a, b = queue.popleft()
        for idx in range(4):
            na = a + dx[idx]
            nb = b + dy[idx]

            if not visited[na][nb] and sea[na][nb]:
                visited[na][nb] = 1
                queue.append((na, nb))
# 입력
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
# 델타
ice = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
while True:
    cnt += 1
    sea = melt()

    island_cnt = 0
    visited = [[0] * M for _ in range(N)]
    for x in range(1, N-1):
        for y in range(1, M-1):
            if sea[x][y] > 0 and not visited[x][y]:
                bfs(x, y)
                island_cnt += 1

    if island_cnt >= 2:
        print(cnt)
        break
    elif island_cnt == 0:
        print(0)
        break
