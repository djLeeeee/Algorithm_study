# 백준 20955번 민서의 응급 수술

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    px, py = find(x), find(y)
    p[py] = px


N, M = map(int, input().split())
cnt = 0
p = [i for i in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    if find(u) == find(v):
        cnt += 1
        continue
    union(u, v)
for i in range(1, N + 1):
    p[i] = find(p[i])
cnt += len(set(p)) - 2
print(cnt)