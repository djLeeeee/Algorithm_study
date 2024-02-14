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

n = int(input())
edges = []
total = 0
for i in range(n):
    line = input()
    for j in range(n):
        if ord('a') <= ord(line[j]) <= ord('z'):
            d = ord(line[j]) - ord('a') + 1
            edges.append((i, j, d))
            total += d
        elif ord('A') <= ord(line[j]) <= ord('Z'):
            d = ord(line[j]) - ord('A') + 27
            edges.append((i, j, d))
            total += d

p = list(range(n+1))
edges.sort(key= lambda x:x[2])

cnt = 0
edge_cnt = 0
for x, y, d in edges:
    if find(x) != find(y):
        union(x, y)
        edge_cnt += 1
        cnt += d
    if edge_cnt == n-1:
        break

if edge_cnt == n-1:
    print(total - cnt)
else:
    print(-1)