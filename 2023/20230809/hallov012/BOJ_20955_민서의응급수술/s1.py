import sys
sys.setrecursionlimit(10**6)
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
p = list(range(n+1))
ans = 0
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x, y)
    else:
        # 사이클 존재 => 연결 끊기
        ans += 1

node = set()
for i in range(1, n+1):
    node.add(find(i))

# 연결 추가
ans += len(node) - 1
print(ans)
