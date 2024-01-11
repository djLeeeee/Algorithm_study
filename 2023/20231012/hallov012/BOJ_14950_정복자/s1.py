import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

input = sys.stdin.readline

n, m, t = map(int, input().split())
p = list(range(n+1))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
ans, edges_cnt = 0, 0
for i in range(m):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        ans += c + (t * edges_cnt)
        edges_cnt += 1

print(ans)