import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y
    cost[y] += cost[x]


n, m, q = map(int, input().split())
g = defaultdict(list)
edges = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(m)]

tmp = [False] * (m+1)
remove = []

p = list(range(n+1))
cost = [1] * (n+1)

for _ in range(q):
    k = int(input())
    remove.append(k)
    tmp[k] = True

# 제거하지 않을 애들 연결
for i in range(1, m+1):
    if not tmp[i]:
        x, y = edges[i]
        if find(x) != find(y):
            union(x, y)

ans = 0
# 제일 마지막에 끊은 것 부터 다시 연결
for k in reversed(remove):
    x, y = edges[k]
    # 만약 연결이 안되어 있다면 원래 이 간선으로 인해 이어져 있던 것 => 비용 발생
    if find(x) != find(y):
        ans += cost[find(x)] * cost[find(y)]
        union(x, y)

print(ans)



