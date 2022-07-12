import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x

input = sys.stdin.readline

n, m = map(int, input().split())
data = [input() for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 현재 위치에 따른 dx, dy의 이동 index
direction = {'N': 0, 'S': 1, 'W': 2, 'E': 3}

p = list(range(n*m))
for x in range(n):
    for y in range(m):
        temp = data[x][y]
        nx = x + dx[direction[temp]]
        ny = y + dy[direction[temp]]
        now = m*x + y
        next = m*nx + ny
        if find(now) != find(next):
            union(now, next)

# 정확한 부모를 찾아 ans에 set으로 저장
ans = set([find(p[i]) for i in range(n*m)])
print(len(ans))





