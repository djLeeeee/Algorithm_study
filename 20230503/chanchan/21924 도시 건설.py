# https://www.acmicpc.net/problem/21924
import sys
from collections import deque
sys.stdin = open("./input/21924.txt")
input = sys.stdin.readline
max_val = sys.maxsize

N, M = map(int, input().split())
edges = []
parent = [n for n in range(N)]

def find(parent, n):
    if (parent[n] != n):
        parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, n1, n2):
    p1, p2 = find(parent, n1), find(parent, n2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

total_cost = 0
for m in range(M):
    n1, n2, cost = map(int, input().split())
    total_cost += cost
    edges.append((cost, n1 - 1, n2 - 1))

edges.sort()

for edge in edges:
    cost, n1, n2 = edge
    if (find(parent, n1) != find(parent, n2)):
        union(parent, n1, n2)
        total_cost -= cost

num_of_root = 0
for ind in range(N):
    if ind == parent[ind]:
        num_of_root += 1

if num_of_root > 1:
    print(-1)
else:
    print(total_cost)

