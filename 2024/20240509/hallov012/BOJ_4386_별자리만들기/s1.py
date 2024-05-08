import math
import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        p[x] = y
        return True
    return False

input = sys.stdin.readline

n = int(input())

stars = [tuple(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        x, y = stars[i]
        p, q = stars[j]
        d = math.sqrt((x-p)**2 + (y-q)**2)
        edges.append((d, i, j))
edges.sort()
p = list(range(n))
ans = 0
edge_cnt = 0
for d, x, y in edges:
    if union(x, y):
        ans += d
        edge_cnt += 1
    if edge_cnt == n-1:
        break

print(round(ans, 2))