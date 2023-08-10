# https://www.acmicpc.net/problem/11085
import sys
sys.stdin = open("./input/11085.txt")
input = sys.stdin.readline
# ----------------------------------------
ans = sys.maxsize
p, w = map(int, input().split())
b, c = map(int, input().split())

parents = [i for i in range(p)]
edges = []

for _ in range(w):
    s, e, width = map(int, input().split())
    edges.append((width, s, e))

edges.sort(reverse=True)

def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents, n1, n2):
    p1, p2 = find(parents, n1), find(parents, n2)
    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2
    
for (width, s, e) in edges:
    if find(parents, s) != find(parents, e):
        union(parents, s, e)
    if find(parents, b) == find(parents, c):
        print(width)
        break

