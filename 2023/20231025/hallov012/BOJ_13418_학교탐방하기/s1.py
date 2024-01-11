import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

def solve(edges):
    p = list(range(n+1))
    cnt = 0
    edges_cnt = 0
    for i in range(m + 1):
        a, b, c = edges[i]
        if find(a) != find(b):
            union(a, b)
            edges_cnt += 1
            cnt += c
    return cnt ** 2

input = sys.stdin.readline

# 최소한의 길을 선택(어차피 n개 고를거임)
n, m = map(int, input().split())
edges = []
for _ in range(m+1):
    a, b, c = map(int, input().split())
    edges.append((a, b, 1-c))

min_edges = sorted(edges, key=lambda x: x[2])
p = list(range(n+1))
min_cnt = solve(min_edges)

max_edges = list(reversed(min_edges))
p = list(range(n+1))
max_cnt = solve(max_edges)

print(max_cnt - min_cnt)
