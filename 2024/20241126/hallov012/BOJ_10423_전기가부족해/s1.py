import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        p[x] = y

n, m, k = map(int, input().split())
power = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

p = list(range(n+1))
for i in range(k-1):
    union(power[i], power[i+1])

ans = 0
edge_cnt = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        ans += w
        edge_cnt += 1
        if edge_cnt == n-1:
            break

print(ans)