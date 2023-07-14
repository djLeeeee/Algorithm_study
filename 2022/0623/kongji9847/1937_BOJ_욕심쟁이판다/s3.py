# 찐 최장만 살피기 -> 시간초과
# 완전탐색(dfs던 bfs던)으로 돌아다니면서 현재 dp에 있는 값이 돌아다니는 중에 얻은 value값보다 작으면 dp값 덮어 씌우기
# dp값이 고정되어 있는 것이 아니므로, 0 - 3 - 5라 했을 때 0 - 1 - 3 - 5로 갱신하면 3 - 5 계산을 또 해야된다.
# -> 피보나치 수열에서 f(3)계산의 중복을 막기 위해 memoization이 필요한 것과 동일한 개념

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(start_r, start_c):
    stack = [[start_r, start_c, 1]]
    while stack:
        r, c, val = stack.pop()
        if dp[r][c] < val:
            dp[r][c] = val

            for d in range(4):
                nr = r + delta[d][0]
                nc = c + delta[d][1]
                if 0 <= nr < N and 0 <= nc < N and forest[nr][nc] < forest[r][c]:
                    stack.append([nr, nc, val+1])

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not dp[r][c]:
            solution(r, c)

max_val = max(dp[0])
for i in range(1, N):
    max_val = max(max_val, max(dp[i]))

print(max_val)


