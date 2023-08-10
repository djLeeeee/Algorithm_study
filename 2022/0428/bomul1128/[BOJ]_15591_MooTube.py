from sys import stdin

input = stdin.readline


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b


m, n = map(int, input().split())
usado = []
for i in range(m - 1):
    p, q, r = map(int, input().split())
    usado.append((r, p, q))
usado.sort(reverse=True)
limit = []
origin = []
for j in range(n):
    k, v = map(int, input().split())
    limit.append((k, j))
    origin.append(v)
limit.sort()
parent = list(range(m + 1))
parent_num = [1] * (m + 1)
result = [0] * n
i = 0
while limit:
    limit_now, limit_index = limit.pop()
    while i <= m - 2 and usado[i][0] >= limit_now:
        x = usado[i][1]
        y = usado[i][2]
        total = parent_num[find(x)] + parent_num[find(y)]
        union(x, y)
        parent_num[find(x)] = total
        i += 1
    result[limit_index] = parent_num[find(origin[limit_index])] - 1
print(*result, sep='\n')
