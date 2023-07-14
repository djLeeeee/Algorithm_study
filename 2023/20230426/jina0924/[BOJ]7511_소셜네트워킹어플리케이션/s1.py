# 백준 7511번 소셜 네트워킹 어플리케이션

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


T = int(input())
for tc in range(1, T + 1):
    print(f'Scenario {tc}:')
    n = int(input())
    p = [i for i in range(n + 1)]
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) != find(v):
            print(0)
        else:
            print(1)
    print()
