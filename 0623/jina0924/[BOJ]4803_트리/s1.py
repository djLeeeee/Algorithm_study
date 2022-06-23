# 백준 4803번 트리 - 16%

import sys
sys.stdin = open('input.txt')


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


tc = 0
while True:
    v, e = map(int, input().split())
    if v == 0:
        break
    tree = {}
    for i in range(v+1):
        tree[i] = []
    for _ in range(e):
        a, b = map(int, input().split())
        tree[a].append(b)
    cycle = {0}
    p = [i for i in range(v+1)]
    for i in range(1, v+1):
        c_list = tree.get(i)
        for c in c_list:
            root = find_set(i)
            if root != find_set(c):
                union(i, c)
            else:
                cycle.add(root)
    tc += 1
    T = len(set(p) - cycle)
    if not T:
        print(f'Case {tc}: No trees.')
    elif T == 1:
        print(f'Case {tc}: There is one tree.')
    elif T > 1:
        print(f'Case {tc}: A forest of {T} trees.')