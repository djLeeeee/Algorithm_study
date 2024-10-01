import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    p[y] = x
    size[x] += size[y]

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    F = int(input())
    name_idx = {}
    idx = 0
    size = []
    p = []
    for _ in range(F):
        a, b = input().split()
        for k in (a, b):
            if k not in name_idx.keys():
                name_idx[k] = idx
                p.append(idx)
                size.append(1)
                idx += 1
        x, y = name_idx[a], name_idx[b]
        union(x, y)
        print(size[find(x)])