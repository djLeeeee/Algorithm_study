import sys, math
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

def kruskal():
    global ans, edge_cnt
    idx = 0
    while edge_cnt > 0:
        x = edges[idx][0]
        y = edges[idx][1]
        if find(x) != find(y):
            union(x, y)
            edge_cnt -= 1
            ans += edges[idx][2]
        idx += 1

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(range(n+1))
gods = [list(map(int, input().split())) for _ in range(n)]
ans = 0
edges = []
# 선택해야할 간선의 수
edge_cnt = n-1
# 이미 연결되어있는 신들은 체크
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x, y)
        edge_cnt -= 1
# 연결 가능한 모든 경우의 수를 edges에 담아 줌
for i in range(n-1):
    for j in range(i+1, n):
        d = math.sqrt((gods[i][0] - gods[j][0])**2 + (gods[i][1] - gods[j][1])**2)
        edges.append((i+1, j+1, d))
edges.sort(key=lambda x: x[2])
kruskal()
print('%.2f' % ans)

