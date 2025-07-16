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

n = int(input())
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))
edges = []
for p in range(3):
    sorted_planets = sorted(planets, key=lambda x:x[p])
    for i in range(1, n):
        p1, idx1 = sorted_planets[i][p], sorted_planets[i][3]
        p2, idx2 = sorted_planets[i-1][p], sorted_planets[i-1][3]
        edges.append((idx1, idx2, abs(p1-p2)))
edges.sort(key=lambda x:x[2])

ans = 0
p = list(range(n+1))
edges_cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        edges_cnt += 1
    if edges_cnt == n-1:
        break
print(ans)




