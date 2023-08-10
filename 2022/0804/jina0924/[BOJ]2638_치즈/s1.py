# 백준 2638번 치즈

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline
from copy import deepcopy
from collections import deque


def melt(cheese):
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
    time = 0                                    # 치즈가 녹는 데에 걸리는 시간을 담을 변수
    while True:                                 # 치즈가 전부 녹을때까지 반복
        queue = deque([(0, 0)])                 # 모눈종이 가장자리에 치즈가 없으니까 좌상단부터 시작
        time += 1
        new_cheese = deepcopy(cheese)           # 변화된 치즈 값을 담을 리스트 마련
        while queue:                            # 외부 공간 순회
            r, c = queue.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 < nr < N-1 and 0 < nc < M-1 and cheese[nr][nc] == 1:   # 공기와 닿는 치즈면이면
                    new_cheese[nr][nc] += 1                                 # new_cheese에 표시해줌
                elif 0 <= nr < N and 0 <= nc < M and cheese[nr][nc] == 0:   # 연결된 외부 공간이라면
                    cheese[nr][nc] = 10                                     # 방문표시 해주고
                    queue.append((nr, nc))                                  # queue에 담아서 이어 순회함
        for r in range(N):
            for c in range(M):
                if new_cheese[r][c] >= 3:       # 값이 3 이상 = 2번 이상 실내온도의 공기와 접촉 => 녹아 없어짐
                    new_cheese[r][c] = 0
                elif new_cheese[r][c] == 2:     # 값이 2 = 1번 공기와 접촉 => 녹지 않음
                    new_cheese[r][c] = 1
        cnt = sum([sum(new_cheese[i]) for i in range(N)])   # 남아있는 치즈 개수
        if cnt == 0:
            return time
        cheese = deepcopy(new_cheese)           # 변화된 치즈 값으로 갱신


N, M = map(int, input().split())                # N: 모눈의 가로 크기, M: 모눈의 세로 크기
cheese = [list(map(int, input().split())) for _ in range(N)]
print(melt(cheese))
