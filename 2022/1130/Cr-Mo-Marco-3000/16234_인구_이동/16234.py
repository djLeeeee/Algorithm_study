import sys, collections

input = sys.stdin.readline

N, L, R = input().strip().split()

crit = R - L

g = [list(map(int, input().strip().split())) for _ in range(N)]

day = 0
flag = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stock = g[i][j]
                Q = [(i, j)]


    if flag == 0:
        break
    else:
        flag = 1

print(day)
