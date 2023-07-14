# 백준 21924번 도시 건설 - 크루스칼

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    px, py = find(x), find(y)
    if px <= py:
        p[py] = px
    else:
        p[px] = py


N, M = map(int, input().split())
total = 0
edges = []
p = [i for i in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    total += w
    edges.append((w, a, b))
edges.sort()
cnt, cost = 0, 0
for w, a, b in edges:
    if find(a) != find(b):
        cnt += 1
        union(a, b)
        cost += w
        if cnt == N - 1:
            break
if cnt == N - 1:
    print(total - cost)
else:
    print(-1)