import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

n = int(input())
p = list(range(n+1))
edges = []
for i in range(1, n+1):
    edges.append((0, i, int(input())))

for i in range(1, n+1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if i == j:
            continue
        edges.append((i, j, row[j]))

edges.sort(key=lambda x: x[2])

ans = 0
edges_cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        edges_cnt += 1
        if edges_cnt == n:
            break

print(ans)

