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

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

p = list(range(n+1))
ans = 0
for i in range(m):
    x = edges[i][0]
    y = edges[i][1]
    c = edges[i][2]
    if find(x) != find(y):
        union(x, y)
    else:
        ans += c

p_set = set()
for i in range(1, n+1):
    p_set.add(find(i))

if len(p_set) == 1:
    print(ans)
else:
    print(-1)





