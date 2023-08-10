# final
# dfs(재귀)로 최장경로 찾고 + memoization으로 거쳐간 경로에 있는 좌표 값에 저장해서 재사용

import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('input1.txt')
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 2-1. dfs: sr, sc 좌표에서 출발해서 갈 수 있는 최장 경로를 알려주는 재귀함수
def dfs(sr, sc):
    # 종료1 - memo에 저장된 값을 만났을 때, 해당 좌표의 memo값 반환
    if memo[sr][sc]:
        return memo[sr][sc]

    # 진행: 인접한 좌표(b, c, d, e)를 확인해서 갈 수 있는 좌표라면 -> 현재 좌표(a)의 최장 경로는 b, c, d, e에서의 최장 경로 + 1
    for d in range(4):
        nr = sr + delta[d][0]
        nc = sc + delta[d][1]
        if 0 <= nr < N and 0 <= nc < N and forest[nr][nc] > forest[sr][sc]:
            memo[sr][sc] = max(memo[sr][sc], dfs(nr, nc) + 1)

    # 종료 2 - 상하좌우 모두 확인하여 비어 있던 memo에 새로 저장했을 때, 해당 좌표의 memo 값 반환
    return memo[sr][sc]


# 0. input 받고 memoization 준비하기
N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]

# 1. 막다른 길 구하기
for r in range(N):
    for c in range(N):
        flag = 0
        for d in range(4):
            er = r + delta[d][0]
            ec = c + delta[d][1]
            if 0 <= er < N and 0 <= ec < N and forest[er][ec] > forest[r][c]:
                flag = 1
        if flag == 0:
            memo[r][c] = 1


# 2. memo에 등록되지 않은 칸들을 모두 돌면서 최장 경로를 memo에 저장하고, 최대값 갱신하기
max_val = 1
for r in range(N):
    for c in range(N):
        if not memo[r][c]:
            max_val = max(max_val, dfs(r, c))
print(max_val)
