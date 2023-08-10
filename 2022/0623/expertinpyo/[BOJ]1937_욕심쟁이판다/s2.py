# dfs
# 1. 이미 점에 대한 최댓값이 있을 때
# 2. 방문한 적이 없는 점일 때
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if ansList[x][y]:
        return ansList[x][y]

    ansList[x][y] = 1
    for d in di:
        new_x, new_y = x + d[1], y + d[0]
        if 0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y] > arr[x][y]:
            ansList[x][y] = max(ansList[x][y], dfs(new_x, new_y)+1)

    return ansList[x][y]

n = int(input())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(map(int, input().split())) for _ in range(n)]

ansList = [[0] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)




