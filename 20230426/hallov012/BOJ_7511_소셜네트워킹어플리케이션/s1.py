import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
      p[x] = y

input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    k = int(input())
    p = list(range(n+1))
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    print(f'Scenario {tc}:')
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()


