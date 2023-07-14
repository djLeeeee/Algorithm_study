# 시간초과
# dfs(stack 사용)해서 최장 거리 구하고 해당 최장 거리를 구성하는 좌표들을 dp에 저장
# 아마 최장 거리 좌표들을 갱신하는 과정(long)에서 시간초과 났을 듯,,

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# r, c에서 출발하는 최장 거리 구하는 함수
def solution(start_r, start_c):
    max_route = 1
    Q = deque([(start_r, start_c, 1)])
    store = []
    long = []

    while Q:
        sr, sc, route = Q.pop()
        store.append((sr, sc, route))

        # 1) 현재 보고 있는 값이 dp에 저장된 값일 때, 최장 경로 갱신
        if dp[sr][sc]:
            if max_route < route + dp[sr][sc] - 1:
                max_route = route + dp[sr][sc] - 1
                long = deepcopy(store)

            while Q and store:
                if store[-1][-1] >= Q[-1][-1]:
                    store.pop()
                else:
                    break
            continue

        # 2) dp에 저장되지 않은 값일 때, 상하좌우 보면서 stack에 가능한 좌표 넣어두기
        flag = 0
        for d in range(4):
            r = sr + delta[d][0]
            c = sc + delta[d][1]
            if 0 <= r < N and 0 <= c < N and forest[r][c] > forest[sr][sc]:
                flag = 1
                Q.append((r, c, route+1))

        # 막다른 길이라면, 최장경로 갱신해서 long에 저장
        if flag == 0:
            if max_route < route:
                max_route = route
                long = deepcopy(store)

            # 다음 경로를 준비하기 위해 다음 경로와 겹치지 않는 부분은 제거 -> 이 과정에서 시간 초과 예상
            while Q and store:
                if store[-1][-1] >= Q[-1][-1]:
                    store.pop()
                else:
                    break

    # 최장 경로를 dp에 저장하고 최장 경로를 구성하는 다른 좌표들도 1씩 빼서 dp에 역순으로 저장
    dp[start_r][start_c] = max_route
    while len(long) > 1:
        rr, cc, val = long.pop()
        dp[rr][cc] = max_route - (val - 1)


# 0. input 받기
N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

# 1. dp에 저장되있지 않은 출발점 돌면서 최장 거리 구하고, 최대값 갱신
max_val = 1
dp = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not dp[r][c]:
            solution(r, c)
        max_val = max(max_val, dp[r][c])

print(max_val)