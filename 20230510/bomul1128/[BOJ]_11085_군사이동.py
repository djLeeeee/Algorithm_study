from sys import stdin

input = stdin.readline


def find(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


n, m = map(int, input().split())
ini, fin = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
roads.sort(key=lambda x: -x[2])
parent = list(range(n))
for a, b, c in roads:
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pa] = pb
        if find(ini) == find(fin):
            print(c)
            break
