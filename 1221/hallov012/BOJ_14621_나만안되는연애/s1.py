import sys
sys.stdin = open('input.txt')

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
school = [0] + list(input().split())
p = list(range(n+1))
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if school[a] != school[b]:
        edges.append((a, b, c))
edges.sort(key=lambda x:x[2])

ans = 0
edge_cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        edge_cnt += 1
    if edge_cnt == n-1:
        break

if edge_cnt == n-1:
    print(ans)
else:
    print(-1)