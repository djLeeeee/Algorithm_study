import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    edges = list(map(int, input().split()))

    parent = [0] * (V+1)
    children = [[] for _ in range(V+1)]
    for i in range(E):
        p, c = edges[2*i], edges[2*i+1]
        parent[c] = p
        children[p].append(c)

    ancestors = set()
    while a != 0:
        ancestors.add(a)
        a = parent[a]

    while b not in ancestors:
        b = parent[b]

    size = 0
    stack = [b]
    while stack:
        node = stack.pop()
        size += 1
        for c in children[node]:
            stack.append(c)

    print(f"#{tc} {b} {size}")

