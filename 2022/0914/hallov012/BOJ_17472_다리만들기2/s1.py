import sys
from collections import deque
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

def kruskal():
    global ans
    edge_cnt, idx = 0, 0
    while edge_cnt < num-2:
        if idx == len(edges):
            ans = -1
            break
        x = edges[idx][0]
        y = edges[idx][1]
        dist = edges[idx][2]
        if find(x) != find(y):
            union(x, y)
            edge_cnt += 1
            ans += dist
        idx += 1

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
island = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
num = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] and not island[i][j]:
            island[i][j] = num
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] and not island[nx][ny]:
                            island[nx][ny] = num
                            que.append((nx, ny))
            num += 1

edges = []
for i in range(n):
    for j in range(m):
        if island[i][j]:
            start = island[i][j]
            for d in range(4):
                dist = 0
                nx = i + dx[d]
                ny = j + dy[d]
                while 0 <= nx < n and 0 <= ny < m:
                    if island[nx][ny] == start:
                        break
                    elif island[nx][ny] == 0:
                        dist += 1
                        nx += dx[d]
                        ny += dy[d]
                    else:
                        if dist >= 2 and (start, island[nx][ny], dist) not in edges:
                            edges.append((start, island[nx][ny], dist))
                        break
p = list(range(num))
ans = 0
edges.sort(key=lambda x: x[2])
kruskal()
print(ans)
