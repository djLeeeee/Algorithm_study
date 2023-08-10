# 백준 4803번 트리 - 시간초과 -> pypy3 통과

import sys
sys.stdin = open('input.txt')


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


tc = 0
while True:
    v, e = map(int, input().split())            # v: 정점의 개수, e: 간선의 개수
    cycle = {0}                                 # 사이클의 루트 노드를 담을 set
    p = [i for i in range(v+1)]
    if v == 0:
        break
    for _ in range(e):
        a, b = map(int, input().split())
        A = find_set(a)
        B = find_set(b)
        if A == B:                              # 새로 입력받은 값인데 루트 노드가 같다면 사이클
            cycle.add(A)
        else:                                   # 사이클이 아니라면 간선 정보에 따라 union
            union(a, b)
    for i in range(1, v+1):                     # 한 사이클 더 돌려줘야 루트 노드 제대로 찾음
        p[i] = find_set(i)
    tc += 1
    T = len(set(p) - cycle)
    if not T:
        print(f'Case {tc}: No trees.')
    elif T == 1:
        print(f'Case {tc}: There is one tree.')
    elif T > 1:
        print(f'Case {tc}: A forest of {T} trees.')