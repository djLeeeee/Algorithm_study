import sys
from collections import deque
sys.stdin = open('input.txt')

"""
N, M (N줄에 걸쳐 M개)
-1 : 치료제
0 : 감염아직
1: 1번
2: 2번
1, 2는 하나씩 주어짐

각 바이러스 후보지를 일단 저장해놓고, 겹치면 3번확정으로 보내고,
안겹치면 다 지나온 다음에 1번 확정 2번 확정으로 보낸다. 
1번후보 []
1번 확정[]
2번후보 []
2번 확정[]
3번 확정[]
"""
# 상하좌우로 돌면서 감염시키기 때문에
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread():
    while virus[1] or virus[2]:
        tmp_1, tmp_2 = set(), set()

        while virus[1]:
            x, y = virus[1].popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and village[nx][ny] == 0:
                    tmp_1.add((nx, ny))

        while virus[2]:
            x, y = virus[2].popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and village[nx][ny] == 0:
                    tmp_2.add((nx, ny))

        tmp_3 = tmp_1 & tmp_2
        for x, y in tmp_3:
            village[x][y] = 3

        tmp_1 = tmp_1 - tmp_3
        for x, y in tmp_1:
            village[x][y] = 1
            virus[1].append((x, y))

        tmp_2 = tmp_2 - tmp_3
        for x, y in tmp_2:
            village[x][y] = 2
            virus[2].append((x, y))

N, M = map(int, input().split())
virus = [0, deque(), deque()]
village = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if 1 in village[i]:
        virus[1].append((i, village[i].index(1)))
    if 2 in village[i]:
        virus[2].append((i, village[i].index(2)))
spread()
cnt1, cnt2, cnt3 = 0, 0, 0
for i in range(N):
    cnt1 += village[i].count(1)
    cnt2 += village[i].count(2)
    cnt3 += village[i].count(3)
print(cnt1, cnt2, cnt3)