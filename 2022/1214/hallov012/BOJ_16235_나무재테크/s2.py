import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[5] * n for _ in range(n)]
add = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while k:
    new_trees = [[deque() for _ in range(n)] for _ in range(n)]
    # 봄, 여름, 겨울
    for i in range(n):
        for j in range(n):
            flag = True
            for z in trees[i][j]:
                if flag:
                    if arr[i][j] >= z:
                        arr[i][j] -= z
                        new_trees[i][j].append(z+1)
                        if not arr[i][j]:
                            flag = False
                    else:
                        flag = False
                        arr[i][j] += z//2
                else:
                    arr[i][j] += z//2
            # 겨울
            arr[i][j] += add[i][j]

    baby_trees = []
    for i in range(n):
        for j in range(n):
            for z in new_trees[i][j]:
                if not z % 5:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            baby_trees.append((nx, ny))

    for x, y in baby_trees:
        new_trees[x][y].appendleft(1)

    k -= 1
    trees = new_trees

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)

