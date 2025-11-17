import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt')

input = sys.stdin.readline

def bfs(a, b):
    dist = [[-1] * m for _ in range(n)]
    dist[a][b] = 0
    que = deque([(a, b)])
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and arr[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))
    return dist

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    m, n = map(int, input().split())
    if (n, m) == (0, 0):
        break
    arr = []
    dust = []
    sx, sy = 0, 0
    for i in range(n):
        row = input().strip()
        arr.append(row)
        for j in range(m):
            if row[j] == 'o':
                sx, sy = i, j
            elif row[j] == '*':
                dust.append((i, j))
    flag = True
    dist_lst = []
    # 더러운 곳에서 다른 곳으로 가는데 걸리는 이동 횟수 저장
    for x, y in dust:
        dist = bfs(x, y)
        if dist[sx][sy] == -1:
            flag = False
        dist_lst.append(dist)
    if not flag:
        print(-1)
        continue

    cases = list(permutations(list(range(len(dust)))))
    ans = sys.maxsize
    for case in cases:
        x, y = sx, sy
        cnt = dist_lst[case[0]][x][y]
        for i in range(len(case)-1):
            now, next = case[i], case[i+1]
            nx, ny = dust[next]
            cnt += dist_lst[now][nx][ny]
        ans = min(ans, cnt)
    print(ans)







