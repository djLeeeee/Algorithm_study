import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    parents = list(map(int, input().split()))
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    children = [[] for _ in range(n+1)]

    for i in range(2, n+1):
        p = parents[i-2]
        parent[i] = p
        depth[i] = depth[p] + 1
        children[p].append(i)

    ans = 0
    que = deque([1])
    # 이전에 방문한 노드
    prev = 1
    while que:
        cur = que.popleft()
        a, b = prev, cur
        # 깊이 맞추기
        while depth[a] > depth[a]:
            a = parent[a]
            ans += 1
        while depth[b] > depth[a]:
            b = parent[b]
            ans += 1
        # 같은 깊이에서 공통 조상까지
        while a != b:
            a = parent[a]
            b = parent[b]
            ans += 2
        prev = cur
        for child in children[cur]:
            que.append(child)

    print(f"#{tc} {ans}")


