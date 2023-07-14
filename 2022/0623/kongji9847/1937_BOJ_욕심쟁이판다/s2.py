# dfs + dp 이지만, 딱 출발지점의 최장 경로만 저장 1 2 3 4의 경로라면 4 0 0 0 로 dp에 저장되서 나중에 2를 지날 때 같은 계산을 또 해줘야 한다.

import sys
# sys.stdin = open('input1.txt')
input = sys.stdin.readline
from collections import deque

delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
def solution(start_r, start_c):
    max_route = 1
    Q = deque([(start_r, start_c, 1)])

    while Q:
        sr, sc, route = Q.pop()
        if dp[sr][sc]:
            max_route = max(max_route, route + dp[sr][sc]-1)
            continue

        flag = 0
        for d in range(4):
            r = sr + delta[d][0]
            c = sc + delta[d][1]
            if 0 <= r < N and 0 <= c < N and forest[r][c] > forest[sr][sc]:
                flag = 1
                Q.append((r, c, route+1))

        if flag == 0:
            max_route = max(max_route, route)

    dp[start_r][start_c] = max_route



N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

max_val = 1
dp = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        solution(r, c)
        max_val = max(max_val, dp[r][c])
print(max_val)
