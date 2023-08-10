from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def find(idx):
    if idx == parent[idx]:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


N = 10 ** 6
size = [1] * (N + 1)
parent = list(range(N + 1))
for _ in range(int(input())):
    o, *d = input().split()
    if o == 'I':
        x, y = map(int, d)
        fx = find(x)
        fy = find(y)
        if fx != fy:
            size[fy] += size[fx]
            parent[fx] = fy
    elif o == 'Q':
        x = int(d[0])
        print(size[find(x)])
