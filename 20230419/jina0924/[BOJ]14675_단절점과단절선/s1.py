# 백준 14675번 단절점과 단절선

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        # 리프노드는 단절점이 될 수 없음
        if len(tree[k]) == 1:
            print('no')
        else:
            print('yes')
    else:
        # 사이클이 존재하지 않는 트리이므로 어느 간선을 지워도 단절선
        print('yes')